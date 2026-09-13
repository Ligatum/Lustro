"""
lustro.dll speed test (ctypes), normalized per engine round.

Pipelines: HASH256_MANY, HASH256_MANY message-length sweep,
HASH256_MANY small-batch/large-message showcase, PRNG_BATCH_FILL_BLOCKS,
PRNG_BATCH_FILL_BLOCKS_MANY, XOF_BATCH_FILL_BLOCKS, XOF_BATCH_FILL_BLOCKS_MANY.

Place this script in the same directory as lustro.dll.
"""

import ctypes
import os
import sys
import time
import multiprocessing
import numpy as np
import gc
import psutil

# =========================================================
# CONFIG
# =========================================================
MIN_TIME = 3.0
MIN_ITERS = 50

BATCH_SIZES = [128, 256, 512, 1024, 1536, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]

HASH_MSG_LEN_BASELINE = 32

HASH_MSG_LENGTHS = [16, 31, 32, 33, 64, 65, 128, 256, 512, 768, 1024, 2048, 4096]

HASH_SWEEP_N = 131072

SHOWCASE_N_LIST = [128, 256, 512, 768, 1024]
SHOWCASE_MSG_LENGTHS = [256, 512, 1024, 2048, 4096]


def hash_rounds_for_len(msg_len: int) -> int:
    """
    evaluate_scalar() calls for one message of msg_len bytes, per
    absorb_with_domain() / finalize_terminator() (api.rs):
      full_blocks = msg_len // 32
      remainder   = msg_len % 32
      remainder == 0 and msg_len > 0 -> rounds = full_blocks
      otherwise                      -> rounds = full_blocks + 1
    """
    full_blocks = msg_len // 32
    remainder = msg_len % 32
    if remainder == 0 and msg_len > 0:
        return full_blocks
    return full_blocks + 1

ROUNDS_PER_PRNG_CALL = 1

STEPS_PER_CALL = 16

CPU_FREQ_GHZ = 4.5

CACHE_L1_MAX = 32 * 1024
CACHE_L2_MAX = 512 * 1024
CACHE_L3_MAX = 16 * 1024 * 1024

HW_THREADS = psutil.cpu_count(logical=True) or 1

DLL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lustro.dll")

gc.disable()

# =========================================================
# UTILS
# =========================================================
def format_size(size_bytes):
    if size_bytes < 1024:
        s = f"{size_bytes} B"
    elif size_bytes < 1024 ** 2:
        s = f"{size_bytes // 1024} KB"
    else:
        s = f"{size_bytes // (1024 ** 2)} MB"

    if size_bytes <= CACHE_L1_MAX:
        label = "[L1]"
    elif size_bytes <= CACHE_L2_MAX:
        label = "[L2]"
    elif size_bytes <= CACHE_L3_MAX:
        label = "[L3]"
    else:
        label = "[RAM]"
    return f"{s}{label}"

def timed_loop(fn):
    for _ in range(20):
        fn()
    times = []
    total_start = time.perf_counter()
    iter_counter = 0
    while True:
        start = time.perf_counter_ns()
        fn()
        end = time.perf_counter_ns()
        times.append((end - start) * 1e-9)
        iter_counter += 1
        if (time.perf_counter() - total_start) > MIN_TIME and iter_counter >= MIN_ITERS:
            break
    return np.array(times)

def summarize(times, n_elements, rounds_per_elem, total_bytes):
    """
    All metrics normalized per engine round (n_elements * rounds_per_elem),
    so ns_per_round / cycles_per_round / rounds_per_sec are directly
    comparable across pipelines. cycles_per_byte / bytes_per_cycle use
    total_bytes instead.
    """
    p50 = float(np.percentile(times, 50))
    p95 = float(np.percentile(times, 95))
    cycles_p50 = p50 * CPU_FREQ_GHZ * 1e9

    rounds_total = n_elements * rounds_per_elem

    return {
        "gbps": total_bytes / p50 / (1024 ** 3),
        "rounds_per_sec": rounds_total / p50,
        "ns_per_round": (p50 * 1e9) / rounds_total,
        "cycles_per_round": cycles_p50 / rounds_total,
        "cycles_per_byte": cycles_p50 / total_bytes,
        "bytes_per_cycle": total_bytes / cycles_p50,
        "p50_ms": p50 * 1000,
        "p95_ms": p95 * 1000,
        "rounds_total": rounds_total,
    }

