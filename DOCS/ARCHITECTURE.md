Lustro API V1
--------------



*Quick Architecture Overview*


```text
                        IDM
                         │
                        ERD
                         │
                   evaluate_scalar()
                         │
                         ▼
        ┌────────────────┼─────────────────────┐
        │                │                     │
absorb_with_domain   Seed + StreamId   absorb_with_domain
(Domain::Hash)        (Domain::Prng)     (Domain::Xof)
        │                  │                  │
        ▼                  ▼                  ▼
Hash128/Hash256       StreamState        StreamState
        │            (stream_step()      (stream_step()
        │              per refill)        per refill)
        │                  │                  │
        ▼                  ▼                  ▼
      Hash               PRNG                XOF



absorb_hash256/128_into       StreamLane       StreamLane
        │                          │                │
dispatch_hash256/128_into    dispatch_streams  dispatch_streams
        │                          │                │
    Hash Batch                 PRNG Batch        XOF Batch
                                              (sequential absorb)
```

All public modules are compositions built on two internal engine entry points: evaluate_scalar and stream_step.

------------------------------------------------------------------------

## **Design Principles**

- Single internal transformation engine shared by all public modules.

- Minimalism and a straightforward pipeline. Simple things work, when organized.

- Stateless (Hash) and stream-oriented (PRNG, XOF) execution modes.

- Strict domain separation enforced for every public primitive via domain tags.

------------------------------------------------------------------------

## **Domain Separation**

Each public primitive carries a unique domain tag mixed into the initial state before any data is absorbed.

Domain::Hash = 0x01

Domain::Prng = 0x02

Domain::Xof = 0x03

fork(id) reuses the same domain tag as new()/absorb — Domain::Prng for PRNG, Domain::Xof for XOF. There is no separate fork domain.

------------------------------------------------------------------------

## **Engine**

Internal engine functions — all pub(crate), not part of the public API. Split across core.rs, api.rs, and dispatch.rs.

