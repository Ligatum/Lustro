"""
================================================================
LUSTRO V1 API — GOLDEN VECTOR VALIDATOR (FFI + Python)
================================================================
Validates lustro.dll in the same directory as this script.
================================================================
"""

import ctypes
import hashlib
import importlib.machinery
import importlib.util
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DLL_PATH = os.path.join(SCRIPT_DIR, "lustro.dll")

# ================================================================
# GOLDEN VECTORS
# ================================================================

HASH_VECTORS = [
    ("empty", b'', "b517c9080d7fe75a2d5d946f83f963669d1496992081a9a099fcdf652e209ce6", "b517c9080d7fe75a2d5d946f83f96366"),
    ("len1_zero", b'\x00', "4af67eae6cb5cdf0a45a1885a493b52545ab58f99ee3f265d55ae3c983f07c4d", "4af67eae6cb5cdf0a45a1885a493b525"),
    ("len31_zero", b'\x00' * 31, "27a4f04d79de8509c8948e8b00260f98ad1f80eb9ef5e165f8ee095d3b679eea", "27a4f04d79de8509c8948e8b00260f98"),
    ("len32_zero", b'\x00' * 32, "842c078ce4c609fc2d9d1a1d37b12ecc9d6a41776b6929a85b9a45d269e23da9", "842c078ce4c609fc2d9d1a1d37b12ecc"),
    ("len33_zero", b'\x00' * 33, "02f06e3381d2516860f70561db381b9b014b5f748c934e0229c8b3686a008c45", "02f06e3381d2516860f70561db381b9b"),
    ("len63_zero", b'\x00' * 63, "748e004f95619944586748ae9d7001ddea5dde9eadc7ee76ff1975128d121ede", "748e004f95619944586748ae9d7001dd"),
    ("len64_zero", b'\x00' * 64, "b81250dbb1da643d8a2260e6a0a716e405ef50dda2611ca457e6f49589d30ac6", "b81250dbb1da643d8a2260e6a0a716e4"),
    ("len65_zero", b'\x00' * 65, "b97e709e60f31919453f0d5103930a0c78aab7cd1c57bf9f114c43e09c6fcfb2", "b97e709e60f31919453f0d5103930a0c"),
    ("len32_ff", b'\xff' * 32, "898b88ba5569cc47f28cf5618a808eccbafd2d523efe9b573438e7c2bdaa2af9", "898b88ba5569cc47f28cf5618a808ecc"),
    ("len32_ascending", bytes(range(32)), "a1dfb31c10cd28712a98eb5122926f55a117f776be90d77460ca3e0e09738e79", "a1dfb31c10cd28712a98eb5122926f55"),
    ("len64_ascending", bytes(range(32)) + bytes([32 + i for i in range(32)]), "c5d10d1b3871e5172c181a6fdde2a425018c40cd7f8e17c403e918e90756b003", "c5d10d1b3871e5172c181a6fdde2a425"),
]

PRNG_VECTORS = [
    ("seed_zero_stream0_32", b'\x00' * 32, 0, 32, "6ee8ec19b51f03056a5705675d962c17f39602cbe60099ff69bacc7e1a997869"),
    ("seed_zero_stream0_64", b'\x00' * 32, 0, 64, "6ee8ec19b51f03056a5705675d962c17f39602cbe60099ff69bacc7e1a997869b08750b478760d28c813362b7fe77e0971e2451154decda83360c93b61d30b86"),
    ("seed_ff_stream1_32", b'\xff' * 32, 1, 32, "d94a37c25905fa92182b72c091dfd927e9ba28d4b5388043017067689b44f4c6"),
    ("seed_ascending_bigid", bytes(range(32)), 1267650600228229401496703205376, 32, "2e3a743027f5579c7af3d17e7b482c203ecb1b0f85c00dfc32b55c331e0eedf3"),
]

GOLDEN_FINGERPRINT = "e5094cadc17043f4bf30bd66c80d22f0aa36fe6484154ef12950425d8b8016f2"