COL = {
    "pipeline": 12,
    "size": 12,
    "thr": 3,
    "n": 8,
    "rounds": 10,
    "p50": 10,
    "p95": 10,
    "tp": 12,
    "rsec": 14,
    "ns": 10,
    "cy": 8,
    "cyb": 8,
    "bcy": 8,
}

def make_header():
    return (
        f"{'Pipeline':<{COL['pipeline']}} | {'Batch size':<{COL['size']}} | "
        f"{'Thr':<{COL['thr']}} | {'N':<{COL['n']}} | {'Rounds':>{COL['rounds']}} | "
        f"{'p50 (ms)':>{COL['p50']}} | {'p95 (ms)':>{COL['p95']}} | "
        f"{'Throughput':>{COL['tp']}} | {'Rounds/sec':>{COL['rsec']}} | "
        f"{'ns/round':>{COL['ns']}} | {'cy/round':>{COL['cy']}} | "
        f"{'cy/B':>{COL['cyb']}} | {'B/cy':>{COL['bcy']}}"
    )

def print_row(label, threads, n, size_bytes, data):
    tp_str = f"{data['gbps']:.2f} GB/s"
    rs_str = f"{data['rounds_per_sec'] / 1e6:.3f} M/s"
    print(
        f"{label:<{COL['pipeline']}} | {format_size(size_bytes):<{COL['size']}} | "
        f"{threads:<{COL['thr']}} | {n:<{COL['n']}} | {data['rounds_total']:>{COL['rounds']}} | "
        f"{data['p50_ms']:>{COL['p50']}.4f} | {data['p95_ms']:>{COL['p95']}.4f} | "
        f"{tp_str:>{COL['tp']}} | {rs_str:>{COL['rsec']}} | "
        f"{data['ns_per_round']:>{COL['ns']}.2f} | {data['cycles_per_round']:>{COL['cy']}.2f} | "
        f"{data['cycles_per_byte']:>{COL['cyb']}.3f} | {data['bytes_per_cycle']:>{COL['bcy']}.3f}"
    )

# =========================================================
# DLL BINDING — 1:1 z potwierdzonym publicznym API
# (SRC/FFI/mod.rs, hash.rs, prng.rs, xof.rs)
# =========================================================
U8P = ctypes.POINTER(ctypes.c_uint8)
SizeT = ctypes.c_size_t

def load_lib():
    if not os.path.exists(DLL_PATH):
        raise FileNotFoundError(f"not found: {DLL_PATH}")
    lib = ctypes.CDLL(DLL_PATH)

    lib.lustro_api_version.restype = ctypes.c_uint32
    lib.lustro_api_version.argtypes = []

    # NOTE: lustro_dispatcher_init celowo pominiete -- nie istnieje w
    # aktualnym publicznym API (brak w dispatch.rs). Pula Rayon jest
    # inicjalizowana leniwie przy pierwszym rownoleglym dispatchu.

    lib.lustro_hash256_many.restype = ctypes.c_int32
    lib.lustro_hash256_many.argtypes = [U8P, SizeT, SizeT, U8P]

    lib.lustro_prng_batch_new_range.restype = ctypes.c_void_p
    lib.lustro_prng_batch_new_range.argtypes = [U8P, ctypes.c_uint64, ctypes.c_uint64, SizeT]
    lib.lustro_prng_batch_free.restype = None
    lib.lustro_prng_batch_free.argtypes = [ctypes.c_void_p]
    lib.lustro_prng_batch_fill_blocks.restype = ctypes.c_int32
    lib.lustro_prng_batch_fill_blocks.argtypes = [ctypes.c_void_p, U8P, SizeT]
    lib.lustro_prng_batch_fill_blocks_many.restype = ctypes.c_int32
    lib.lustro_prng_batch_fill_blocks_many.argtypes = [ctypes.c_void_p, U8P, SizeT, SizeT]

    lib.lustro_xof_batch_new.restype = ctypes.c_void_p
    lib.lustro_xof_batch_new.argtypes = [ctypes.POINTER(U8P), ctypes.POINTER(SizeT), SizeT]
    lib.lustro_xof_batch_free.restype = None
    lib.lustro_xof_batch_free.argtypes = [ctypes.c_void_p]
    lib.lustro_xof_batch_fill_blocks.restype = ctypes.c_int32
    lib.lustro_xof_batch_fill_blocks.argtypes = [ctypes.c_void_p, U8P, SizeT]
    lib.lustro_xof_batch_fill_blocks_many.restype = ctypes.c_int32
    lib.lustro_xof_batch_fill_blocks_many.argtypes = [ctypes.c_void_p, U8P, SizeT, SizeT]

    return lib

