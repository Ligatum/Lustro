# Lustro API V1 — Architecture

This document describes the architecture, execution semantics, and
binding references for Lustro. For a quick start, see [README](README.md).

---

## 1. Architecture at a Glance

### Design Principles

- Single internal transformation engine shared by all public modules.
- Minimalism and a straightforward pipeline. Simple things work, when organized.
- Stateless (Hash) and stream-oriented (PRNG, XOF) execution modes.
- Explicit domain separation for every public primitive via domain tags.

### Diagram

```text
                    Core Transformation
                 evaluate_scalar() / stream_step()
                              │
              ┌───────────────┴───────────────┐
              │                                │
        Absorption Layer                Branch Derivation
      absorb_with_domain()          prepare_base + derive_branch_stream
              │                                │
   ┌──────────┴──────────┐          ┌──────────┴──────────┐
   │                     │          │                     │
Domain::Hash          Domain::Xof   Seed + StreamId    Current state + id
   │                     │          (Domain::Prng)         (fork)
   ▼                     ▼             │                     │
 Hash128/             StreamState      ▼                     ▼
 Hash256                  │        StreamState           StreamState
   │                      ▼                                (child)
   ▼                    XOF             │
  Hash              (stream_step()      ▼
                      per refill)      PRNG
                                   (stream_step()
                                    per refill)


                    ── Batch execution (parallel path) ──

absorb_hash256_batch_into        StreamLane           StreamLane
absorb_hash128_batch_into             │                    │
        │                             │                    │
dispatch_hash256_batch_into      dispatch_streams()  dispatch_streams()
dispatch_hash128_batch_into           │                    │
        │                             │                    │
    Hash Batch                   PRNG Batch           XOF Batch
                                                    (independent absorption,
                                                     lockstep dispatch)
```

All public primitives use the same internal engine through
`evaluate_scalar()` and `stream_step()`. `absorb_with_domain()`
and `StreamState` are built on top of that engine.

---

## 2. Core Model

- The state is 256-bit, represented as `(s0: u128, s1: u128)`.
- The state is evaluated in two modes:
  - **Stateless** — `evaluate_scalar()`, a single IDM + ERD with `step = 0`.
  - **Stateful** — `stream_step()`, the same IDM + ERD driven by a
    step counter, called once per output block.
- Hash and XOF both *initialize* their state via absorption
  (`absorb_with_domain`); PRNG initializes via seed + identifier derivation.
- PRNG and XOF *consumption* (byte/block output) both go through the same
  `StreamState`.