XOF_VECTORS = [
    ("empty", b'', 32, "02ad43fd65980f38f1b7534a64021590f6c8ba17d4221ae80aa96270dc6d94a4"),
    ("len1_zero", b'\x00', 32, "e3910ae86648e8065edc228f173678111a14107e4fab23b8a1c5c07c57c7304f"),
    ("len31_zero", b'\x00' * 31, 32, "1274c3bdb904b3cdef46fbbecf9d9378e3641b38d29de36c54efb1896a6ddb78"),
    ("len32_zero", b'\x00' * 32, 32, "6b0d927254ba9817d5ff2ce7d2e8217904a84e42fb0d7860c307c2bb5cedf52a"),
    ("len32_zero_fill64", b'\x00' * 32, 64, "6b0d927254ba9817d5ff2ce7d2e8217904a84e42fb0d7860c307c2bb5cedf52acd5d20925eb81f6e8ff14059d7b2dd8d916f7487971b3abfeeff94acff569caa"),
    ("len33_zero", b'\x00' * 33, 32, "1ec0aa786e1e4be1029bd1ddd54c641ae3174625532b7afec557b2ba7a4e1188"),
    ("len63_zero", b'\x00' * 63, 32, "00129b4a7d25693b76b9ca3efae5d243a476c47a8c216a2735ab0b1871a02272"),
    ("len64_zero", b'\x00' * 64, 32, "8cfade886a41bae4495e88f385c916879bae62c3dc4389fce4bb02c02d50707d"),
    ("len65_zero", b'\x00' * 65, 32, "4c0f92d962f0110402d76a0ffc535a23e51edfe0755f20400889634e03be2854"),
    ("len32_ff", b'\xff' * 32, 32, "3c452b55bf3d2d9edb272126e6f1326ca219153aa28f68984d7927e09fd2a286"),
    ("len32_ascending", bytes(range(32)), 32, "0c7591015f04ef0cf61c6b0f32d4f78e85e1d149275995820bef8129993e468b"),
    ("len64_ascending", bytes(range(32)) + bytes([32 + i for i in range(32)]), 32, "8d99025b2ca5001a7bae78306e65c996fbca798372e0fd18e9e93b7deaea5a49"),
]

GOLDEN_FINGERPRINT = "fed255a3feb481e86992223866d08312b77f9c0b652056a8ccbb7466fa8aa50b"

# ================================================================
# TEST HARNESS
# ================================================================
FAILURES = []


def check(label, condition, detail=""):
    status = "PASS" if condition else "FAIL"
    print(f"  [{status}] {label}" + (f" — {detail}" if detail and not condition else ""))
    if not condition:
        FAILURES.append(label)


def validate_layer(layer_name, hash256_fn, hash128_fn, prng_fill_fn, xof_fill_fn):
    sha = hashlib.sha256()

    print(f"\n== {layer_name}: HASH VECTORS ==")
    for label, msg, exp256, exp128 in HASH_VECTORS:
        got256 = hash256_fn(msg)
        got128 = hash128_fn(msg)
        sha.update(got256)
        sha.update(got128)
        check(f"{layer_name} hash256 [{label}]", got256.hex() == exp256,
              f"expected={exp256} got={got256.hex()}")
        check(f"{layer_name} hash128 [{label}]", got128.hex() == exp128,
              f"expected={exp128} got={got128.hex()}")

    print(f"\n== {layer_name}: PRNG VECTORS ==")
    for label, seed, stream_id, fill_len, exp in PRNG_VECTORS:
        got = prng_fill_fn(seed, stream_id, fill_len)
        sha.update(got)
        check(f"{layer_name} prng [{label}]", got.hex() == exp,
              f"expected={exp} got={got.hex()}")

    print(f"\n== {layer_name}: XOF VECTORS ==")
    for label, message, fill_len, exp in XOF_VECTORS:
        got = xof_fill_fn(message, fill_len)
        sha.update(got)
        check(f"{layer_name} xof [{label}]", got.hex() == exp,
              f"expected={exp} got={got.hex()}")

    fingerprint = sha.hexdigest()
    check(f"{layer_name} fingerprint", fingerprint == GOLDEN_FINGERPRINT,
          f"expected={GOLDEN_FINGERPRINT} got={fingerprint}")


