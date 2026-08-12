```text
-------------------------------------------------------------------------------
--- Testing lustro "Lustro Engine V1 256-bit" GOOD

[[[ Sanity Tests ]]]

Verification value 0xE5D9D866 ....... SKIP (self- or unseeded)
Running sanity check 1       .......... PASS
Running AppendedZeroesTest .......... PASS

[[[ Speed Tests ]]]

Bulk speed test - 262144-byte keys
Alignment  7 -  0.410 bytes/cycle - 1535.86 MiB/sec @ 3924 MHz
Alignment  6 -  0.410 bytes/cycle - 1535.87 MiB/sec @ 3924 MHz
Alignment  5 -  0.410 bytes/cycle - 1535.86 MiB/sec @ 3924 MHz
Alignment  4 -  0.410 bytes/cycle - 1535.88 MiB/sec @ 3924 MHz
Alignment  3 -  0.410 bytes/cycle - 1535.85 MiB/sec @ 3924 MHz
Alignment  2 -  0.410 bytes/cycle - 1535.87 MiB/sec @ 3924 MHz
Alignment  1 -  0.410 bytes/cycle - 1535.87 MiB/sec @ 3924 MHz
Alignment  0 -  0.410 bytes/cycle - 1535.86 MiB/sec @ 3924 MHz
Average      -  0.410 bytes/cycle - 1535.87 MiB/sec @ 3924 MHz

Small key speed test -    1-byte keys -   106.00 cycles/hash
Small key speed test -    2-byte keys -   106.00 cycles/hash
Small key speed test -    3-byte keys -   107.87 cycles/hash
Small key speed test -    4-byte keys -   106.00 cycles/hash
Small key speed test -    5-byte keys -   107.97 cycles/hash
Small key speed test -    6-byte keys -   107.92 cycles/hash
Small key speed test -    7-byte keys -   108.50 cycles/hash
Small key speed test -    8-byte keys -   106.00 cycles/hash
Small key speed test -    9-byte keys -   108.91 cycles/hash
Small key speed test -   10-byte keys -   107.83 cycles/hash
Small key speed test -   11-byte keys -   108.68 cycles/hash
Small key speed test -   12-byte keys -   108.12 cycles/hash
Small key speed test -   13-byte keys -   108.67 cycles/hash
Small key speed test -   14-byte keys -   108.73 cycles/hash
Small key speed test -   15-byte keys -   109.29 cycles/hash
Small key speed test -   16-byte keys -   107.13 cycles/hash
Small key speed test -   17-byte keys -   107.96 cycles/hash
Small key speed test -   18-byte keys -   107.95 cycles/hash
Small key speed test -   19-byte keys -   107.95 cycles/hash
Small key speed test -   20-byte keys -   107.96 cycles/hash
Small key speed test -   21-byte keys -   108.30 cycles/hash
Small key speed test -   22-byte keys -   108.29 cycles/hash
Small key speed test -   23-byte keys -   108.37 cycles/hash
Small key speed test -   24-byte keys -   189.26 cycles/hash
Small key speed test -   25-byte keys -   189.68 cycles/hash
Small key speed test -   26-byte keys -   188.69 cycles/hash
Small key speed test -   27-byte keys -   188.81 cycles/hash
Small key speed test -   28-byte keys -   189.49 cycles/hash
Small key speed test -   29-byte keys -   189.09 cycles/hash
Small key speed test -   30-byte keys -   189.41 cycles/hash
Small key speed test -   31-byte keys -   189.74 cycles/hash
Small key speed test -   32-byte keys -   182.55 cycles/hash
Average                                   130.535 cycles/hash
Average, weighted by key length freq.     118.457 cycles/hash (using 93.0% of top-7m Tranco DNS names dataset)
Average, weighted by key length freq.     108.528 cycles/hash (using 27.1% of startup-1M UMASH trace dataset)

[[[ 'Hashmap' Speed Tests ]]]

Unable to open words dict file /usr/share/dict/words

[[[ Avalanche Tests ]]]

Testing   24-bit keys -> 256-bit hashes, 300000 reps.......... worst bias is 0.668000%
Testing   32-bit keys -> 256-bit hashes, 300000 reps.......... worst bias is 0.695333%
Testing   40-bit keys -> 256-bit hashes, 300000 reps.......... worst bias is 0.748000%
Testing   48-bit keys -> 256-bit hashes, 300000 reps.......... worst bias is 0.712000%
Testing   56-bit keys -> 256-bit hashes, 300000 reps.......... worst bias is 0.766667%
Testing   64-bit keys -> 256-bit hashes, 300000 reps.......... worst bias is 0.842667%
Testing   72-bit keys -> 256-bit hashes, 300000 reps.......... worst bias is 0.723333%
Testing   80-bit keys -> 256-bit hashes, 300000 reps.......... worst bias is 0.709333%
Testing   96-bit keys -> 256-bit hashes, 300000 reps.......... worst bias is 0.760000%
Testing  112-bit keys -> 256-bit hashes, 300000 reps.......... worst bias is 0.731333%
Testing  128-bit keys -> 256-bit hashes, 300000 reps.......... worst bias is 0.875333%
Testing  160-bit keys -> 256-bit hashes, 300000 reps.......... worst bias is 0.802000%

[[[ Keyset 'Sparse' Tests ]]]

Keyset 'Sparse' - 16-bit keys with up to 9 bits set - 50643 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected          0.3, actual      0 (0.00x)
Testing collisions (high 19-25 bits) - Worst is 20 bits: 1221/1203 (1.01x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected          0.3, actual      0 (0.00x)
Testing collisions (low  19-25 bits) - Worst is 22 bits: 306/304 (1.00x)
Testing distribution - Worst bias is the 13-bit window at bit 243 - 0.703%

Keyset 'Sparse' - 24-bit keys with up to 8 bits set - 1271626 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        188.2, actual    183 (0.97x)
Testing collisions (high 24-35 bits) - Worst is 34 bits: 60/47 (1.27x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        188.2, actual    181 (0.96x)
Testing collisions (low  24-35 bits) - Worst is 35 bits: 32/23 (1.36x)
Testing distribution - Worst bias is the 17-bit window at bit 103 - 0.098%

Keyset 'Sparse' - 32-bit keys with up to 7 bits set - 4514873 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected       2372.2, actual   2379 (1.00x) (7)
Testing collisions (high 25-38 bits) - Worst is 31 bits: 4780/4742 (1.01x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected       2372.2, actual   2325 (0.98x) (-47)
Testing collisions (low  25-38 bits) - Worst is 35 bits: 316/296 (1.07x)
Testing distribution - Worst bias is the 19-bit window at bit 56 - 0.067%

Keyset 'Sparse' - 40-bit keys with up to 6 bits set - 4598479 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected       2460.8, actual   2474 (1.01x) (14)
Testing collisions (high 25-38 bits) - Worst is 37 bits: 81/76 (1.05x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected       2460.8, actual   2464 (1.00x) (4)
Testing collisions (low  25-38 bits) - Worst is 38 bits: 49/38 (1.27x)
Testing distribution - Worst bias is the 19-bit window at bit 22 - 0.064%

Keyset 'Sparse' - 48-bit keys with up to 6 bits set - 14196869 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected      23437.8, actual  23503 (1.00x) (66)
Testing collisions (high 27-42 bits) - Worst is 41 bits: 61/45 (1.33x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected      23437.8, actual  23311 (0.99x) (-126)
Testing collisions (low  27-42 bits) - Worst is 28 bits: 369430/368886 (1.00x)
Testing distribution - Worst bias is the 20-bit window at bit 244 - 0.028%

Keyset 'Sparse' - 56-bit keys with up to 5 bits set - 4216423 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected       2069.0, actual   2055 (0.99x) (-13)
Testing collisions (high 25-38 bits) - Worst is 35 bits: 271/258 (1.05x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected       2069.0, actual   2101 (1.02x) (33)
Testing collisions (low  25-38 bits) - Worst is 32 bits: 2101/2068 (1.02x)
Testing distribution - Worst bias is the 19-bit window at bit 102 - 0.062%

Keyset 'Sparse' - 64-bit keys with up to 5 bits set - 8303633 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected       8021.7, actual   8029 (1.00x) (8)
Testing collisions (high 26-40 bits) - Worst is 36 bits: 526/501 (1.05x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected       8021.7, actual   8075 (1.01x) (54)
Testing collisions (low  26-40 bits) - Worst is 39 bits: 70/62 (1.12x)
Testing distribution - Worst bias is the 20-bit window at bit 177 - 0.041%

Keyset 'Sparse' - 72-bit keys with up to 5 bits set - 15082603 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected      26451.8, actual  26360 (1.00x) (-91)
Testing collisions (high 27-42 bits) - Worst is 42 bits: 28/25 (1.08x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected      26451.8, actual  26427 (1.00x) (-24)
Testing collisions (low  27-42 bits) - Worst is 41 bits: 58/51 (1.12x)
Testing distribution - Worst bias is the 20-bit window at bit 248 - 0.031%

Keyset 'Sparse' - 96-bit keys with up to 4 bits set - 3469497 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected       1401.0, actual   1429 (1.02x) (29)
Testing collisions (high 25-38 bits) - Worst is 38 bits: 26/21 (1.19x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected       1401.0, actual   1397 (1.00x) (-3)
Testing collisions (low  25-38 bits) - Worst is 35 bits: 183/175 (1.04x)
Testing distribution - Worst bias is the 19-bit window at bit 241 - 0.075%

Keyset 'Sparse' - 160-bit keys with up to 4 bits set - 26977161 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected      84546.1, actual  84522 (1.00x) (-24)
Testing collisions (high 28-44 bits) - Worst is 44 bits: 26/20 (1.26x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected      84546.1, actual  85244 (1.01x) (698)
Testing collisions (low  28-44 bits) - Worst is 44 bits: 34/20 (1.64x)
Testing distribution - Worst bias is the 20-bit window at bit 174 - 0.014%

Keyset 'Sparse' - 256-bit keys with up to 3 bits set - 2796417 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        910.2, actual    945 (1.04x) (35)
Testing collisions (high 25-37 bits) - Worst is 37 bits: 35/28 (1.23x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        910.2, actual    929 (1.02x) (19)
Testing collisions (low  25-37 bits) - Worst is 31 bits: 1866/1819 (1.03x)
Testing distribution - Worst bias is the 19-bit window at bit 169 - 0.124%


[[[ Keyset 'Permutation' Tests ]]]

Combination Lowbits Tests:
Keyset 'Combination' - up to 7 blocks from a set of 8 - 2396744 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        668.6, actual    632 (0.95x)
Testing collisions (high 24-37 bits) - Worst is 37 bits: 25/20 (1.20x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        668.6, actual    660 (0.99x) (-8)
Testing collisions (low  24-37 bits) - Worst is 29 bits: 5418/5341 (1.01x)
Testing distribution - Worst bias is the 18-bit window at bit  6 - 0.070%


Combination Highbits Tests
Keyset 'Combination' - up to 7 blocks from a set of 8 - 2396744 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        668.6, actual    669 (1.00x) (1)
Testing collisions (high 24-37 bits) - Worst is 30 bits: 2696/2672 (1.01x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        668.6, actual    671 (1.00x) (3)
Testing collisions (low  24-37 bits) - Worst is 37 bits: 23/20 (1.10x)
Testing distribution - Worst bias is the 18-bit window at bit 101 - 0.085%


Combination Hi-Lo Tests:
Keyset 'Combination' - up to 6 blocks from a set of 15 - 12204240 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected      17322.9, actual  17383 (1.00x) (61)
Testing collisions (high 27-41 bits) - Worst is 39 bits: 148/135 (1.09x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected      17322.9, actual  17255 (1.00x) (-67)
Testing collisions (low  27-41 bits) - Worst is 39 bits: 143/135 (1.06x)
Testing distribution - Worst bias is the 20-bit window at bit 32 - 0.034%


Combination 0x80000000 Tests:
Keyset 'Combination' - up to 17 blocks from a set of 2 - 262142 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected          8.0, actual     10 (1.25x) (3)
Testing collisions (high 21-30 bits) - Worst is 30 bits: 35/31 (1.09x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected          8.0, actual      7 (0.88x)
Testing collisions (low  21-30 bits) - Worst is 30 bits: 38/31 (1.19x)
Testing distribution - Worst bias is the 15-bit window at bit 160 - 0.235%


Combination 0x00000001 Tests:
Keyset 'Combination' - up to 17 blocks from a set of 2 - 262142 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected          8.0, actual     11 (1.38x) (4)
Testing collisions (high 21-30 bits) - Worst is 28 bits: 130/127 (1.02x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected          8.0, actual     12 (1.50x) (5)
Testing collisions (low  21-30 bits) - Worst is 30 bits: 41/31 (1.28x)
Testing distribution - Worst bias is the 15-bit window at bit 11 - 0.303%


Combination 0x8000000000000000 Tests:
Keyset 'Combination' - up to 17 blocks from a set of 2 - 262142 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected          8.0, actual      6 (0.75x)
Testing collisions (high 21-30 bits) - Worst is 28 bits: 129/127 (1.01x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected          8.0, actual      4 (0.50x)
Testing collisions (low  21-30 bits) - Worst is 24 bits: 2058/2037 (1.01x)
Testing distribution - Worst bias is the 14-bit window at bit 126 - 0.240%


Combination 0x0000000000000001 Tests:
Keyset 'Combination' - up to 17 blocks from a set of 2 - 262142 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected          8.0, actual      6 (0.75x)
Testing collisions (high 21-30 bits) - Worst is 28 bits: 137/127 (1.07x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected          8.0, actual     10 (1.25x) (3)
Testing collisions (low  21-30 bits) - Worst is 30 bits: 35/31 (1.09x)
Testing distribution - Worst bias is the 15-bit window at bit 138 - 0.212%


Combination 16-bytes [0-1] Tests:
Keyset 'Combination' - up to 17 blocks from a set of 2 - 262142 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected          8.0, actual      7 (0.88x)
Testing collisions (high 21-30 bits) - Worst is 22 bits: 8040/8023 (1.00x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected          8.0, actual      5 (0.63x)
Testing collisions (low  21-30 bits) - Worst is 28 bits: 137/127 (1.07x)
Testing distribution - Worst bias is the 15-bit window at bit 142 - 0.351%


Combination 16-bytes [0-last] Tests:
Keyset 'Combination' - up to 17 blocks from a set of 2 - 262142 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected          8.0, actual      4 (0.50x)
Testing collisions (high 21-30 bits) - Worst is 21 bits: 15610/15721 (0.99x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected          8.0, actual      7 (0.88x)
Testing collisions (low  21-30 bits) - Worst is 29 bits: 69/63 (1.08x)
Testing distribution - Worst bias is the 15-bit window at bit 42 - 0.282%


Combination 32-bytes [0-1] Tests:
Keyset 'Combination' - up to 17 blocks from a set of 2 - 262142 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected          8.0, actual      8 (1.00x) (1)
Testing collisions (high 21-30 bits) - Worst is 24 bits: 2100/2037 (1.03x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected          8.0, actual      9 (1.13x) (2)
Testing collisions (low  21-30 bits) - Worst is 30 bits: 33/31 (1.03x)
Testing distribution - Worst bias is the 15-bit window at bit 38 - 0.196%


Combination 32-bytes [0-last] Tests:
Keyset 'Combination' - up to 17 blocks from a set of 2 - 262142 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected          8.0, actual      7 (0.88x)
Testing collisions (high 21-30 bits) - Worst is 27 bits: 288/255 (1.13x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected          8.0, actual      5 (0.63x)
Testing collisions (low  21-30 bits) - Worst is 25 bits: 1082/1021 (1.06x)
Testing distribution - Worst bias is the 15-bit window at bit 109 - 0.262%


Combination 64-bytes [0-1] Tests:
Keyset 'Combination' - up to 17 blocks from a set of 2 - 262142 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected          8.0, actual     15 (1.88x) (8)
Testing collisions (high 21-30 bits) - Worst is 30 bits: 37/31 (1.16x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected          8.0, actual     11 (1.38x) (4)
Testing collisions (low  21-30 bits) - Worst is 30 bits: 39/31 (1.22x)
Testing distribution - Worst bias is the 15-bit window at bit 161 - 0.252%


Combination 64-bytes [0-last] Tests:
Keyset 'Combination' - up to 17 blocks from a set of 2 - 262142 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected          8.0, actual     11 (1.38x) (4)
Testing collisions (high 21-30 bits) - Worst is 24 bits: 2068/2037 (1.02x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected          8.0, actual      7 (0.88x)
Testing collisions (low  21-30 bits) - Worst is 27 bits: 275/255 (1.07x)
Testing distribution - Worst bias is the 15-bit window at bit 214 - 0.251%


Combination 128-bytes [0-1] Tests:
Keyset 'Combination' - up to 17 blocks from a set of 2 - 262142 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected          8.0, actual     11 (1.38x) (4)
Testing collisions (high 21-30 bits) - Worst is 22 bits: 8003/8023 (1.00x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected          8.0, actual      8 (1.00x) (1)
Testing collisions (low  21-30 bits) - Worst is 28 bits: 138/127 (1.08x)
Testing distribution - Worst bias is the 15-bit window at bit 94 - 0.240%


Combination 128-bytes [0-last] Tests:
Keyset 'Combination' - up to 17 blocks from a set of 2 - 262142 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected          8.0, actual      9 (1.13x) (2)
Testing collisions (high 21-30 bits) - Worst is 29 bits: 76/63 (1.19x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected          8.0, actual     11 (1.38x) (4)
Testing collisions (low  21-30 bits) - Worst is 29 bits: 65/63 (1.02x)
Testing distribution - Worst bias is the 15-bit window at bit 91 - 0.281%


[[[ Keyset 'Window' Tests ]]]

Keyset 'Window' -  32-bit key,  25-bit window - 32 tests, 33554432 keys per test
Window at   0 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at   1 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at   2 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at   3 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at   4 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at   5 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at   6 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at   7 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at   8 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at   9 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  10 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  11 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  12 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  13 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  14 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  15 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  16 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  17 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  18 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  19 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  20 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  21 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  22 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  23 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  24 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  25 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  26 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  27 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  28 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  29 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  30 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  31 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Window at  32 - Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)

[[[ Keyset 'Cyclic' Tests ]]]

Keyset 'Cyclic' - 8 cycles of 32 bytes - 1000000 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        116.4, actual    110 (0.94x)
Testing collisions (high 23-34 bits) - Worst is 33 bits: 59/58 (1.01x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        116.4, actual    114 (0.98x)
Testing collisions (low  23-34 bits) - Worst is 34 bits: 30/29 (1.03x)
Testing distribution - Worst bias is the 17-bit window at bit 196 - 0.134%

Keyset 'Cyclic' - 8 cycles of 33 bytes - 1000000 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        116.4, actual    120 (1.03x) (4)
Testing collisions (high 23-34 bits) - Worst is 29 bits: 985/930 (1.06x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        116.4, actual    108 (0.93x)
Testing collisions (low  23-34 bits) - Worst is 31 bits: 240/232 (1.03x)
Testing distribution - Worst bias is the 17-bit window at bit 99 - 0.149%

Keyset 'Cyclic' - 8 cycles of 34 bytes - 1000000 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        116.4, actual    112 (0.96x)
Testing collisions (high 23-34 bits) - Worst is 34 bits: 32/29 (1.10x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        116.4, actual    112 (0.96x)
Testing collisions (low  23-34 bits) - Worst is 30 bits: 476/465 (1.02x)
Testing distribution - Worst bias is the 17-bit window at bit 74 - 0.148%

Keyset 'Cyclic' - 8 cycles of 35 bytes - 1000000 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        116.4, actual    126 (1.08x) (10)
Testing collisions (high 23-34 bits) - Worst is 34 bits: 37/29 (1.27x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        116.4, actual    123 (1.06x) (7)
Testing collisions (low  23-34 bits) - Worst is 32 bits: 123/116 (1.06x)
Testing distribution - Worst bias is the 17-bit window at bit 10 - 0.143%

Keyset 'Cyclic' - 8 cycles of 36 bytes - 1000000 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        116.4, actual    126 (1.08x) (10)
Testing collisions (high 23-34 bits) - Worst is 33 bits: 70/58 (1.20x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        116.4, actual    117 (1.01x) (1)
Testing collisions (low  23-34 bits) - Worst is 31 bits: 248/232 (1.07x)
Testing distribution - Worst bias is the 17-bit window at bit 156 - 0.160%

Keyset 'Cyclic' - 8 cycles of 40 bytes - 1000000 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        116.4, actual     99 (0.85x)
Testing collisions (high 23-34 bits) - Worst is 26 bits: 7552/7413 (1.02x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        116.4, actual    106 (0.91x)
Testing collisions (low  23-34 bits) - Worst is 34 bits: 39/29 (1.34x)
Testing distribution - Worst bias is the 17-bit window at bit 96 - 0.169%


[[[ Keyset 'TwoBytes' Tests ]]]

Keyset 'TwoBytes' - up-to-4-byte keys, 652545 total keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected         49.6, actual     54 (1.09x) (5)
Testing collisions (high 23-33 bits) - Worst is 33 bits: 28/24 (1.13x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected         49.6, actual     53 (1.07x) (4)
Testing collisions (low  23-33 bits) - Worst is 33 bits: 30/24 (1.21x)
Testing distribution - Worst bias is the 16-bit window at bit 38 - 0.190%

Keyset 'TwoBytes' - up-to-8-byte keys, 5471025 total keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected       3483.1, actual   3426 (0.98x) (-57)
Testing collisions (high 26-39 bits) - Worst is 39 bits: 38/27 (1.40x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected       3483.1, actual   3506 (1.01x) (23)
Testing collisions (low  26-39 bits) - Worst is 32 bits: 3506/3483 (1.01x)
Testing distribution - Worst bias is the 20-bit window at bit 49 - 0.074%

Keyset 'TwoBytes' - up-to-12-byte keys, 18616785 total keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected      40289.5, actual  40420 (1.00x) (131)
Testing collisions (high 27-42 bits) - Worst is 32 bits: 40420/40289 (1.00x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected      40289.5, actual  40336 (1.00x) (47)
Testing collisions (low  27-42 bits) - Worst is 40 bits: 167/157 (1.06x)
Testing distribution - Worst bias is the 20-bit window at bit 224 - 0.021%


[[[ Keyset 'Text' Tests ]]]

Keyset 'Text' - keys of form "FooXXXXBar" - 14776336 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected      25389.0, actual  25477 (1.00x) (88)
Testing collisions (high 27-42 bits) - Worst is 40 bits: 106/99 (1.07x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected      25389.0, actual  25414 (1.00x) (25)
Testing collisions (low  27-42 bits) - Worst is 42 bits: 28/24 (1.13x)
Testing distribution - Worst bias is the 20-bit window at bit 159 - 0.025%

Keyset 'Text' - keys of form "FooBarXXXX" - 14776336 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected      25389.0, actual  25577 (1.01x) (188)
Testing collisions (high 27-42 bits) - Worst is 30 bits: 102060/101207 (1.01x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected      25389.0, actual  25542 (1.01x) (153)
Testing collisions (low  27-42 bits) - Worst is 42 bits: 29/24 (1.17x)
Testing distribution - Worst bias is the 20-bit window at bit 145 - 0.029%

Keyset 'Text' - keys of form "XXXXFooBar" - 14776336 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected      25389.0, actual  25269 (1.00x) (-120)
Testing collisions (high 27-42 bits) - Worst is 40 bits: 100/99 (1.01x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected      25389.0, actual  25652 (1.01x) (263)
Testing collisions (low  27-42 bits) - Worst is 36 bits: 1618/1588 (1.02x)
Testing distribution - Worst bias is the 20-bit window at bit 221 - 0.030%

Keyset 'Words' - 4000000 random keys of len 6-16 from alnum charset
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected       1862.1, actual   1906 (1.02x) (44)
Testing collisions (high 25-38 bits) - Worst is 37 bits: 69/58 (1.19x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected       1862.1, actual   1764 (0.95x)
Testing collisions (low  25-38 bits) - Worst is 30 bits: 7596/7441 (1.02x)
Testing distribution - Worst bias is the 19-bit window at bit 55 - 0.071%

Keyset 'Words' - 4000000 random keys of len 6-16 from password charset
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected       1862.1, actual   1809 (0.97x)
Testing collisions (high 25-38 bits) - Worst is 38 bits: 34/29 (1.17x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected       1862.1, actual   1842 (0.99x) (-20)
Testing collisions (low  25-38 bits) - Worst is 29 bits: 15013/14864 (1.01x)
Testing distribution - Worst bias is the 19-bit window at bit 58 - 0.072%

Unable to open words dict file /usr/share/dict/words
Keyset 'Words' - 0 dict words
Testing collisions (256-bit) - Expected   -0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected         -0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected         -0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected         -0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected         -0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected         -0.0, actual      0 (0.00x)
Testing collisions (high  2- 2 bits) - Worst is  0 bits:  0/ 1 (0.00x)
Testing collisions (low  224-bit) - Expected         -0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected         -0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected         -0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected         -0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected         -0.0, actual      0 (0.00x)
Testing collisions (low   2- 2 bits) - Worst is  0 bits:  0/ 1 (0.00x)


[[[ Keyset 'Zeroes' Tests ]]]

Keyset 'Zeroes' - 204800 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected          4.9, actual      8 (1.64x) (4)
Testing collisions (high 21-29 bits) - Worst is 29 bits: 42/39 (1.08x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected          4.9, actual      0 (0.00x)
Testing collisions (low  21-29 bits) - Worst is 28 bits: 88/78 (1.13x)
Testing distribution - Worst bias is the 15-bit window at bit 191 - 0.296%


[[[ Keyset 'Seed' Tests ]]]

Keyset 'Seed' - 5000000 keys
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected       2909.3, actual   2844 (0.98x)
Testing collisions (high 26-39 bits) - Worst is 31 bits: 5882/5816 (1.01x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected       2909.3, actual   2937 (1.01x) (28)
Testing collisions (low  26-39 bits) - Worst is 38 bits: 53/45 (1.17x)
Testing distribution - Worst bias is the 19-bit window at bit 239 - 0.057%


[[[ Keyset 'PerlinNoise' Tests ]]]

Testing 16777216 coordinates (L2) : 
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected      32725.4, actual  32496 (0.99x) (-229)
Testing collisions (high 27-42 bits) - Worst is 35 bits: 4190/4095 (1.02x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected      32725.4, actual  32835 (1.00x) (110)
Testing collisions (low  27-42 bits) - Worst is 42 bits: 42/31 (1.31x)

Testing AV variant, 128 count with 4 spacing, 4-12:
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected       1116.2, actual   1160 (1.04x) (44)
Testing collisions (high 25-37 bits) - Worst is 37 bits: 40/34 (1.15x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected       1116.2, actual   1082 (0.97x)
Testing collisions (low  25-37 bits) - Worst is 36 bits: 79/69 (1.13x)


[[[ Diff 'Differential' Tests ]]]

Testing 8303632 up-to-5-bit differentials in 64-bit keys -> 256 bit hashes.
100 reps, 830363200 total tests, expecting 0.00 random collisions..........
0 total collisions, of which 0 single collisions were ignored

Testing 11017632 up-to-4-bit differentials in 128-bit keys -> 256 bit hashes.
100 reps, 1101763200 total tests, expecting 0.00 random collisions..........
0 total collisions, of which 0 single collisions were ignored

Testing 2796416 up-to-3-bit differentials in 256-bit keys -> 256 bit hashes.
100 reps, 279641600 total tests, expecting 0.00 random collisions..........
0 total collisions, of which 0 single collisions were ignored


[[[ DiffDist 'Differential Distribution' Tests ]]]

Testing bit 0
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    511 (1.00x)
Testing collisions (high 24-36 bits) - Worst is 29 bits: 4170/4090 (1.02x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    500 (0.98x)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 42/31 (1.31x)
Testing distribution - Worst bias is the 18-bit window at bit 146 - 0.072%

Testing bit 1
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    521 (1.02x) (10)
Testing collisions (high 24-36 bits) - Worst is 35 bits: 68/63 (1.06x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    550 (1.07x) (39)
Testing collisions (low  24-36 bits) - Worst is 35 bits: 76/63 (1.19x)
Testing distribution - Worst bias is the 18-bit window at bit 84 - 0.115%

Testing bit 2
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    495 (0.97x)
Testing collisions (high 24-36 bits) - Worst is 29 bits: 4112/4090 (1.01x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    521 (1.02x) (10)
Testing collisions (low  24-36 bits) - Worst is 32 bits: 521/511 (1.02x)
Testing distribution - Worst bias is the 18-bit window at bit 163 - 0.130%

Testing bit 3
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    549 (1.07x) (38)
Testing collisions (high 24-36 bits) - Worst is 33 bits: 282/255 (1.10x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    507 (0.99x) (-4)
Testing collisions (low  24-36 bits) - Worst is 34 bits: 148/127 (1.16x)
Testing distribution - Worst bias is the 18-bit window at bit 253 - 0.129%

Testing bit 4
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    520 (1.02x) (9)
Testing collisions (high 24-36 bits) - Worst is 32 bits: 520/511 (1.02x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    512 (1.00x) (1)
Testing collisions (low  24-36 bits) - Worst is 35 bits: 74/63 (1.16x)
Testing distribution - Worst bias is the 18-bit window at bit 141 - 0.110%

Testing bit 5
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    524 (1.02x) (13)
Testing collisions (high 24-36 bits) - Worst is 34 bits: 140/127 (1.09x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    511 (1.00x)
Testing collisions (low  24-36 bits) - Worst is 33 bits: 266/255 (1.04x)
Testing distribution - Worst bias is the 18-bit window at bit 18 - 0.090%

Testing bit 6
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    515 (1.01x) (4)
Testing collisions (high 24-36 bits) - Worst is 33 bits: 267/255 (1.04x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    502 (0.98x) (-9)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 38/31 (1.19x)
Testing distribution - Worst bias is the 18-bit window at bit 13 - 0.112%

Testing bit 7
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    462 (0.90x)
Testing collisions (high 24-36 bits) - Worst is 36 bits: 38/31 (1.19x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    522 (1.02x) (11)
Testing collisions (low  24-36 bits) - Worst is 35 bits: 82/63 (1.28x)
Testing distribution - Worst bias is the 18-bit window at bit 167 - 0.133%

Testing bit 8
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    507 (0.99x) (-4)
Testing collisions (high 24-36 bits) - Worst is 34 bits: 142/127 (1.11x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    504 (0.98x) (-7)
Testing collisions (low  24-36 bits) - Worst is 34 bits: 132/127 (1.03x)
Testing distribution - Worst bias is the 18-bit window at bit 173 - 0.099%

Testing bit 9
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    513 (1.00x) (2)
Testing collisions (high 24-36 bits) - Worst is 27 bits: 16406/16298 (1.01x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    495 (0.97x)
Testing collisions (low  24-36 bits) - Worst is 34 bits: 136/127 (1.06x)
Testing distribution - Worst bias is the 18-bit window at bit 240 - 0.114%

Testing bit 10
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    536 (1.05x) (25)
Testing collisions (high 24-36 bits) - Worst is 33 bits: 275/255 (1.07x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    548 (1.07x) (37)
Testing collisions (low  24-36 bits) - Worst is 32 bits: 548/511 (1.07x)
Testing distribution - Worst bias is the 18-bit window at bit 108 - 0.119%

Testing bit 11
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    522 (1.02x) (11)
Testing collisions (high 24-36 bits) - Worst is 32 bits: 522/511 (1.02x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    471 (0.92x)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 36/31 (1.13x)
Testing distribution - Worst bias is the 18-bit window at bit 22 - 0.118%

Testing bit 12
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    507 (0.99x) (-4)
Testing collisions (high 24-36 bits) - Worst is 36 bits: 40/31 (1.25x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    544 (1.06x) (33)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 35/31 (1.09x)
Testing distribution - Worst bias is the 18-bit window at bit 229 - 0.120%

Testing bit 13
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    553 (1.08x) (42)
Testing collisions (high 24-36 bits) - Worst is 36 bits: 41/31 (1.28x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    502 (0.98x) (-9)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 36/31 (1.13x)
Testing distribution - Worst bias is the 18-bit window at bit 13 - 0.095%

Testing bit 14
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    510 (1.00x) (-1)
Testing collisions (high 24-36 bits) - Worst is 26 bits: 32492/32429 (1.00x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    486 (0.95x)
Testing collisions (low  24-36 bits) - Worst is 35 bits: 66/63 (1.03x)
Testing distribution - Worst bias is the 18-bit window at bit 29 - 0.093%

Testing bit 15
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    507 (0.99x) (-4)
Testing collisions (high 24-36 bits) - Worst is 35 bits: 67/63 (1.05x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    492 (0.96x)
Testing collisions (low  24-36 bits) - Worst is 30 bits: 2051/2046 (1.00x)
Testing distribution - Worst bias is the 18-bit window at bit 135 - 0.094%

Testing bit 16
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    507 (0.99x) (-4)
Testing collisions (high 24-36 bits) - Worst is 25 bits: 64374/64191 (1.00x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    538 (1.05x) (27)
Testing collisions (low  24-36 bits) - Worst is 35 bits: 76/63 (1.19x)
Testing distribution - Worst bias is the 18-bit window at bit 24 - 0.095%

Testing bit 17
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    494 (0.97x)
Testing collisions (high 24-36 bits) - Worst is 28 bits: 8237/8170 (1.01x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    537 (1.05x) (26)
Testing collisions (low  24-36 bits) - Worst is 32 bits: 537/511 (1.05x)
Testing distribution - Worst bias is the 18-bit window at bit 84 - 0.099%

Testing bit 18
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    500 (0.98x)
Testing collisions (high 24-36 bits) - Worst is 36 bits: 41/31 (1.28x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    513 (1.00x) (2)
Testing collisions (low  24-36 bits) - Worst is 31 bits: 1043/1023 (1.02x)
Testing distribution - Worst bias is the 18-bit window at bit 83 - 0.107%

Testing bit 19
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    510 (1.00x) (-1)
Testing collisions (high 24-36 bits) - Worst is 30 bits: 2099/2046 (1.03x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    531 (1.04x) (20)
Testing collisions (low  24-36 bits) - Worst is 34 bits: 138/127 (1.08x)
Testing distribution - Worst bias is the 18-bit window at bit 74 - 0.089%

Testing bit 20
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    523 (1.02x) (12)
Testing collisions (high 24-36 bits) - Worst is 36 bits: 37/31 (1.16x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    454 (0.89x)
Testing collisions (low  24-36 bits) - Worst is 24 bits: 125849/125777 (1.00x)
Testing distribution - Worst bias is the 18-bit window at bit 130 - 0.120%

Testing bit 21
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    515 (1.01x) (4)
Testing collisions (high 24-36 bits) - Worst is 35 bits: 65/63 (1.02x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    503 (0.98x) (-8)
Testing collisions (low  24-36 bits) - Worst is 26 bits: 32616/32429 (1.01x)
Testing distribution - Worst bias is the 18-bit window at bit 74 - 0.113%

Testing bit 22
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    511 (1.00x)
Testing collisions (high 24-36 bits) - Worst is 31 bits: 1051/1023 (1.03x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    552 (1.08x) (41)
Testing collisions (low  24-36 bits) - Worst is 32 bits: 552/511 (1.08x)
Testing distribution - Worst bias is the 18-bit window at bit 71 - 0.120%

Testing bit 23
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    491 (0.96x)
Testing collisions (high 24-36 bits) - Worst is 35 bits: 67/63 (1.05x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    557 (1.09x) (46)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 43/31 (1.34x)
Testing distribution - Worst bias is the 18-bit window at bit 231 - 0.099%

Testing bit 24
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    502 (0.98x) (-9)
Testing collisions (high 24-36 bits) - Worst is 35 bits: 64/63 (1.00x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    520 (1.02x) (9)
Testing collisions (low  24-36 bits) - Worst is 34 bits: 132/127 (1.03x)
Testing distribution - Worst bias is the 18-bit window at bit 115 - 0.113%

Testing bit 25
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    458 (0.89x)
Testing collisions (high 24-36 bits) - Worst is 25 bits: 64135/64191 (1.00x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    529 (1.03x) (18)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 34/31 (1.06x)
Testing distribution - Worst bias is the 18-bit window at bit 174 - 0.078%

Testing bit 26
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    478 (0.93x)
Testing collisions (high 24-36 bits) - Worst is 24 bits: 125480/125777 (1.00x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    536 (1.05x) (25)
Testing collisions (low  24-36 bits) - Worst is 33 bits: 278/255 (1.09x)
Testing distribution - Worst bias is the 18-bit window at bit 82 - 0.102%

Testing bit 27
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    533 (1.04x) (22)
Testing collisions (high 24-36 bits) - Worst is 35 bits: 76/63 (1.19x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    569 (1.11x) (58)
Testing collisions (low  24-36 bits) - Worst is 34 bits: 155/127 (1.21x)
Testing distribution - Worst bias is the 18-bit window at bit 59 - 0.086%

Testing bit 28
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    533 (1.04x) (22)
Testing collisions (high 24-36 bits) - Worst is 32 bits: 533/511 (1.04x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    525 (1.03x) (14)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 35/31 (1.09x)
Testing distribution - Worst bias is the 18-bit window at bit 180 - 0.075%

Testing bit 29
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    540 (1.05x) (29)
Testing collisions (high 24-36 bits) - Worst is 36 bits: 48/31 (1.50x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    541 (1.06x) (30)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 42/31 (1.31x)
Testing distribution - Worst bias is the 18-bit window at bit 111 - 0.108%

Testing bit 30
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    554 (1.08x) (43)
Testing collisions (high 24-36 bits) - Worst is 34 bits: 143/127 (1.12x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    506 (0.99x) (-5)
Testing collisions (low  24-36 bits) - Worst is 27 bits: 16451/16298 (1.01x)
Testing distribution - Worst bias is the 18-bit window at bit 115 - 0.086%

Testing bit 31
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    495 (0.97x)
Testing collisions (high 24-36 bits) - Worst is 34 bits: 131/127 (1.02x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    479 (0.94x)
Testing collisions (low  24-36 bits) - Worst is 24 bits: 126004/125777 (1.00x)
Testing distribution - Worst bias is the 18-bit window at bit 112 - 0.092%

Testing bit 32
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    508 (0.99x) (-3)
Testing collisions (high 24-36 bits) - Worst is 36 bits: 36/31 (1.13x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    521 (1.02x) (10)
Testing collisions (low  24-36 bits) - Worst is 29 bits: 4207/4090 (1.03x)
Testing distribution - Worst bias is the 18-bit window at bit 19 - 0.113%

Testing bit 33
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    500 (0.98x)
Testing collisions (high 24-36 bits) - Worst is 36 bits: 43/31 (1.34x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    511 (1.00x)
Testing collisions (low  24-36 bits) - Worst is 35 bits: 75/63 (1.17x)
Testing distribution - Worst bias is the 18-bit window at bit 64 - 0.099%

Testing bit 34
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    552 (1.08x) (41)
Testing collisions (high 24-36 bits) - Worst is 35 bits: 71/63 (1.11x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    533 (1.04x) (22)
Testing collisions (low  24-36 bits) - Worst is 31 bits: 1067/1023 (1.04x)
Testing distribution - Worst bias is the 18-bit window at bit 163 - 0.095%

Testing bit 35
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    534 (1.04x) (23)
Testing collisions (high 24-36 bits) - Worst is 32 bits: 534/511 (1.04x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    493 (0.96x)
Testing collisions (low  24-36 bits) - Worst is 35 bits: 68/63 (1.06x)
Testing distribution - Worst bias is the 18-bit window at bit 178 - 0.087%

Testing bit 36
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    532 (1.04x) (21)
Testing collisions (high 24-36 bits) - Worst is 35 bits: 81/63 (1.27x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    472 (0.92x)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 34/31 (1.06x)
Testing distribution - Worst bias is the 18-bit window at bit 81 - 0.092%

Testing bit 37
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    552 (1.08x) (41)
Testing collisions (high 24-36 bits) - Worst is 35 bits: 90/63 (1.41x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    533 (1.04x) (22)
Testing collisions (low  24-36 bits) - Worst is 33 bits: 275/255 (1.07x)
Testing distribution - Worst bias is the 18-bit window at bit 188 - 0.114%

Testing bit 38
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    507 (0.99x) (-4)
Testing collisions (high 24-36 bits) - Worst is 31 bits: 1051/1023 (1.03x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    534 (1.04x) (23)
Testing collisions (low  24-36 bits) - Worst is 32 bits: 534/511 (1.04x)
Testing distribution - Worst bias is the 18-bit window at bit 74 - 0.094%

Testing bit 39
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    524 (1.02x) (13)
Testing collisions (high 24-36 bits) - Worst is 36 bits: 35/31 (1.09x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    544 (1.06x) (33)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 36/31 (1.13x)
Testing distribution - Worst bias is the 18-bit window at bit 97 - 0.072%

Testing bit 40
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    485 (0.95x)
Testing collisions (high 24-36 bits) - Worst is 31 bits: 1042/1023 (1.02x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    518 (1.01x) (7)
Testing collisions (low  24-36 bits) - Worst is 31 bits: 1085/1023 (1.06x)
Testing distribution - Worst bias is the 18-bit window at bit 245 - 0.092%

Testing bit 41
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    535 (1.05x) (24)
Testing collisions (high 24-36 bits) - Worst is 36 bits: 38/31 (1.19x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    535 (1.05x) (24)
Testing collisions (low  24-36 bits) - Worst is 34 bits: 143/127 (1.12x)
Testing distribution - Worst bias is the 18-bit window at bit 58 - 0.106%

Testing bit 42
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    485 (0.95x)
Testing collisions (high 24-36 bits) - Worst is 30 bits: 2049/2046 (1.00x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    500 (0.98x)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 34/31 (1.06x)
Testing distribution - Worst bias is the 18-bit window at bit 198 - 0.091%

Testing bit 43
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    506 (0.99x) (-5)
Testing collisions (high 24-36 bits) - Worst is 35 bits: 71/63 (1.11x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    505 (0.99x) (-6)
Testing collisions (low  24-36 bits) - Worst is 33 bits: 265/255 (1.04x)
Testing distribution - Worst bias is the 18-bit window at bit 63 - 0.097%

Testing bit 44
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    468 (0.91x)
Testing collisions (high 24-36 bits) - Worst is 26 bits: 32619/32429 (1.01x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    492 (0.96x)
Testing collisions (low  24-36 bits) - Worst is 29 bits: 4158/4090 (1.02x)
Testing distribution - Worst bias is the 18-bit window at bit 62 - 0.107%

Testing bit 45
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    519 (1.01x) (8)
Testing collisions (high 24-36 bits) - Worst is 36 bits: 39/31 (1.22x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    503 (0.98x) (-8)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 33/31 (1.03x)
Testing distribution - Worst bias is the 18-bit window at bit 54 - 0.088%

Testing bit 46
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    492 (0.96x)
Testing collisions (high 24-36 bits) - Worst is 28 bits: 8183/8170 (1.00x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    502 (0.98x) (-9)
Testing collisions (low  24-36 bits) - Worst is 34 bits: 133/127 (1.04x)
Testing distribution - Worst bias is the 18-bit window at bit 66 - 0.085%

Testing bit 47
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    547 (1.07x) (36)
Testing collisions (high 24-36 bits) - Worst is 32 bits: 547/511 (1.07x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    484 (0.95x)
Testing collisions (low  24-36 bits) - Worst is 33 bits: 260/255 (1.02x)
Testing distribution - Worst bias is the 18-bit window at bit 166 - 0.115%

Testing bit 48
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    517 (1.01x) (6)
Testing collisions (high 24-36 bits) - Worst is 36 bits: 36/31 (1.13x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    481 (0.94x)
Testing collisions (low  24-36 bits) - Worst is 35 bits: 68/63 (1.06x)
Testing distribution - Worst bias is the 18-bit window at bit 147 - 0.118%

Testing bit 49
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    519 (1.01x) (8)
Testing collisions (high 24-36 bits) - Worst is 36 bits: 45/31 (1.41x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    511 (1.00x)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 39/31 (1.22x)
Testing distribution - Worst bias is the 18-bit window at bit 239 - 0.104%

Testing bit 50
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    503 (0.98x) (-8)
Testing collisions (high 24-36 bits) - Worst is 33 bits: 261/255 (1.02x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    489 (0.96x)
Testing collisions (low  24-36 bits) - Worst is 34 bits: 133/127 (1.04x)
Testing distribution - Worst bias is the 18-bit window at bit 100 - 0.108%

Testing bit 51
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    493 (0.96x)
Testing collisions (high 24-36 bits) - Worst is 30 bits: 2070/2046 (1.01x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    511 (1.00x)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 42/31 (1.31x)
Testing distribution - Worst bias is the 18-bit window at bit 27 - 0.116%

Testing bit 52
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    504 (0.98x) (-7)
Testing collisions (high 24-36 bits) - Worst is 34 bits: 135/127 (1.05x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    511 (1.00x)
Testing collisions (low  24-36 bits) - Worst is 31 bits: 1060/1023 (1.04x)
Testing distribution - Worst bias is the 18-bit window at bit  0 - 0.084%

Testing bit 53
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    510 (1.00x) (-1)
Testing collisions (high 24-36 bits) - Worst is 36 bits: 38/31 (1.19x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    520 (1.02x) (9)
Testing collisions (low  24-36 bits) - Worst is 33 bits: 262/255 (1.02x)
Testing distribution - Worst bias is the 18-bit window at bit 87 - 0.098%

Testing bit 54
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    538 (1.05x) (27)
Testing collisions (high 24-36 bits) - Worst is 32 bits: 538/511 (1.05x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    542 (1.06x) (31)
Testing collisions (low  24-36 bits) - Worst is 32 bits: 542/511 (1.06x)
Testing distribution - Worst bias is the 18-bit window at bit 244 - 0.095%

Testing bit 55
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    540 (1.05x) (29)
Testing collisions (high 24-36 bits) - Worst is 36 bits: 36/31 (1.13x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    531 (1.04x) (20)
Testing collisions (low  24-36 bits) - Worst is 31 bits: 1094/1023 (1.07x)
Testing distribution - Worst bias is the 18-bit window at bit 118 - 0.137%

Testing bit 56
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    486 (0.95x)
Testing collisions (high 24-36 bits) - Worst is 35 bits: 79/63 (1.23x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    547 (1.07x) (36)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 40/31 (1.25x)
Testing distribution - Worst bias is the 18-bit window at bit 199 - 0.108%

Testing bit 57
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    514 (1.00x) (3)
Testing collisions (high 24-36 bits) - Worst is 34 bits: 146/127 (1.14x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    522 (1.02x) (11)
Testing collisions (low  24-36 bits) - Worst is 32 bits: 522/511 (1.02x)
Testing distribution - Worst bias is the 18-bit window at bit 220 - 0.089%

Testing bit 58
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    472 (0.92x)
Testing collisions (high 24-36 bits) - Worst is 25 bits: 64195/64191 (1.00x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    536 (1.05x) (25)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 39/31 (1.22x)
Testing distribution - Worst bias is the 18-bit window at bit 241 - 0.092%

Testing bit 59
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    553 (1.08x) (42)
Testing collisions (high 24-36 bits) - Worst is 33 bits: 297/255 (1.16x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    511 (1.00x)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 36/31 (1.13x)
Testing distribution - Worst bias is the 18-bit window at bit 202 - 0.100%

Testing bit 60
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    501 (0.98x)
Testing collisions (high 24-36 bits) - Worst is 35 bits: 67/63 (1.05x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    518 (1.01x) (7)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 37/31 (1.16x)
Testing distribution - Worst bias is the 18-bit window at bit 20 - 0.096%

Testing bit 61
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    514 (1.00x) (3)
Testing collisions (high 24-36 bits) - Worst is 32 bits: 514/511 (1.00x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    525 (1.03x) (14)
Testing collisions (low  24-36 bits) - Worst is 36 bits: 38/31 (1.19x)
Testing distribution - Worst bias is the 18-bit window at bit 19 - 0.088%

Testing bit 62
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    514 (1.00x) (3)
Testing collisions (high 24-36 bits) - Worst is 35 bits: 70/63 (1.09x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    527 (1.03x) (16)
Testing collisions (low  24-36 bits) - Worst is 34 bits: 140/127 (1.09x)
Testing distribution - Worst bias is the 18-bit window at bit 100 - 0.100%

Testing bit 63
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected        511.9, actual    487 (0.95x)
Testing collisions (high 24-36 bits) - Worst is 30 bits: 2087/2046 (1.02x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected        511.9, actual    501 (0.98x)
Testing collisions (low  24-36 bits) - Worst is 24 bits: 125723/125777 (1.00x)
Testing distribution - Worst bias is the 18-bit window at bit 239 - 0.116%


[[[ Prng Tests ]]]

Generating 33554432 random numbers : 
Testing collisions (256-bit) - Expected    0.0, actual      0 (0.00x)
Testing collisions (high 224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (high 32-bit) - Expected     130731.3, actual 130376 (1.00x) (-355)
Testing collisions (high 28-44 bits) - Worst is 28 bits: 2011363/2012434 (1.00x)
Testing collisions (low  224-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  160-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  128-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  64-bit) - Expected          0.0, actual      0 (0.00x)
Testing collisions (low  32-bit) - Expected     130731.3, actual 130218 (1.00x) (-513)
Testing collisions (low  28-44 bits) - Worst is 42 bits: 143/127 (1.12x)

[[[ BadSeeds Tests ]]]

Testing 0 internal bad seeds:
0x0 PASS


Input vcode 0x00000001, Output vcode 0x00000001, Result vcode 0x00000001
Verification value is 0x00000001 - Testing took 2418.532000 seconds
-------------------------------------------------------------------------------

```