See [§5 Engine](#5-engine) for engine details.
Absorption padding is described in [§4 Absorption / Hash & XOF-Init Model](#4-absorption--hash--xof-init-model).

---

## 3. Domain Separation

Each construction uses a distinct domain tag, XORed into the initial state:

```text
Domain::Hash = 0x01
Domain::Prng = 0x02
Domain::Xof  = 0x03
```

Hash, PRNG, and XOF each use a distinct domain. `fork()` reuses the parent's
domain (`Domain::Prng` for PRNG and `Domain::Xof` for XOF).

---

## 4. Absorption / Hash & XOF-Init Model

Hash and XOF share the same absorption mechanism, `absorb_with_domain()`;
they differ in what happens after absorption.

```text
Hash: message → absorption → digest (stateless, one-shot)
XOF:  message → absorption → StreamState → stream_step() → output (stateful)
```

**Absorption mechanics** (`absorb_with_domain`, `finalize_terminator`):

- The domain tag is XORed into `s0`, and the encoded bit-length is XORed into `s1`.
- Input is consumed in 32-byte blocks; each full block is XORed into
  `(s0, s1)` and passed through `evaluate_scalar`.
- If the input is a non-zero multiple of 32 bytes, no terminator round is performed.
- Otherwise, the final block is padded with `0x80` followed by zeros and passed
  through `finalize_terminator`, which performs one additional `evaluate_scalar()`
  call. If the remaining input is shorter than 16 bytes, `b0` is also XORed into
  `s1`.

**Hash finalization**: `Hash256` is raw `(s0 || s1)` state as 32
little-endian bytes; `Hash128` serializes only `s0` — see
[§10 Behavioral Guarantees](#10-behavioral-guarantees).

**XOF initialization**: the absorbed `(s0, s1)` becomes the initial
`StreamState`. All further output (`next_block`, `fill_bytes`, ...) uses the
same stream mechanics as PRNG — see [§6](#6-stream-model-streamstate).

---

## 5. Engine

Internal engine functions — all `pub(crate)`, not part of the public API.
Split across `core.rs`, `api.rs`, and `dispatch.rs`.

### Core Transformation

| Function | Description |
|---|---|
| `idm_scalar_ref` | IDM — Initial Diffusion Module; initial state mixing layer. |
| `erd_round_scalar_ref` | ERD — Evolving Representation Dynamics round; state permutation with Weyl counter perturbation. |
| `evaluate_scalar` | Single stateless IDM + ERD evaluation (`step = 0`). Used for message absorption (Hash/XOF) and branch derivation. |
| `stream_step` | Counter-driven IDM + ERD evaluation. Called by `StreamState::refill()` on every PRNG/XOF block advance. |

### Absorption Layer

| Function | Description |
|---|---|
| `absorb_with_domain` | Block-by-block message absorption with domain separation. See [§4](#4-absorption--hash--xof-init-model). |
| `absorb_hash256_batch_into` | Delegates N-message 256-bit batch hashing to `dispatch_hash256_batch_into`; writes directly into caller-provided `&mut [[u8;32]]`. |
| `absorb_hash128_batch_into` | Delegates N-message 128-bit batch hashing to `dispatch_hash128_batch_into`; writes directly into caller-provided `&mut [[u8;16]]`. |

### Branch Derivation Pipeline

This is the shared mechanism behind stream initialization (PRNG) and forking (PRNG/XOF, single and batch):

| Function | Description |
|---|---|
| `prepare_base` | Stage 1: applies the domain tag and `STREAM_INIT_MASK` to `(s0, s1)`. Accepts either seed-derived state or live stream state and can be reused for sibling derivations. |
| `derive_branch_stream` | Stage 2: XORs the identifier into `base_s1`, then calls `evaluate_scalar`. Returns `(s0, s1)` ready for `StreamState::new()`. |
| `fork_lane` | Per-lane fork helper: `prepare_base` + `derive_branch_stream` on raw `(s0, s1)` pairs. Used by `LustroPrngBatch`/`LustroXofBatch` `fork`/`fork_range`. |

### Dispatch Layer

| Function | Description |
|---|---|
| `dispatch_hash256_batch_into` | 256-bit batch evaluation using either the scalar or Rayon path, selected by workload. Writes directly into caller-provided `&mut [[u8;32]]`. |
| `dispatch_hash128_batch_into` | Same scalar/parallel split as the 256-bit variant. It simply omits `s1` serialization. |
| `dispatch_streams` | Lockstep single-step block generation for N independent `StreamLane`s. Scalar or Rayon-parallel path depends on workload size. |
| `dispatch_streams_many` | Multi-step block generation — advances each lane by `steps`. Output is stream-major and the shared Rayon pool is reused for parallel dispatches. |

Threshold values between scalar and parallel execution are listed in [§9 Execution Policy](#9-execution-policy).

---

## 6. Stream Model (`StreamState`)

Shared component used by both `LustroPrng` and `LustroXof`.

| Method | Description |
|---|---|
| `refill` | Advances the stream by one `stream_step()`; resets cursor to 0. |
| `fill_bytes` | Buffered byte output — continuous cursor; sequential split calls are equivalent to a single call of the concatenated length (see §10). |
| `read_bytes<N>` | Typed read of exactly N bytes (≤ 32); delegates to `fill_bytes`. |
| `read_full_block` | Returns one full 32-byte block; always triggers one engine step and resets the cursor to 32. |
| `fork` | Derives a new `StreamState` via `prepare_base` + `derive_branch_stream`. Cursor is not part of this branch derivation, but it *is* part of single-stream consumption state and is preserved by snapshots (see §8). It does not mutate `self`. |
| `to_parts` | Returns the complete internal state as `(s0: u128, s1: u128, step: u64, cursor: u8)`. Used by `export_snapshot()` on `LustroPrng` / `LustroXof`. |
| `from_parts` | Reconstructs `StreamState` from raw parts. Panics if `cursor > 32`. Used by `import_snapshot()` on `LustroPrng` / `LustroXof`. |

A new `StreamState` starts with `cursor = 32`; the first read triggers `refill()`.

---

## 7. Batch Model (`StreamLane`)

`StreamLane` is the block-oriented batch equivalent of `StreamState`, with minimal 
per-lane state `(s0, s1, step)` and no cursor. Batch output is always block-aligned. 
Each lane advances in full 32-byte blocks, with no byte-level consumption state. 
As a result, batch has no `next_u64()`-style API and its snapshot format has no cursor.

### Single Stream vs Batch

| | Single Stream (`StreamState`) | Batch (`StreamLane`) |
|---|---|---|
| Cursor | yes (0–32) | none (always block-aligned) |
| Output granularity | arbitrary byte count (`fill_bytes`) | fixed 32-byte blocks (`fill_blocks`) |
| State count | 1 | N independent lanes |
| Parallel execution | no | optional, size-dependent (see §9) |
| Snapshot | fixed 56 bytes, includes cursor | variable `16 + N×48` bytes, block-aligned |
| Derivation source | one seed (PRNG) / one message (XOF) | N independent lanes, same seed or N messages |

### Components

| Component | Purpose / API |
|---|---|
| `StreamLane` | Minimal per-lane state layout `(s0, s1, step)`. |
| `LustroPrngBatch` | Multi-stream execution context over a shared seed. `new()` — explicit stream IDs; `new_range()` — sequential stream IDs; `fill_blocks()` / `fill_blocks_many()` — write directly into caller-provided output via the dispatcher; `len()` / `is_empty()` — batch geometry. |
| `LustroXofBatch` | Multi-stream execution context derived from independently absorbed messages. Same `fill_blocks()` / `fill_blocks_many()` / `len()` / `is_empty()` surface as `LustroPrngBatch`; `new(messages)` absorbs each message independently before dispatch. |

`fill_blocks()` / `fill_blocks_many()` write directly into caller-provided
output and perform no per-call heap allocation.
The Rayon thread pool is initialized lazily on the first parallel dispatch
and reused afterwards.

---

## 8. Snapshot Model

Snapshots serialize generator state to a stable byte format for later
restoration.

- **Validation order**: snapshot `version` is checked first, then `kind`
  (rejecting e.g. a PRNG snapshot imported as XOF), then — for single-stream
  snapshots — `cursor` bounds, before any state field is decoded.
- **Single-stream** (`LustroPrngSnapshot`, `LustroXofSnapshot`): fixed
  56-byte layout — `version(1) | kind(1) | reserved(6) | s0(16) | s1(16) |
  step(8) | cursor(1) | reserved(7)`.
- **Batch** (`LustroPrngBatchSnapshot`, `LustroXofBatchSnapshot`):
  variable-length — 16-byte header (`version(1) | kind(1) | reserved(6) |
  lane_count(8)`) followed by `lane_count × 48` bytes, each lane encoding
  `s0(16) | s1(16) | step(8) | reserved(8)`. No cursor field — batch lanes are
  always block-aligned.

`SnapshotKind` values: `Prng`, `Xof`, `PrngBatch`, `XofBatch`.
`SnapshotError` values: `UnsupportedVersion`, `InvalidKind`, `InvalidCursor`,
`InvalidLength`.

---

## 9. Execution Policy

Thresholds used by the dispatch layer to select the scalar or Rayon path.

```text
Hash parallelization
  message-count threshold:  1664 messages
  total-byte threshold:     64 KiB

Stream parallelization (single-step, fill_blocks)
  stream-count threshold:   1536 streams
  parallel chunk size:      288 lanes

Multi-step stream parallelization (fill_blocks_many)
  work-size threshold:      1536 (lanes × steps)
  minimum chunk count:      2
  parallel chunk size:      34 lanes
```

The current thresholds were tuned on an Intel i5-11600K.

---

## 10. Behavioral Guarantees

These guarantees hold across Rust, Python, and C FFI layers.

### Stream semantics

- Typed reads (`next_u64`, `next_u128`) are little-endian, drawn from the same
  underlying byte stream as `fill_bytes`/`fill`/`*_fill`.
- `next_block()` always advances the stream by exactly one engine round and
  returns one 32-byte block, regardless of the cursor position before
  the call — the cursor is simply ignored and reset.
- `fill_bytes()` / `fill()` / `fill_into()` / `*_fill()` have a concatenation
  guarantee: splitting one large request into several sequential calls yields
  the same bytes as a single call, as long as no other stream-consuming call
  (`next_u64`/`next_u128`/`next_block`) is interleaved.
- Single-stream `export_snapshot()` / `import_snapshot()` (PRNG/XOF) resume
  exactly: the restored context continues from the exported `step` and
  `cursor`. Batch snapshots restore each lane's `(s0, s1, step)` state;
  batch lanes have no cursor (see §7 and §8).

### Fork semantics

- `fork()` (single-stream and batch, PRNG and XOF) always starts the child at
  `step = 0` — the child does not inherit the parent's step counter or cursor.
- The parent stream is unaffected by any number of `fork()` calls.
- Fork is deterministic: the same parent state and identifier produce the same
  child. The identifier is part of the branch derivation; different identifiers
  are intended to produce different derived streams.
- Two forks with the same identifier will be identical regardless of how many
  bytes were consumed from the parent's current output block.

### Hash semantics

- `hash128()` always equals the first 16 bytes of `hash256()`. Both use the
  same absorption path; `hash128()` only omits serialization of `s1`.

### Batch semantics

- Batch operations preserve lane/stream order end to end.
- `fill_blocks_many()` uses stream-major output: all requested blocks for
  lane 0, then all blocks for lane 1, and so on. This differs from
  calling `fill_blocks()` repeatedly, which advances every lane in lockstep
  and produces lane-major blocks per call. These two are not interchangeable output layouts.

### API robustness semantics

- **Misuse is fail-fast** — caller-supplied length/shape mismatches are treated
  as programming errors and may panic in the Rust API; see §12.1 Error Model. 
  This is distinct from malformed *runtime data* (e.g. corrupt snapshot bytes): 
  for APIs that explicitly validate external input, malformed input is reported through 
  `Result`, `LustroError`, or a null-pointer return, rather than being an intentionally 
  exposed panic path. See §13 for the FFI panic-strategy caveat (`panic = "abort"` vs `"unwind"`).
- **Snapshot kind is validated before decoding** — a PRNG snapshot cannot be
  imported as XOF (or vice versa), and a single-stream snapshot cannot be
  imported as a batch (or vice versa). A mismatch returns an error rather than
  silently producing a corrupt stream. See §8 for validation order.

---

## 11. Public API Surface

At the architecture level, Lustro exposes three primary constructions:

```text
Hash → message → fixed-size digest (stateless)
PRNG → seed + stream ID → deterministic byte stream (stateful)
XOF  → message → deterministic byte stream (stateful)
```

Batch APIs provide grouped execution over multiple independent inputs.
See [§7 Batch Model](#7-batch-model-streamlane).

Specific functions, arguments, and types for each are listed per binding
below.

---

## 12. Language Bindings

### 12.1 Rust API (pure Rust, no bindings)

**Functions**

| Module | Functions |
|---|---|
| API Version | `lustro_api_version()` |
| Hash | `hash256(message)`, `hash128(message)`, `hash256_many(messages)`, `hash128_many(messages)`, `hash256_many_into(messages, out)`, `hash128_many_into(messages, out)` |
| `LustroPrng` | `new(seed, stream_id)`, `next_u64()`, `next_u128()`, `next_block()`, `fill_bytes(out)`, `fork(id)`, `clone()`, `export_snapshot()`, `import_snapshot(snapshot)` |
| `LustroPrngBatch` | `new(seed, stream_ids)`, `new_range(seed, first_stream_id, count)`, `len()`, `is_empty()`, `fill_blocks(out)`, `fill_blocks_many(out, steps)`, `fork(ids)`, `fork_range(first)`, `clone()`, `export_snapshot()`, `import_snapshot(snapshot)` |
| `LustroXof` | `new(message)`, `next_u64()`, `next_u128()`, `next_block()`, `fill_bytes(out)`, `fork(id)`, `clone()`, `export_snapshot()`, `import_snapshot(snapshot)` |
| `LustroXofBatch` | `new(messages)`, `len()`, `is_empty()`, `fill_blocks(out)`, `fill_blocks_many(out, steps)`, `fork(ids)`, `fork_range(first)`, `clone()`, `export_snapshot()`, `import_snapshot(snapshot)` |

**Types**

| Type | Methods / Traits |
|---|---|
| `Hash128`, `Hash256`, `Seed256` | `as_bytes()`, `AsRef<[u8; N]>`, `AsRef<[u8]>`, `TryFrom<&[u8]>` |
| `Seed256` (additionally) | `from_bytes([u8; 32])` |
| `StreamId` | `get()` |
| `LustroPrngSnapshot`, `LustroXofSnapshot` | `to_le_bytes()` (56 bytes, fixed), `from_le_bytes()` |
| `LustroPrngBatchSnapshot`, `LustroXofBatchSnapshot` | `to_le_bytes()` (variable length), `from_le_bytes()` |
| `SnapshotKind` | `Prng`, `Xof`, `PrngBatch`, `XofBatch` — validated before snapshot state fields are decoded |
| `SnapshotError` | `UnsupportedVersion`, `InvalidKind`, `InvalidCursor`, `InvalidLength` |

**Optional Integrations**

`LustroPrng` implements `rand_core::RngCore` and `rand_core::SeedableRng`
under `feature = "rand"`.

- `SeedableRng::from_seed()`, `From<Seed256>`, and `From<[u8; 32]>` all create
  **stream 0**. Use `LustroPrng::new()` directly when a specific `StreamId` is
  required.

**Error Model**

The Rust API has only a few fallible operations: the four snapshot decoders
and the `TryFrom<&[u8]>` conversions for `Hash128`, `Hash256`, and `Seed256`.
Everything else is infallible, except for caller-supplied length/shape
mismatches, which are handled with Rust panics.

| Function(s) | Behavior |
|---|---|
| `LustroPrngSnapshot::from_le_bytes`, `LustroXofSnapshot::from_le_bytes`, `LustroPrngBatchSnapshot::from_le_bytes`, `LustroXofBatchSnapshot::from_le_bytes` | Returns `Result<Self, SnapshotError>`. |
| `Hash128::try_from`, `Hash256::try_from`, `Seed256::try_from` (via `TryFrom<&[u8]>`) | Returns `Result<Self, TryFromSliceError>` on wrong-length input. |
| `hash256_many_into` / `hash128_many_into` | Panics if `messages.len() != out.len()`. |
| `LustroPrngBatch::fill_blocks` / `LustroXofBatch::fill_blocks` | Panics if `out.len() != len()`. |
| `LustroPrngBatch::fill_blocks_many` / `LustroXofBatch::fill_blocks_many` | Panics if `out.len() != len() * steps` (or on `usize` overflow). |
| `LustroPrngBatch::fork` / `LustroXofBatch::fork` | Panics if `ids.len() != len()`. |
| Everything else (`new`, `next_*`, `fill_bytes`, single-stream `fork`, `clone`, `export_snapshot`, `import_snapshot(snapshot)`, `fork_range`, `hash256`, `hash128`, `hash256_many`, `hash128_many`) | Infallible — always succeeds for valid Rust-typed arguments. |

Note: these panics are plain Rust panics (`assert_eq!`), not `LustroError`
values — `LustroError` is part of the C FFI ABI only (see §12.3).

**Snapshot Roundtrip** (not shown in README Quick Start)

```rust
let snapshot = rng.export_snapshot();
let bytes = snapshot.to_le_bytes();               // 56 bytes

let snapshot2 = LustroPrngSnapshot::from_le_bytes(&bytes)?; // fallible
let mut restored = LustroPrng::import_snapshot(snapshot2);  // infallible
```

---

### 12.2 Python Bindings

**Functions**

| Module | Functions |
|---|---|
| API Version | `lustro_api_version()` |
| `LustroHashPy` | `hash256(message)`, `hash128(message)`, `hash256_many(messages)`, `hash128_many(messages)` |
| `LustroPrngPy` | `new(seed, stream_id)`, `next_u64()`, `next_u128()`, `next_block()`, `fill(size)`, `fill_into(buf)`, `clone_rng()`, `fork(id)`, `export_snapshot()`, `import_snapshot(bytes)` |
| `LustroPrngBatchPy` | `new(seed, stream_ids)`, `new_range(seed, first_stream_id, count)`, `len()`, `is_empty()`, `fill_blocks(out)`, `fill_blocks_many(steps, out)`, `fork(ids)`, `fork_range(first)`, `export_snapshot()`, `import_snapshot(bytes)` |
| `LustroXofPy` | `new(message)`, `next_u64()`, `next_u128()`, `next_block()`, `fill(size)`, `fill_into(buf)`, `clone_xof()`, `fork(id)`, `export_snapshot()`, `import_snapshot(bytes)` |
| `LustroXofBatchPy` | `new(messages)`, `len()`, `is_empty()`, `fill_blocks(out)`, `fill_blocks_many(steps, out)`, `fork(ids)`, `fork_range(first)`, `export_snapshot()`, `import_snapshot(bytes)` |

**Parameter Types**

Unless otherwise noted, scalar parameters for functions not listed here are
plain Python `int`/`bool` with no shape or dtype constraints. (Return values
vary by function — e.g. `next_block()` returns `bytes`, `hash256_many()`
returns a NumPy array; see the function tables above.) NumPy array
*parameters* are required only where noted below — all must be C-contiguous
or the call raises `ValueError`.

| Function | Parameter | Expected type |
|---|---|---|
| `LustroHashPy.hash256`/`hash128(message)` | `message` | Python `bytes`, any length |
| `LustroHashPy.hash256_many(data)` | `data` | `numpy.ndarray`, shape `(n, msg_len)`, dtype `uint8` → returns shape `(n, 32)`, dtype `uint8` |
| `LustroHashPy.hash128_many(data)` | `data` | `numpy.ndarray`, shape `(n, msg_len)`, dtype `uint8` → returns shape `(n, 16)`, dtype `uint8` |
| `LustroPrngPy(seed, stream_id)` | `seed` | Python `bytes`, exactly 32 bytes (`ValueError` otherwise) |
| | `stream_id` | Python `int`, `0 ≤ stream_id < 2¹²⁸` (`OverflowError` otherwise) |
| `LustroPrngPy.fill(size)` | `size` | Python `int` → returns `bytes` of that length |
| `LustroPrngPy.fill_into(buf)` | `buf` | Python `bytearray`, filled in place to `len(buf)` |
| `LustroPrngPy.fork(id)` | `id` | Python `int`, `0 ≤ id < 2¹²⁸` (`OverflowError` otherwise) |
| `LustroPrngPy.export_snapshot()` | — | returns `bytes`, exactly 56 bytes |
| `LustroPrngPy.import_snapshot(bytes)` | `bytes` | Python `bytes`, exactly 56 bytes (staticmethod) |
| `LustroPrngBatchPy.new(seed, stream_ids)` | `stream_ids` | Python `list[int]` (staticmethod) |
| `LustroPrngBatchPy.new_range(seed, first_stream_id, count)` | `first_stream_id`, `count` | Python `int`, Python `int` (staticmethod) |
| `LustroPrngBatchPy.fill_blocks(out)` | `out` | `numpy.ndarray`, shape `(n, 4)`, dtype `uint64`, `n == batch.len()` |
| `LustroPrngBatchPy.fill_blocks_many(steps, out)` | `out` | `numpy.ndarray`, shape `(n, steps, 4)`, dtype `uint64` |
| `LustroPrngBatchPy.fork(ids)` | `ids` | Python `list[int]`, `len(ids) == batch.len()` |
| `LustroXofPy(message)` | `message` | Python `bytes`, any length (including empty) |
| `LustroXofBatchPy.new(messages)` | `messages` | Python `list[bytes]` — **not** numpy; each element independently sized (staticmethod) |

**Python-Specific Notes**

- The following methods release the GIL while the underlying Rust computation
  runs (`py.allow_threads`), allowing other Python threads to run concurrently:
  `LustroHashPy.hash256`/`hash128`, `hash256_many`/`hash128_many`; `LustroPrngPy`/`LustroXofPy.fill`;
  `LustroPrngBatchPy`/`LustroXofBatchPy.fill_blocks`/`fill_blocks_many`. **`fill_into()` 
  does not release the GIL** — it writes into the caller's `bytearray` through an `unsafe` 
  borrow; the GIL prevents concurrent resize or drop of the buffer.
- `import_snapshot(bytes)` raises `ValueError` on malformed input (wrong
  length, unsupported version, or kind mismatch — e.g. a PRNG snapshot passed
  to `LustroXofPy`), mapping the Rust `SnapshotError` variants.
- Each 32-byte block, where represented as NumPy output, is four `uint64`
  values in little-endian order — not a separate encoding from the raw byte
  stream.

All other behavioral guarantees (fork step=0, hash128 truncation, snapshot
resume, concatenation guarantee) are as described in
[§10 Behavioral Guarantees](#10-behavioral-guarantees).

**Batch Example** (illustrates the NumPy contract; not in README)

```python
import numpy as np
from lustro import LustroPrngBatchPy

batch = LustroPrngBatchPy.new_range(seed, 0, 4)
out = np.empty((batch.len(), 4), dtype=np.uint64)
batch.fill_blocks(out)
```

---

### 12.3 C FFI Reference

C ABI exported through `extern "C"` functions, compatible with C and C++.

**Function Table**

| Module | Functions |
|---|---|
| API Version | `lustro_api_version()` |
| Hash | `lustro_hash256(data, data_len, out)`, `lustro_hash128(data, data_len, out)` |
| Hash Batch | `lustro_hash256_many(data_ptr, n, message_len, out_ptr)`, `lustro_hash128_many(data_ptr, n, message_len, out_ptr)`, `lustro_hash256_many_var(message_ptrs, n, message_lens, out_ptr)`, `lustro_hash128_many_var(message_ptrs, n, message_lens, out_ptr)` |
| PRNG | `lustro_prng_new(seed, stream_id_hi, stream_id_lo)`, `_free`, `_clone`, `_fill(out, out_len)`, `_next_u64`, `_next_u128`, `_next_block`, `_fork(id_hi, id_lo)`, `_export_snapshot(out)`, `_import_snapshot(bytes)` |
| PRNG Batch | `lustro_prng_batch_new(seed, ids_hi, ids_lo, n)`, `_new_range(seed, first_hi, first_lo, count)`, `_free`, `_len`, `_fill_blocks(out, out_len)`, `_fill_blocks_many(out, out_len, steps)`, `_fork(ids_hi, ids_lo, n)`, `_fork_range(first_hi, first_lo)`, `_snapshot_size`, `_export_snapshot(out, out_len)`, `_import_snapshot(bytes, len)` |
| XOF | `lustro_xof_new(message, message_len)`, `_free`, `_clone`, `_fill(out, out_len)`, `_next_u64`, `_next_u128`, `_next_block`, `_fork(id_hi, id_lo)`, `_export_snapshot(out)`, `_import_snapshot(bytes)` |
| XOF Batch | `lustro_xof_batch_new(message_ptrs, message_lens, n)`, `_free`, `_len`, `_fill_blocks(out, out_len)`, `_fill_blocks_many(out, out_len, steps)`, `_fork(ids_hi, ids_lo, n)`, `_fork_range(first_hi, first_lo)`, `_snapshot_size`, `_export_snapshot(out, out_len)`, `_import_snapshot(bytes, len)` |

`fork_range(ctx, first_hi, first_lo)` variants do not take a count. They
derive `ctx.len()` children with sequential IDs starting at `first`, equivalent
to calling `*_fork` with `ids = [first, first+1, ..., first+len()-1]`.
Likewise, `*_batch_new_range(seed, first_hi, first_lo, count)` is equivalent
to `*_batch_new(seed, ids, count)` with `ids = [first, ..., first+count-1]`.
IDs advance with wrapping `u128` arithmetic, so a range near `u128::MAX`
wraps back to `0`. The same applies to the Rust and Python APIs.

**1. Type Mapping**

| C Type | Rust Origin | Notes |
|---|---|---|
| `uint8_t*` | `*const u8` / `*mut u8` | byte buffer, in or out |
| `uintptr_t` | `usize` | platform-dependent width |
| `uint64_t` | `u64` | `stream_id_hi`/`_lo` components |
| `int32_t` | `LustroError` (`#[repr(i32)]`) | see Return Value Conventions |
| `uint32_t` | `u32` | `lustro_api_version()` only |
| opaque pointer | `*mut LustroPrng` / `*mut LustroPrngBatch` / `*mut LustroXof` / `*mut LustroXofBatch` | never dereference from C; pass through only |
| `const uint8_t* const*` | `&[&[u8]]` (array of message slices) | Used by variable-length message APIs such as `*_many_var(...)` and `lustro_xof_batch_new(...)`, together with a parallel `const uintptr_t*` of lengths |

Input/output byte buffers are checked for `NULL`; no separate alignment check
is performed. Scalar writes such as `*_next_u64` use `write_unaligned`.

**2. Calling Convention**

All exported functions use `extern "C"` and expose the platform's standard
C ABI. Do not bind as `stdcall`.

**3. Return Value Conventions**

There are three categories:

- **`LustroError` (`int32`)** — returned by hash, fill, next-value, and
  snapshot-export functions.

  | Value | Name | Meaning |
  |---|---|---|
  | 0 | `Ok` | success |
  | 1 | `InvalidLength` | buffer/length argument invalid |
  | 2 | `InvalidPointer` | required pointer is `NULL` (the library checks for `NULL`, not alignment — see Type Mapping notes below) |
  | 3 | `OutputTooSmall` | output buffer smaller than required |
  | 4 | `AlreadyFinalised` | context already finalised |
  | 5 | `VerificationFailed` | verification step failed |
  | 6 | `InternalPanic` | internal panic caught at FFI boundary |

  The enum contains all defined ABI error values, but V1 currently returns only
  `Ok`, `InvalidLength`, `InvalidPointer`, and `InternalPanic`.
  V1 does not distinguish an undersized output buffer from other invalid-length
  arguments. Both return `InvalidLength`; output lengths are checked against
  the exact expected size.

- **Pointer-returning functions** (`*_new`, `*_clone`, `*_fork`,
  `*_fork_range`, `*_import_snapshot`) — `NULL` indicates failure; no error
  code is returned.

- **Value-returning functions** (`*_len`, `*_snapshot_size` → `uintptr_t`;
  `lustro_api_version` → `uint32_t`) — value returned directly, no error path.

- **void-returning functions** (`*_free`) — no return value; safe to call
  with `NULL` (no-op).

**4. Required Buffer Sizes**

Output buffers:

| Function family | Buffer | Size |
|---|---|---|
| `lustro_hash256*` | `out` | 32 bytes per message |
| `lustro_hash128*` | `out` | 16 bytes per message |
| `*_next_u128` | `out` | 16 bytes |
| `*_next_block` | `out` | 32 bytes |
| `*_export_snapshot` (single-context, PRNG/XOF) | `out` | 56 bytes |
| `*_batch_fill_blocks` | `out` | `n_lanes × 32` bytes — matches `sizeof(...)` on a `[n][32]` array, as in the README batch example |
| `*_batch_fill_blocks_many` | `out` | `n_lanes × steps × 32` bytes |
| `*_batch_export_snapshot` | `out` | `16 + n_lanes × 48` bytes — call `*_batch_snapshot_size(ctx)` first |

Input buffers:

| Function family | Buffer | Size |
|---|---|---|
| `lustro_prng_new` / `lustro_prng_batch_new` / `lustro_prng_batch_new_range` | `seed` | 32 bytes, fixed |

**5. Ownership / Lifetime**

| Handle type | Created by | Freed by |
|---|---|---|
| `LustroPrng*` | `_new`, `_clone`, `_fork`, `_import_snapshot` | `lustro_prng_free` |
| `LustroPrngBatch*` | `_new`, `_new_range`, `_fork`, `_fork_range`, `_import_snapshot` | `lustro_prng_batch_free` |
| `LustroXof*` | `_new`, `_clone`, `_fork`, `_import_snapshot` | `lustro_xof_free` |
| `LustroXofBatch*` | `_new`, `_fork`, `_fork_range`, `_import_snapshot` | `lustro_xof_batch_free` |

`*_import_snapshot` returns an independent context with the same ownership
and cleanup rules as a context created by `*_new`.

**6. Null / Zero-Length Semantics**

The `n == 0` behavior depends on the return-value category. It does **not**
make every pointer argument optional; only array/data pointers whose length
is determined by `n` may be `NULL`:

- **`LustroError`-returning functions** (`*_many`, `*_many_var`,
  `*_batch_fill_blocks*`): with `n == 0`, the function returns
  `LustroError::Ok` without dereferencing the `n`-sized data/output pointers.
  Those pointers may be `NULL`. For `n > 0`, a required `NULL` pointer returns
  `InvalidPointer`.
- **Batch constructors and batch fork operations** (`*_batch_new`,
  `*_batch_fork`, `*_batch_fork_range`, etc.): with `n == 0`, the function
  returns a valid empty context rather than `NULL`. For example,
  `lustro_xof_batch_new(..., n = 0)` returns an empty `LustroXofBatch`.
  A `NULL` result otherwise only indicates that no context was created; it
  does not distinguish invalid input from a panic caught by `catch_unwind`.
- **Fixed-size inputs unrelated to `n` still require a valid pointer.**
  For example, `lustro_prng_batch_new(seed, ids_hi, ids_lo, n)` always
  requires a valid 32-byte `seed`; a `NULL` seed returns `NULL`, even when
  `n == 0`. Only the `n`-sized `ids_hi`/`ids_lo` arrays are exempt from the
  `NULL` check when `n == 0`.

**7. Thread Safety**

`LustroPrng`, `LustroPrngBatch`, `LustroXof`, and `LustroXofBatch` contain only
plain state (`u128`/`u64`/`u8` fields) and provide no internal synchronization.
All mutating FFI functions operate through `&mut *ctx`. Using the same handle concurrently 
from multiple threads without external synchronization causes a data race. Use a separate 
handle per thread, or synchronize access to handles shared across threads.

**8. Minimal Examples**

**C — hash + basic PRNG:**

```c
uint8_t out[32];
LustroError err = lustro_hash256(data, data_len, out);

LustroPrng *ctx = lustro_prng_new(seed, 0, 0);
uint64_t val;
lustro_prng_next_u64(ctx, &val);
lustro_prng_free(ctx);
```

**PRNG lifecycle with snapshot and fork:**

```c
uint8_t seed[32] = { /* 32 bytes */ };
LustroPrng *ctx = lustro_prng_new(seed, 0, 0);
if (!ctx) { /* handle failure */ }

uint8_t snap[56];
lustro_prng_export_snapshot(ctx, snap);

LustroPrng *restored = lustro_prng_import_snapshot(snap);
LustroPrng *child = lustro_prng_fork(ctx, 0, 42);

lustro_prng_free(child);
lustro_prng_free(restored);
lustro_prng_free(ctx);
```

**Python (ctypes) — input/output buffer mapping:**

This repository's reference Python wrapper maps input byte buffers to
`ctypes.c_char_p` and writable output buffers to
`ctypes.create_string_buffer()`. Other bindings may choose different but
equivalent representations.

```python
lib.lustro_hash256(data, ctypes.c_size_t(data_len), out)

ctx = lib.lustro_prng_new(seed, ctypes.c_uint64(0), ctypes.c_uint64(0))
val = ctypes.c_uint64(0)
lib.lustro_prng_next_u64(ctx, ctypes.byref(val))
lib.lustro_prng_free(ctx)
```

**9. Header Distribution**

`lustro.h` is published with each release. Use the header matching the linked
library version; do not copy or edit it manually between versions.

`lustro.h` is generated by `build.rs` through `cbindgen` when the crate is
built with `--features ffi`. The C FFI module is also gated by this feature;
Python bindings require `--features python`.

**C FFI-Specific Behavioral Notes** (in addition to §10)

- `*_next_u128` writes 16 raw little-endian bytes from the same stream as
  `*_fill`.
- `*_fill` and `*_batch_fill_blocks` preserve the concatenation guarantee from
  §10. `*_batch_fill_blocks_many` uses stream-major output, so matching it
  against repeated `*_batch_fill_blocks` calls requires reordering the latter's
  output first.
- `*_import_snapshot` returns `NULL` for malformed input. Rust and Python
  report the same errors through `SnapshotError` and the corresponding Python
  exception.

---

## 13. Security & Memory Model

1. **`Seed256` is `Copy`** — copying it duplicates the underlying seed bytes.
   This version does not provide secret-memory protection.
2. **No automatic zeroization** — `Seed256` and internal stream state are not
   cleared on drop.
3. **No hidden generator state** — each PRNG/XOF instance owns its own state.
   The Rayon thread pool used for batch parallelism is shared execution state,
   not generator state.
4. **FFI panic behavior depends on the panic strategy.** With
   `panic = "unwind"` (the `release-ffi` profile), the FFI boundary catches
   Rust panics and returns `LustroError::InternalPanic`. With the default
   `panic = "abort"` release profile, a panic terminates the process instead.
   Use `release-ffi` or an equivalent `panic = "unwind"` profile if
   `InternalPanic` handling is required.
5. **Thread safety** — the underlying Rust contexts
   (`LustroPrng`, `LustroPrngBatch`, `LustroXof`, `LustroXofBatch`) provide no
   internal synchronization. Shared handles or objects must not be mutated
   concurrently without the synchronization required by the binding.
   For C FFI, this means caller-side synchronization around shared pointers;
   Python also applies the usual GIL and object-borrowing rules.

API robustness properties such as fail-fast misuse handling and snapshot-kind
validation are behavioral contracts, not security properties; see §8 and §10.
Fork, clone, and determinism guarantees are also covered by §10.