def u8_buf(data: bytes):
    n = len(data)
    return (ctypes.c_uint8 * n).from_buffer_copy(data) if n else (ctypes.c_uint8 * 0)()

# =========================================================
# WORKERS
# =========================================================
def hash_batch_worker(n, msg_len, q):
    lib = load_lib()

    rng = np.random.default_rng(123)
    data = rng.integers(0, 256, size=(n, msg_len), dtype=np.uint8)
    data_flat = np.ascontiguousarray(data).reshape(-1)
    data_ptr = data_flat.ctypes.data_as(U8P)

    out = np.empty(n * 32, dtype=np.uint8)
    out_ptr = out.ctypes.data_as(U8P)

    def call():
        err = lib.lustro_hash256_many(data_ptr, n, msg_len, out_ptr)
        if err != 0:
            raise RuntimeError(f"lustro_hash256_many returned error {err}")

    times = timed_loop(call)
    total_bytes = n * msg_len
    result = summarize(times, n, hash_rounds_for_len(msg_len), total_bytes)
    q.put({"threads": HW_THREADS, "result": result, "size_bytes": total_bytes})

def prng_batch_worker(n, q):
    try:
        lib = load_lib()

        seed = u8_buf(bytes(range(32)))
        batch_ctx = lib.lustro_prng_batch_new_range(seed, 0, 0, n)
        if not batch_ctx:
            raise RuntimeError("lustro_prng_batch_new_range returned NULL")

        try:
            out = np.empty(n * 32, dtype=np.uint8)
            out_ptr = out.ctypes.data_as(U8P)
            out_len = n * 32

            def call():
                err = lib.lustro_prng_batch_fill_blocks(batch_ctx, out_ptr, out_len)
                if err != 0:
                    raise RuntimeError(f"lustro_prng_batch_fill_blocks returned error {err}")

            times = timed_loop(call)
            total_bytes = n * 32
            result = summarize(times, n, ROUNDS_PER_PRNG_CALL, total_bytes)
            q.put({"threads": HW_THREADS, "result": result, "size_bytes": total_bytes})
        finally:
            lib.lustro_prng_batch_free(batch_ctx)
    except Exception as e:
        q.put({"error": repr(e)})