| **Function** | **Description** |
|----|----|
| **idm_scalar_ref** | IDM — Initial Diffusion Module; initial state mixing layer. |
| **erd_round_scalar_ref** | ERD — Evolving Representation Dynamics round; state-permutation and mixing layer with Weyl counter-based perturbation. |
| **evaluate_scalar** | Single stateless IDM + ERD evaluation (step = 0). Entry point for all Hash and branch-derivation paths. |
| **stream_step** | Counter-driven IDM + ERD evaluation. Called by StreamState::refill() on every PRNG/XOF block advance. |
| **absorb_with_domain** | Block-by-block message absorption with domain separation. Two-path padding: exact 32-byte multiples skip the terminator round; all others go through finalize_terminator. |
| **absorb_hash256_batch_into** | Delegates N-message 256-bit batch hashing to dispatch_hash256_batch_into; writes directly into caller-provided &mut \[\[u8;32\]\]. |
| **absorb_hash128_batch_into** | Delegates N-message 128-bit batch hashing to dispatch_hash128_batch_into; writes directly into caller-provided &mut \[\[u8;16\]\]. |
| **prepare_base** | Stage 1 of branch derivation - applies domain tag and STREAM_INIT_MASK to (s0, s1). Caller-agnostic: accepts either seed-derived (s0,s1) or live stream state. |
| **derive_branch_stream** | Stage 2 of branch derivation - XORs identifier into prepared base_s1 (base_s1 ^ id), then calls evaluate_scalar. Returns (s0, s1) ready for StreamState::new(). |
| **fork_lane** | Per-lane fork helper: prepare_base + derive_branch_stream on raw (s0, s1) pairs. Used by LustroPrngBatch::fork/fork_range and LustroXofBatch::fork/fork_range. |
| **dispatch_hash256_batch_into** | Multi-tiered 256-bit batch evaluation - scalar below MT threshold, Rayon parallel above. Zero-copy into &mut \[\[u8;32\]\]. |
| **dispatch_hash128_batch_into** | Multi-tiered 128-bit batch evaluation - same scalar/parallel split as hash256 variant. Omits s1 serialization. |
| **dispatch_streams** | Lockstep single-step block generation for N independent StreamLanes. Scalar or Rayon parallel path selected by workload size. |
| **dispatch_streams_many** | Vertical multi-step block generation - advances each lane by \`steps\` rounds per call. Stream-major output layout; amortizes Rayon pool-install cost. |

------------------------------------------------------------------------

## **StreamState**

Shared buffer management component used by LustroPrng and LustroXof. All methods are pub(crate) — not part of the public API.

| **Method** | **Description** |
|----|----|
| **refill** | Advances the stream by one stream_step(); resets cursor to 0. |
| **fill_bytes** | Buffered byte output — continuous cursor; sequential split calls are equivalent to a single call of the concatenated length. |
| **read_bytes\<N\>** | Typed read of exactly N bytes (≤ 32); delegates to fill_bytes. |
| **read_full_block** | Aligned 32-byte output; always triggers one engine step, unconditionally resetting the cursor to 32. |
| **fork** | Derives a new StreamState via prepare_base + derive_branch_stream. Ignores cursor — buffer position is not generator state. Does not mutate self. |
| **to_parts** | Returns the complete internal state as (s0: u128, s1: u128, step: u64, cursor: u8). Used by export_snapshot() on LustroPrng / LustroXof. |
| **from_parts** | Reconstructs StreamState from raw parts. Panics if cursor \> 32. Used by import_snapshot() on LustroPrng / LustroXof. |

------------------------------------------------------------------------

## **Batch Architecture & StreamLane**

<table style="width:98%;">
<colgroup>
<col style="width: 22%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr>
<th><strong>Component</strong></th>
<th><strong>Purpose / API</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>StreamLane</strong></td>
<td>Cache-friendly internal state layout (s0, s1, step); minimal internal execution state.</td>
</tr>
<tr>
<td><strong>LustroPrngBatch</strong></td>
<td>
High-performance multi-stream execution context.<br><br>
✦ new() explicit initialization via an arbitrary slice of stream IDs<br>
✦ new_range() efficient sequential stream ID construction<br>
✦ fill_blocks() zero-heap-allocation concurrent evaluation loop via dispatcher<br>
✦ fill_blocks_many() zero-allocation generation of multiple consecutive blocks per lane<br>
✦ len() / is_empty() batch geometry inspection
</td>
</tr>
<tr>
<td><strong>LustroXofBatch</strong></td>
<td>
High-performance multi-stream execution context derived from messages.<br><br>
✦ new(messages) absorbs each message sequentially<br>
✦ fill_blocks() zero-heap-allocation concurrent evaluation loop via dispatcher<br>
✦ fill_blocks_many() zero-allocation generation of multiple consecutive blocks per lane<br>
✦ len() / is_empty() batch geometry inspection
</td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

## **Public Modules**

| **Module** | **Internal Pipeline** |
|----|----|
| **Hash** | absorb_with_domain → evaluate_scalar → Hash128 / Hash256 |
| **Hash Batch (convenience)** | hash256_many / hash128_many → Vec\<Hash256/128\>, delegates to perf path |
| **Hash Batch (performance)** | hash256_many_into / hash128_many_into → dispatch → zero-alloc &mut \[\] |
| **PRNG** | Seed + StreamId → Domain-separated stream derivation → StreamState |
| **PRNG Batch** | StreamState → StreamLane → dispatch_streams |
| **PRNG Fork** | Current StreamState + Child StreamId → Domain-separated stream derivation → StreamState |
| **PRNG Batch Fork** | Current StreamLane + Child StreamId → StreamLane |
| **XOF** | Message → absorb_with_domain → StreamState |
| **XOF Batch** | Messages → absorb_with_domain (sequential) → StreamState → StreamLane → dispatch_streams |
| **XOF Fork** | Current StreamState + Child StreamId → Domain-separated stream derivation → StreamState |
| **XOF Batch Fork** | Current StreamLane + Child StreamId → StreamLane |

------------------------------------------------------------------------

## **Rust API (pure Rust, no bindings)**

| **Module** | **Functions** |
|----|----|
| **API Version** | lustro_api_version() |
| **Hash** | hash256(message), hash128(message), hash256_many(messages), hash128_many(messages), hash256_many_into(messages, out), hash128_many_into(messages, out) |
| **LustroPrng** | new(seed, stream_id), next_u64(), next_u128(), next_block(), fill_bytes(out), fork(id), clone(), export_snapshot(), import_snapshot(snapshot) **\[implements rand_core::RngCore and rand_core::SeedableRng (feature = "rand"); from_seed() creates stream 0\]** |
| **LustroPrngBatch** | new(seed, stream_ids), new_range(seed, first_stream_id, count), len(), is_empty(), fill_blocks(out), fill_blocks_many(out, steps), fork(ids), fork_range(first), clone(), export_snapshot(), import_snapshot(snapshot) |
| **LustroXof** | new(message), next_u64(), next_u128(), next_block(), fill_bytes(out), fork(id), clone(), export_snapshot(), import_snapshot(snapshot) |
| **LustroXofBatch** | new(messages), len(), is_empty(), fill_blocks(out), fill_blocks_many(out, steps), fork(ids), fork_range(first), clone(), export_snapshot(), import_snapshot(snapshot) |
| **Hash128, Hash256, Seed256** | as_bytes(), AsRef\<\[u8; N\]\>, AsRef\<\[u8\]\>, TryFrom\<&\[u8\]\> |
| **LustroPrngSnapshot, LustroXofSnapshot** | to_le_bytes(), from_le_bytes() |
| **LustroPrngBatchSnapshot, LustroXofBatchSnapshot** | to_le_bytes(), from_le_bytes() |
| **SnapshotKind** | Prng, Xof, PrngBatch, XofBatch — checked before any other snapshot field is trusted |
| **SnapshotError** | UnsupportedVersion, InvalidKind, InvalidCursor, InvalidLength |
| **Seed256 additionally** | from_bytes(\[u8; 32\]) |
| **StreamId** | get() |
| **Conversion / LustroPrng** | From\<Seed256\>, From\<\[u8; 32\]\> — both create stream 0; use new() for non-zero StreamId |

## Rust API — Behavioral Notes

**1. next_u128() returns a native u128 —** assembled from the same little-endian byte stream as fill_bytes() — not a separate encoding.

**2. next_block() always advances by exactly one engine round —** regardless of any partially-consumed buffer position; ignores and resets the internal cursor, and always returns exactly one 32-byte block.

**3. fill_bytes() has a concatenation guarantee —** splitting one large request into several sequential calls yields the same bytes as a single call for the concatenated length, as long as no other stream-consuming call (next_u64/next_u128/next_block) is interleaved. This applies to StreamState::fill_bytes() directly; the batch-level fill_blocks_many() analogue reorders output to stream-major layout instead (see C FFI Behavioral Note 3).

**4. export_snapshot()/import_snapshot() resume exactly —** the restored context continues from exactly the exported step and cursor.

**5. fork() always starts the child at step=0 —** true for every fork variant (single-stream and batch, PRNG and XOF) — the child does not inherit the parent's step counter or buffered cursor position.

**6. hash128() is the truncation of hash256() —** hash128(data) always equals the first 16 bytes of hash256(data), for any input — both call absorb_with_domain with the same domain; hash128 simply omits serializing the second half of state (s1).

## Rust API — Error Model

The only fallible functions in the Rust API are the four snapshot decoders. Everything else is infallible, or panics strictly on caller-supplied length/shape mismatch — never on malformed runtime data (“Misuse is fail-fast”).

| **Function(s)** | **Behavior** |
|----|----|
| LustroPrngSnapshot::from_le_bytes LustroXofSnapshot::from_le_bytes LustroPrngBatchSnapshot::from_le_bytes LustroXofBatchSnapshot::from_le_bytes | Returns Result\<Self, SnapshotError\> — the only fallible functions in the entire Rust API. SnapshotError variants: UnsupportedVersion, InvalidKind, InvalidCursor, InvalidLength. |
| hash256_many_into / hash128_many_into | Panics if messages.len() != out.len(). |
| LustroPrngBatch::fill_blocks / LustroXofBatch::fill_blocks | Panics if out.len() != len(). LustroError::InvalidLength. |
| LustroPrngBatch::fill_blocks_many / LustroXofBatch::fill_blocks_many | Panics if out.len() != len() \* steps (or on usize overflow). LustroError::InvalidLength. |
| LustroPrngBatch::fork / LustroXofBatch::fork | Panics if ids.len() != len(). NULL — fork is a pointer-returning function (no LustroError available). ids count mismatch is checked explicitly before the panicking call. |
| Everything else (new, next\_\*, fill_bytes, single-stream fork, clone, export_snapshot, import_snapshot(snapshot), fork_range, hash256, hash128, hash256_many, hash128_many) | Infallible — always succeeds, no panic path for valid Rust-typed arguments. |

**Minimal Usage Examples**

> // Hash
>
> let digest = hash256(b"hello world");
>
> // PRNG
>
> let seed = Seed256::from_bytes(\[0u8; 32\]);
>
> let mut rng = LustroPrng::new(&seed, StreamId(0));
>
> let x = rng.next_u64();
>
> // PRNG snapshot roundtrip
>
> let snapshot = rng.export_snapshot();
>
> let bytes = snapshot.to_le_bytes(); // 56 bytes
>
> let snapshot2 = LustroPrngSnapshot::from_le_bytes(&bytes)?; // fallible: version/kind/cursor checked
>
> let mut restored = LustroPrng::import_snapshot(snapshot2); // infallible
>
> // PRNG batch
>
> let ids: Vec\<StreamId\> = (0..4).map(StreamId).collect();
>
> let mut batch = LustroPrngBatch::new(&seed, &ids);
>
> let mut out = vec\![\[0u8; 32\]; batch.len()\];
>
> batch.fill_blocks(&mut out);
>
> // XOF
>
> let mut xof = LustroXof::new(b"absorbed message");
>
> let block = xof.next_block();

------------------------------------------------------------------------

## **Python Bindings**

| **Module** | **Functions** |
|----|----|
| **API Version** | lustro_api_version() |
| **LustroHashPy** | hash256(message), hash128(message), hash256_many(messages), hash128_many(messages) |
| **LustroPrngPy** | new(seed, stream_id), next_u64(), next_u128(), next_block(), fill(size), fill_into(buf), clone_rng(), fork(id), export_snapshot(), import_snapshot(bytes) |
| **LustroPrngBatchPy** | new(seed, stream_ids), new_range(seed, first_stream_id, count), len(), is_empty(), fill_blocks(out), fill_blocks_many(steps, out), fork(ids), fork_range(first), export_snapshot(), import_snapshot(bytes) |
| **LustroXofPy** | new(message), next_u64(), next_u128(), next_block(), fill(size), fill_into(buf), clone_xof(), fork(id), export_snapshot(), import_snapshot(bytes) |
| **LustroXofBatchPy** | new(messages), len(), is_empty(), fill_blocks(out), fill_blocks_many(steps, out), fork(ids), fork_range(first), export_snapshot(), import_snapshot(bytes) |

## Python Bindings — Parameter Types

Every function not listed here takes/returns plain Python scalars (int, bool) with no shape or dtype constraints. NumPy arrays are required only where noted — all must be C-contiguous or the call raises ValueError.

| **Function** | **Parameter** | **Expected type** |
|----|----|----|
| LustroHashPy.hash256/hash128(message) | message | Python bytes, any length |
| LustroHashPy.hash256_many(data) | data | numpy.ndarray, shape (n, msg_len), dtype=uint8 → returns ndarray shape (n, 32), dtype=uint8 |
| LustroHashPy.hash128_many(data) | data | numpy.ndarray, shape (n, msg_len), dtype=uint8 → returns ndarray shape (n, 16), dtype=uint8 |
| LustroPrngPy(seed, stream_id) | seed | Python bytes, exactly 32 bytes (ValueError otherwise) |
|  | stream_id | Python int, 0 ≤ stream_id \< 2¹²⁸ (OverflowError otherwise) |
| LustroPrngPy.fill(size) | size | Python int → returns bytes of that length |
| LustroPrngPy.fill_into(buf) | buf | Python bytearray, filled in place to len(buf) |
| LustroPrngPy.fork(id) | id | Python int, 0 ≤ id \< 2¹²⁸ (OverflowError otherwise) |
| LustroPrngPy.export_snapshot() | — | returns bytes, exactly 56 bytes |
| LustroPrngPy.import_snapshot(bytes) | bytes | Python bytes, exactly 56 bytes (staticmethod) |
| LustroPrngBatchPy.new(seed, stream_ids) | stream_ids | Python list\[int\] (staticmethod) |
| LustroPrngBatchPy.new_range(seed, first_stream_id, count) | first_stream_id, count | Python int, Python int (staticmethod) |
| LustroPrngBatchPy.fill_blocks(out) | out | numpy.ndarray, shape (n, 4), dtype=uint64, n == batch.len() |
| LustroPrngBatchPy.fill_blocks_many(steps, out) | out | numpy.ndarray, shape (n, steps, 4), dtype=uint64 |
| LustroPrngBatchPy.fork(ids) | ids | Python list\[int\], len(ids) == batch.len() |
| LustroXofPy(message) | message | Python bytes, any length (including empty) |
| LustroXofBatchPy.new(messages) | messages | Python list\[bytes\] — NOT numpy; each element independently sized (staticmethod) |

## Python Bindings — Behavioral Notes

**1. next_u128() returns a Python int —** same underlying little-endian byte stream as fill()/fill_into().

**2. next_block() always advances by exactly one engine round —** returns exactly 32 bytes.

**3. fill(size)/fill_into(buf) have the same concatenation guarantee as Rust's fill_bytes() —** sequential calls are equivalent to one call requesting the concatenated length, as long as no other stream-consuming call is interleaved. This applies to fill()/fill_into() directly; the batch-level fill_blocks_many() analogue reorders output to stream-major layout instead (see C FFI Behavioral Note 3).

**4. export_snapshot()/import_snapshot(bytes) resume exactly —** same guarantee as Rust; import_snapshot(bytes) raises ValueError on malformed input (wrong length, unsupported version, or kind mismatch — e.g. a PRNG snapshot passed to LustroXofPy).

**5. fork(id) / batch fork(ids) always start the child at step=0 —** same behavior as the Rust API — does not inherit the parent's step counter.

**6. hash128() is the truncation of hash256() —** same guarantee as the Rust API — LustroHashPy.hash128(m) always equals the first 16 bytes of LustroHashPy.hash256(m).

**7. All computationally significant calls** (hash256/128, hash256_many/hash128_many, PRNG/XOF fill/fill_blocks/fill_blocks_many) **release the GIL** for the duration of the underlying Rust computation (py.allow_threads) — other Python threads can run concurrently while a call is in flight.

**Minimal Usage Examples**

> \# Hash
>
> h = LustroHashPy()
>
> digest = h.hash256(b"hello world")
>
> \# PRNG
>
> rng = LustroPrngPy(seed, 0) \# seed: exactly 32 bytes
>
> x = rng.next_u64()
>
> \# PRNG snapshot roundtrip
>
> snap = rng.export_snapshot() \# 56 bytes
>
> restored = LustroPrngPy.import_snapshot(snap)
>
> \# PRNG batch
>
> batch = LustroPrngBatchPy.new_range(seed, 0, 4)
>
> out = np.empty((batch.len(), 4), dtype=np.uint64)
>
> batch.fill_blocks(out)
>
> \# XOF batch (plain list\[bytes\], not numpy)
>
> xof_batch = LustroXofBatchPy.new(\[b"m1", b"m2"\])
>
> out2 = np.empty((xof_batch.len(), 4), dtype=np.uint64)
>
> xof_batch.fill_blocks(out2)

------------------------------------------------------------------------

## **C FFI Bindings**

ABI interface exported via extern "C" functions for non-Rust users, compatible with both C and C++ environments. Error Model - Unified LustroError enum with stable numeric values

<table style="width:98%;">
<colgroup>
<col style="width: 15%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr>
<th><strong>Module</strong></th>
<th><strong>Functions</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>API Version</strong></td>
<td>lustro_api_version()</td>
</tr>
<tr>
<td><strong>HASH</strong></td>
<td>lustro_hash256(data, data_len, out), lustro_hash128(data, data_len, out)</td>
</tr>
<tr>
<td><strong>HASH Batch</strong></td>
<td><p><em>lustro_hash256_many(data_ptr, n, message_len, out_ptr), lustro_hash128_many(data_ptr, n, message_len, out_ptr),</em></p>
<p><em>lustro_hash256_many_var(message_ptrs, n, message_lens, out_ptr),</em></p>
<p><em>lustro_hash128_many_var(message_ptrs, n, message_lens, out_ptr)</em></p></td>
</tr>
<tr>
<td><strong>PRNG</strong></td>
<td>lustro_prng_new(seed, stream_id_hi, stream_id_lo), _free, _clone, _fill(out, out_len), _next_u64, _next_u128, _next_block, _fork(id_hi, id_lo), _export_snapshot(out), _import_snapshot(bytes)</td>
</tr>
<tr>
<td><strong>PRNG Batch</strong></td>
<td>lustro_prng_batch_new(seed, ids_hi, ids_lo, n), _new_range(seed, first_hi, first_lo, count), _free, _len, _fill_blocks(out, out_len), _fill_blocks_many(out, out_len, steps), _fork(ids_hi, ids_lo, n), _fork_range(first_hi, first_lo), _snapshot_size, _export_snapshot(out, out_len), _import_snapshot(bytes, len)</td>
</tr>
<tr>
<td><strong>XOF</strong></td>
<td>lustro_xof_new(message, message_len), _free, _clone, _fill(out, out_len), _next_u64, _next_u128, _next_block, _fork(id_hi, id_lo), _export_snapshot(out), _import_snapshot(bytes)</td>
</tr>
<tr>
<td><strong>XOF Batch</strong></td>
<td>lustro_xof_batch_new(message_ptrs, message_lens, n), _free, _len, _fill_blocks(out, out_len), _fill_blocks_many(out, out_len, steps), _fork(ids_hi, ids_lo, n), _fork_range(first_hi, first_lo), _snapshot_size, _export_snapshot(out, out_len), _import_snapshot(bytes, len)</td>
</tr>
</tbody>
</table>

## C FFI — Behavioral Notes

**1. lustro\_\*\_next_u128 writes 16 raw little-endian bytes —** documented per-function in lustro.h; same underlying stream as \*\_fill.

**2. lustro\_\*\_next_block always performs exactly one engine round and writes exactly 32 bytes —** regardless of cursor position; same semantics as the Rust/Python layers.

**3. lustro\_\*\_fill / \*\_batch_fill_blocks\* carry the same concatenation guarantee —** as the Rust/Python layers, at the byte level, for \*\_fill and \*\_batch_fill_blocks (single-step) only. For \*\_batch_fill_blocks_many, the guarantee holds only after reordering sequential \*\_batch_fill_blocks() output to stream-major layout (see Engine table, dispatch_streams_many) — it is not a byte-for-byte concatenation of successive \*\_batch_fill_blocks() calls.

**4. lustro\_\*\_import_snapshot resumes exactly on success —** same resume guarantee as Rust/Python; returns NULL instead of raising on malformed input (see Return Value Conventions in the C FFI Binding Reference).

**5. lustro\_\*\_fork / \*\_batch_fork always start the child at step=0 —** same behavior as the Rust/Python layers.

**6. lustro_hash128 is the truncation of lustro_hash256 —** same guarantee as the Rust/Python layers; lustro_hash128_many / \_many_var are the truncated counterparts of the 256-bit batch functions, not separately-derived digests.

## **C FFI — Binding Reference**

C FFI Bindings section above with info needed to write a correct binding without reading Rust source: type mapping, error/return conventions, buffer sizing, ownership rules, a minimal working example, and header distribution guidance.

**1. Type Mapping**

| **C Type** | **Rust Origin** | **Notes** |
|----|----|----|
| uint8_t\* | \*const u8 / \*mut u8 | byte buffer, in or out |
| uintptr_t | usize | platform-width; not uint32_t/uint64_t |
| uint64_t | u64 | stream_id_hi/\_lo components |
| int32_t | LustroError (#\[repr(i32)\]) | see Return Value Conventions |
| uint32_t | u32 | lustro_api_version() only |
| opaque pointer | \*mut LustroPrng / \*mut LustroPrngBatch / \*mut LustroXof / \*mut LustroXofBatch | never dereference from C; pass through only |
| const uint8_t\* const\* | &\[&\[u8\]\] (array of message slices) | pointer-to-pointer pattern; used by \*\_many_var(message_ptrs, ...) and \*\_batch_new(message_ptrs, ...) for variable-length message arrays. Paired with a parallel const uintptr_t\* of lengths. |

**2. Calling Convention**

All exported functions are extern "C" — cdecl. Do not bind as stdcall.

**3. Return Value Conventions**

Three categories:

• **LustroError (int32)** — used by all hash\*, \*\_fill, \*\_next\_\*, \*\_export_snapshot functions.

| **Value** | **Name**           | **Meaning**                           |
|-----------|--------------------|---------------------------------------|
| 0         | Ok                 | success                               |
| 1         | InvalidLength      | buffer/length argument invalid        |
| 2         | InvalidPointer     | null or misaligned pointer            |
| 3         | OutputTooSmall     | output buffer smaller than required   |
| 4         | AlreadyFinalised   | context already finalised             |
| 5         | VerificationFailed | verification step failed              |
| 6         | InternalPanic      | internal panic caught at FFI boundary |

• **Pointer-returning functions** (\*\_new, \*\_clone, \*\_fork, \*\_fork_range, \*\_import_snapshot) — NULL return indicates failure; no separate error code is available.

• **Value-returning functions** (\*\_len, \*\_snapshot_size → uintptr_t; lustro_api_version → uint32_t) — value is returned directly, no error path.

• **void-returning functions** (\*\_free) — no return value; safe to call with NULL (no-op).

**4. Required Buffer Sizes**

| **Function family** | **Buffer** | **Size** |
|----|----|----|
| lustro_hash256\* | out | 32 bytes per message |
| lustro_hash128\* | out | 16 bytes per message |
| \*\_next_u128 | out | 16 bytes |
| \*\_next_block | out | 32 bytes |
| \*\_export_snapshot (single-context, PRNG/XOF) | out | 56 bytes, fixed |
| \*\_batch_export_snapshot | out | dynamic — call \*\_batch_snapshot_size(ctx) first, allocate, then export |

Input buffers (not covered above — the table in section 4 lists only out buffers; seed is a required input buffer with its own fixed size):

| **Function family** | **Buffer** | **Size** |
|----|----|----|
| lustro_prng_new / lustro_prng_batch_new / lustro_prng_batch_new_range | seed | 32 bytes, fixed |

**5. Ownership / Lifetime**

| **Handle type** | **Created by** | **Freed by** |
|----|----|----|
| LustroPrng\* | \_new, \_clone, \_fork, \_import_snapshot | lustro_prng_free |
| LustroPrngBatch\* | \_new, \_new_range, \_fork, \_fork_range, \_import_snapshot | lustro_prng_batch_free |
| LustroXof\* | \_new, \_clone, \_fork, \_import_snapshot | lustro_xof_free |
| LustroXofBatch\* | \_new, \_fork, \_fork_range, \_import_snapshot | lustro_xof_batch_free |

\_import_snapshot produces a fully independent context, owned and freed identically to one created via \_new.

**6. Null / Zero-Length Semantics**

n == 0 returns LustroError::Ok without dereferencing any pointer — data_ptr = NULL is valid when n == 0. For n \> 0, a NULL on a required pointer returns InvalidPointer. Applies to all \*\_many / \*\_many_var / batch functions.

**7. Minimal Example**

**C:**

> uint8_t out\[32\];
>
> LustroError err = lustro_hash256(data, data_len, out);
>
> LustroPrng \*ctx = lustro_prng_new(seed, 0, 0);
>
> uint64_t val;
>
> lustro_prng_next_u64(ctx, &val);
>
> lustro_prng_free(ctx);

**Python (ctypes):**

> lib.lustro_hash256(data, ctypes.c_size_t(data_len), out)
>
> ctx = lib.lustro_prng_new(seed, ctypes.c_uint64(0), ctypes.c_uint64(0))
>
> val = ctypes.c_uint64(0)
>
> lib.lustro_prng_next_u64(ctx, ctypes.byref(val))
>
> lib.lustro_prng_free(ctx)

**Full PRNG Lifecycle**

> uint8_t seed\[32\] = { /\* 32 bytes \*/ };
>
> LustroPrng \*ctx = lustro_prng_new(seed, 0, 0);
>
> if (!ctx) { /\* handle allocation/seed failure \*/ }
>
> uint64_t val;
>
> lustro_prng_next_u64(ctx, &val);
>
> uint8_t block\[32\];
>
> lustro_prng_next_block(ctx, block);
>
> uint8_t buf\[128\];
>
> LustroError err = lustro_prng_fill(ctx, buf, sizeof(buf));
>
> if (err != LUSTRO_ERROR_OK) { /\* handle error \*/ }
>
> // snapshot roundtrip
>
> uint8_t snap\[56\];
>
> lustro_prng_export_snapshot(ctx, snap);
>
> LustroPrng \*restored = lustro_prng_import_snapshot(snap);
>
> // fork a child stream
>
> LustroPrng \*child = lustro_prng_fork(ctx, 0, 42);
>
> lustro_prng_free(child);
>
> lustro_prng_free(restored);
>
> lustro_prng_free(ctx);

**8. Header Distribution**

lustro.h is published alongside each release. Do not hand-copy or hand-edit the header between versions — take it from the release matching the linked library version.

lustro.h is generated automatically by build.rs via cbindgen whenever the crate is built with --features ffi. The C FFI module itself only compiles under this feature; Python bindings similarly require --features python.

**9. Thread Safety**

LustroPrng, LustroPrngBatch, LustroXof, and LustroXofBatch hold plain state (u128/u64/u8 fields) with no internal synchronization. All mutating FFI functions operate through &mut \*ctx. A single handle used concurrently from multiple threads without external synchronization is a data race. Safe usage requires either a distinct handle per thread, or caller-side locking around any handle shared across threads.

**Notations:**

**Reference Python ctypes mapping**

This repository's Python wrapper maps input byte buffers to ctypes.c_char_p and writable output buffers to ctypes.create_string_buffer(). Other bindings may choose different but equivalent representations.

**Fork Range Without Explicit Count (Batch)**

lustro_prng_batch_fork_range(ctx, first_hi, first_lo) and lustro_xof_batch_fork_range(ctx, first_hi, first_lo) take no count parameter — they always derive exactly ctx.len() children, with sequential ids starting at first. Equivalent to calling the explicit *_batch_fork variant with ids = [first, first+1, ..., first+len()-1].

**New Range Without Explicit IDs (Batch)**

lustro_prng_batch_new_range(seed, first_hi, first_lo, count) constructs a batch equivalent to calling lustro_prng_batch_new(seed, ids, count) with ids = \[first, first+1, ..., first+count-1\].

------------------------------------------------------------------------

------------------------------------------------------------------------

## **Security Notes**

**1. Seed256 is Copy —** copying a seed duplicates the underlying secret bytes. This library version does not provide secret-memory protection. Future versions may implement Drop.

**2. No automatic zeroization —** Seed256 and internal stream state are not cleared from memory on drop.

**3. No hidden global state —** every PRNG/XOF instance owns its own independent internal state.

**4. Panics never cross the FFI boundary —** all exported C functions convert internal panics into error codes; see the Rust API Error Model table for the resulting signal per panic.

**\*** This guarantee depends on the crate being compiled with unwinding panics (panic = "unwind"). The default release profile sets panic = "abort", under which catch_unwind cannot intercept anything. The C FFI cdylib must be built with the release-ffi profile (or an equivalent panic = "unwind" setting) for internal panics to convert into LustroError::InternalPanic instead of aborting the process.

**5. Misuse is fail-fast —** internal invariant violations are treated as programming errors and may panic in the Rust API.

**6. Clone preserves state —** cloning a PRNG or XOF instance produces an identical output stream.

**7. Fork is deterministic —** reuses the domain-separated construction of new()/absorb — the same parent state and id always derive the same child; different ids diverge.

**8. Fork does not mutate the parent —** the parent stream continues its own sequence unaffected by any number of fork() calls.

**9. Fork ignores cursor position —** two forks with the same id are identical regardless of how many bytes were already consumed from the parent's current output block.

**10. Snapshot kind is checked before version-specific decoding —** a PRNG snapshot cannot be imported as XOF (or vice versa), and a single-stream snapshot cannot be imported as a batch (or vice versa); mismatches return an error rather than silently producing a bad stream.\
\
**Functionality note:**

**rand_core integration (feature = "rand")**

LustroPrng implements both rand_core::RngCore and rand_core::SeedableRng.

SeedableRng::from_seed(), From\<Seed256\> and From\<\[u8; 32\]\> always create **stream 0**. Use LustroPrng::new() directly when a specific StreamId is required.