# ================================================================
# FFI LAYER
# ================================================================
def try_load_ffi():
    if not os.path.exists(DLL_PATH):
        print(f"\n[FFI] skipped — {DLL_PATH} not found")
        return None
    try:
        lib = ctypes.CDLL(DLL_PATH)

        lib.lustro_hash256.restype = ctypes.c_int32
        lib.lustro_hash256.argtypes = [ctypes.c_char_p, ctypes.c_size_t, ctypes.POINTER(ctypes.c_uint8)]

        lib.lustro_hash128.restype = ctypes.c_int32
        lib.lustro_hash128.argtypes = [ctypes.c_char_p, ctypes.c_size_t, ctypes.POINTER(ctypes.c_uint8)]

        lib.lustro_prng_new.restype = ctypes.c_void_p
        lib.lustro_prng_new.argtypes = [ctypes.c_char_p, ctypes.c_uint64, ctypes.c_uint64]

        lib.lustro_prng_free.restype = None
        lib.lustro_prng_free.argtypes = [ctypes.c_void_p]

        lib.lustro_prng_fill.restype = ctypes.c_int32
        lib.lustro_prng_fill.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint8), ctypes.c_size_t]

        lib.lustro_xof_new.restype = ctypes.c_void_p
        lib.lustro_xof_new.argtypes = [ctypes.c_char_p, ctypes.c_size_t]

        lib.lustro_xof_free.restype = None
        lib.lustro_xof_free.argtypes = [ctypes.c_void_p]

        lib.lustro_xof_fill.restype = ctypes.c_int32
        lib.lustro_xof_fill.argtypes = [ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint8), ctypes.c_size_t]

    except (OSError, AttributeError) as e:
        print(f"\n[FFI] skipped — {DLL_PATH} does not export the lustro_* FFI symbols ({e})")
        return None

    def hash256_fn(msg: bytes) -> bytes:
        out = (ctypes.c_uint8 * 32)()
        err = lib.lustro_hash256(msg, len(msg), out)
        if err != 0:
            raise RuntimeError(f"lustro_hash256 returned error {err}")
        return bytes(out)

    def hash128_fn(msg: bytes) -> bytes:
        out = (ctypes.c_uint8 * 16)()
        err = lib.lustro_hash128(msg, len(msg), out)
        if err != 0:
            raise RuntimeError(f"lustro_hash128 returned error {err}")
        return bytes(out)

    def prng_fill_fn(seed: bytes, stream_id: int, fill_len: int) -> bytes:
        stream_hi = (stream_id >> 64) & 0xFFFFFFFFFFFFFFFF
        stream_lo = stream_id & 0xFFFFFFFFFFFFFFFF
        ctx = lib.lustro_prng_new(seed, stream_hi, stream_lo)
        if not ctx:
            raise RuntimeError("lustro_prng_new returned NULL")
        out = (ctypes.c_uint8 * fill_len)()
        err = lib.lustro_prng_fill(ctx, out, fill_len)
        lib.lustro_prng_free(ctx)
        if err != 0:
            raise RuntimeError(f"lustro_prng_fill returned error {err}")
        return bytes(out)

    def xof_fill_fn(message: bytes, fill_len: int) -> bytes:
        ctx = lib.lustro_xof_new(message, len(message))
        if not ctx:
            raise RuntimeError("lustro_xof_new returned NULL")
        out = (ctypes.c_uint8 * fill_len)()
        err = lib.lustro_xof_fill(ctx, out, fill_len)
        lib.lustro_xof_free(ctx)
        if err != 0:
            raise RuntimeError(f"lustro_xof_fill returned error {err}")
        return bytes(out)

    return hash256_fn, hash128_fn, prng_fill_fn, xof_fill_fn


# ================================================================
# PYTHON LAYER
# ================================================================
def try_load_python_dll():
    if not os.path.exists(DLL_PATH):
        print(f"\n[Python] skipped — {DLL_PATH} not found")
        return None
    try:
        loader = importlib.machinery.ExtensionFileLoader("lustro", DLL_PATH)
        spec = importlib.util.spec_from_file_location("lustro", DLL_PATH, loader=loader)
        module = importlib.util.module_from_spec(spec)
        loader.exec_module(module)
    except Exception as e:
        print(f"\n[Python] skipped — {DLL_PATH} does not export a Python module init function ({e})")
        return None

    h = module.LustroHashPy()

    def hash256_fn(msg: bytes) -> bytes:
        return h.hash256(msg)

    def hash128_fn(msg: bytes) -> bytes:
        return h.hash128(msg)

    def prng_fill_fn(seed: bytes, stream_id: int, fill_len: int) -> bytes:
        p = module.LustroPrngPy(seed, stream_id)
        return p.fill(fill_len)

    def xof_fill_fn(message: bytes, fill_len: int) -> bytes:
        x = module.LustroXofPy(message)
        return x.fill(fill_len)

    return hash256_fn, hash128_fn, prng_fill_fn, xof_fill_fn


# ================================================================
# MAIN
# ================================================================
def main():
    width = 72
    print("=" * width)
    print(f"{'LUSTRO V1 — GOLDEN VECTOR VALIDATOR':^{width}}")
    print(f"{'directory: ' + SCRIPT_DIR:^{width}}")
    print("=" * width)

    layers = {
        "FFI": try_load_ffi(),
        "Python": try_load_python_dll(),
    }

    active = {name: fns for name, fns in layers.items() if fns is not None}

    if not active:
        sys.exit("\nERROR: no layer is available for validation.")

    for name, (hash256_fn, hash128_fn, prng_fill_fn, xof_fill_fn) in active.items():
        validate_layer(name, hash256_fn, hash128_fn, prng_fill_fn, xof_fill_fn)

    print("\n" + "=" * width)
    if FAILURES:
        print(f"RESULT: {len(FAILURES)} test(s) FAILED:")
        for f in FAILURES:
            print(f"  - {f}")
        sys.exit(1)
    else:
        print(f"RESULT: All tests passed. File is a binary match ({', '.join(active.keys())}).")
    print("=" * width)


if __name__ == "__main__":
    main()