def prng_many_batch_worker(n, q):
    """
    Same batch as prng_batch_worker, but each DLL call advances
    STEPS_PER_CALL rounds per stream instead of 1 -- one pool.install()
    amortized over STEPS_PER_CALL rounds instead of one per round.
    """
    try:
        lib = load_lib()

        seed = u8_buf(bytes(range(32)))
        batch_ctx = lib.lustro_prng_batch_new_range(seed, 0, 0, n)
        if not batch_ctx:
            raise RuntimeError("lustro_prng_batch_new_range returned NULL")

        try:
            out_len = n * STEPS_PER_CALL * 32
            out = np.empty(out_len, dtype=np.uint8)
            out_ptr = out.ctypes.data_as(U8P)

            def call():
                err = lib.lustro_prng_batch_fill_blocks_many(
                    batch_ctx, out_ptr, out_len, STEPS_PER_CALL
                )
                if err != 0:
                    raise RuntimeError(f"lustro_prng_batch_fill_blocks_many returned error {err}")

            times = timed_loop(call)
            total_bytes = n * STEPS_PER_CALL * 32
            result = summarize(times, n, STEPS_PER_CALL, total_bytes)
            q.put({"threads": HW_THREADS, "result": result, "size_bytes": total_bytes})
        finally:
            lib.lustro_prng_batch_free(batch_ctx)
    except Exception as e:
        q.put({"error": repr(e)})

def _make_xof_batch(lib, n):
    messages = [f"m{i}".encode() for i in range(n)]
    bufs = [u8_buf(m) for m in messages]  # musza zyc do konca lustro_xof_batch_new
    ptr_array = (U8P * n)(*[ctypes.cast(b, U8P) for b in bufs])
    len_array = (SizeT * n)(*[len(m) for m in messages])
    ctx = lib.lustro_xof_batch_new(ptr_array, len_array, n)
    if not ctx:
        raise RuntimeError("lustro_xof_batch_new returned NULL")
    return ctx

def xof_batch_fill_blocks_worker(n, q):
    try:
        lib = load_lib()

        batch_ctx = _make_xof_batch(lib, n)
        try:
            out = np.empty(n * 32, dtype=np.uint8)
            out_ptr = out.ctypes.data_as(U8P)
            out_len = n * 32

            def call():
                err = lib.lustro_xof_batch_fill_blocks(batch_ctx, out_ptr, out_len)
                if err != 0:
                    raise RuntimeError(f"lustro_xof_batch_fill_blocks returned error {err}")

            times = timed_loop(call)
            total_bytes = n * 32
            result = summarize(times, n, ROUNDS_PER_PRNG_CALL, total_bytes)
            q.put({"threads": HW_THREADS, "result": result, "size_bytes": total_bytes})
        finally:
            lib.lustro_xof_batch_free(batch_ctx)
    except Exception as e:
        q.put({"error": repr(e)})

def xof_many_batch_worker(n, q):
    try:
        lib = load_lib()

        batch_ctx = _make_xof_batch(lib, n)
        try:
            out_len = n * STEPS_PER_CALL * 32
            out = np.empty(out_len, dtype=np.uint8)
            out_ptr = out.ctypes.data_as(U8P)

            def call():
                err = lib.lustro_xof_batch_fill_blocks_many(
                    batch_ctx, out_ptr, out_len, STEPS_PER_CALL
                )
                if err != 0:
                    raise RuntimeError(f"lustro_xof_batch_fill_blocks_many returned error {err}")

            times = timed_loop(call)
            total_bytes = n * STEPS_PER_CALL * 32
            result = summarize(times, n, STEPS_PER_CALL, total_bytes)
            q.put({"threads": HW_THREADS, "result": result, "size_bytes": total_bytes})
        finally:
            lib.lustro_xof_batch_free(batch_ctx)
    except Exception as e:
        q.put({"error": repr(e)})

def run_worker(func, args):
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=func, args=(*args, q))
    p.start()
    res = q.get()
    p.join()
    if "error" in res:
        raise RuntimeError(f"worker {func.__name__} returned error: {res['error']}")
    return res

# =========================================================
# MAIN
# =========================================================
def main():
    WIDTH = 171

    if not os.path.exists(DLL_PATH):
        print(f"ERROR: not found: {DLL_PATH}")
        sys.exit(1)

    hdr = make_header()

    print("=" * WIDTH)
    print(f"{'LUSTRO.DLL — BATCH SPEED TEST (normalized per round)':^{WIDTH}}")
    print(f"{'DLL: ' + DLL_PATH:^{WIDTH}}")
    print(f"{'HW logical threads: ' + str(HW_THREADS):^{WIDTH}}")
    print("=" * WIDTH)

    print(
        f"\n{'HASH256_MANY  (' + str(hash_rounds_for_len(HASH_MSG_LEN_BASELINE)) + ' round / message, msg_len=' + str(HASH_MSG_LEN_BASELINE) + ')':^{WIDTH}}")
    print(hdr)
    print("-" * WIDTH)
    for n in BATCH_SIZES:
        res = run_worker(hash_batch_worker, (n, HASH_MSG_LEN_BASELINE))
        print_row("HASH", res["threads"], n, res["size_bytes"], res["result"])

    print(
        f"\n{'HASH256_MANY -- SMALL BATCH, LARGER MESSAGES (byte-threshold showcase)':^{WIDTH}}")
    print(hdr)
    print("-" * WIDTH)
    for n in SHOWCASE_N_LIST:
        for msg_len in SHOWCASE_MSG_LENGTHS:
            res = run_worker(hash_batch_worker, (n, msg_len))
            print_row(f"HASH_L{msg_len}", res["threads"], n, res["size_bytes"], res["result"])

    print(
        f"\n{'HASH256_MANY — MSG LENGTH SWEEP (N=' + str(HASH_SWEEP_N) + ' fixed; N column below = msg_len)':^{WIDTH}}")
    print(hdr)
    print("-" * WIDTH)
    for msg_len in HASH_MSG_LENGTHS:
        res = run_worker(hash_batch_worker, (HASH_SWEEP_N, msg_len))
        print_row(f"HASH_L{msg_len}", res["threads"], msg_len, res["size_bytes"], res["result"])

    print(f"\n{'PRNG_BATCH_FILL_BLOCKS  (' + str(ROUNDS_PER_PRNG_CALL) + ' round / stream / call)':^{WIDTH}}")
    print(hdr)
    print("-" * WIDTH)
    for n in BATCH_SIZES:
        res = run_worker(prng_batch_worker, (n,))
        print_row("PRNG", res["threads"], n, res["size_bytes"], res["result"])

    print(f"\n{'PRNG_BATCH_FILL_BLOCKS_MANY  (' + str(STEPS_PER_CALL) + ' rounds / stream / call)':^{WIDTH}}")
    print(hdr)
    print("-" * WIDTH)
    for n in BATCH_SIZES:
        res = run_worker(prng_many_batch_worker, (n,))
        print_row("PRNG_MANY", res["threads"], n, res["size_bytes"], res["result"])

    print(
        f"\n{'XOF_BATCH_FILL_BLOCKS  (' + str(ROUNDS_PER_PRNG_CALL) + ' round / stream / call, same dispatch_streams as PRNG_BATCH)':^{WIDTH}}")
    print(hdr)
    print("-" * WIDTH)
    for n in BATCH_SIZES:
        res = run_worker(xof_batch_fill_blocks_worker, (n,))
        print_row("XOF", res["threads"], n, res["size_bytes"], res["result"])

    print(f"\n{'XOF_BATCH_FILL_BLOCKS_MANY  (' + str(STEPS_PER_CALL) + ' rounds / stream / call)':^{WIDTH}}")
    print(hdr)
    print("-" * WIDTH)
    for n in BATCH_SIZES:
        res = run_worker(xof_many_batch_worker, (n,))
        print_row("XOF_MANY", res["threads"], n, res["size_bytes"], res["result"])

    print("\n" + "=" * WIDTH)
    print(
        "All ns/round and cy/round figures are comparable across every table\n"
        "above (normalized per engine round, not per element).\n"
        "The difference between *_FILL_BLOCKS and *_FILL_BLOCKS_MANY ns/round at\n"
        "the same N is the cost of a single DLL/Rayon entry (ctypes marshalling +\n"
        "pool.install()), amortized in the MANY variant over " + str(STEPS_PER_CALL) + " rounds\n"
        "instead of 1."
    )
    print("=" * WIDTH)

if __name__ == "__main__":
    multiprocessing.set_start_method("spawn", force=True)
    main()