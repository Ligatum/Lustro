```text
=================================================================
                 LUSTRO CORE V1 - PREMIERE AUDIT                 
=================================================================

[*] Running test: B2...

[>>>] B2: AVALANCHE / SAC
[>>>] Samples: 5,000,000
[>>>] Single-bit flips: 256
[>>>] Second-order pairs: 512
  [1/5] single-bit flips...
  [2/5] second-order SAC (512 pairs)...
  [3/5] structured flips (108 masks)...
  [4/5] conditional SAC (256 bits)...
  [5/5] analysis...

[B2] RESULTS (samples=5,000,000)

  --- SAC MATRIX (single-bit) ---
  Max deviation    : 0.000988  (ideal 0.0)
  Mean deviation   : 0.000178
  RMS deviation    : 0.000223
  Worst cell       : (np.int64(136), np.int64(80))
  EV-normalized z  : -0.29σ
  [OK] uniform

  --- LANE s0 -> o0 ---
  Max deviation    : 0.000919  (ideal 0.0)
  Mean deviation   : 0.000178
  RMS deviation    : 0.000222
  Worst cell       : (np.int64(83), np.int64(109))
  EV-normalized z  : -0.30σ
  [OK] uniform

  --- LANE s0 -> o1 ---
  Max deviation    : 0.000973  (ideal 0.0)
  Mean deviation   : 0.000180
  RMS deviation    : 0.000225
  Worst cell       : (np.int64(47), np.int64(0))
  EV-normalized z  : -0.05σ
  [OK] uniform

  --- LANE s1 -> o0 ---
  Max deviation    : 0.000988  (ideal 0.0)
  Mean deviation   : 0.000178
  RMS deviation    : 0.000223
  Worst cell       : (np.int64(8), np.int64(80))
  EV-normalized z  : 0.01σ
  [OK] uniform

  --- LANE s1 -> o1 ---
  Max deviation    : 0.000916  (ideal 0.0)
  Mean deviation   : 0.000178
  RMS deviation    : 0.000224
  Worst cell       : (np.int64(38), np.int64(76))
  EV-normalized z  : -0.31σ
  [OK] uniform

  --- SECOND-ORDER SAC ---
  Max deviation    : 0.001113  (ideal 0.0)
  Mean deviation   : 0.000178
  RMS deviation    : 0.000223
  Worst cell       : (np.int64(162), np.int64(187))
  EV-normalized z  : 0.12σ
  [OK] uniform

  --- STRUCTURED FLIPS ---
  Max deviation    : 0.001042  (ideal 0.0)
  Mean deviation   : 0.000178
  RMS deviation    : 0.000224
  Worst cell       : (np.int64(82), np.int64(20))
  EV-normalized z  : 0.14σ
  [OK] uniform

  --- HW: single-bit flips ---
  Avg HW           : 128.0004  (ideal 128.0)
  Variance HW      : 63.9985  (ideal ~64.0)
  Avg HW deviation : 0.0004
  [OK] no diffusion anomaly detected
  [OK] HW variance normal (0.0σ from ideal)

  --- HW: second-order flips ---
  Avg HW           : 127.9999  (ideal 128.0)
  Variance HW      : 64.0019  (ideal ~64.0)
  Avg HW deviation : 0.0001
  [OK] no diffusion anomaly detected
  [OK] HW variance normal (0.0σ from ideal)

  --- HW: structured flips ---
  Avg HW           : 128.0007  (ideal 128.0)
  Variance HW      : 64.0023  (ideal ~64.0)
  Avg HW deviation : 0.0007
  [OK] no diffusion anomaly detected
  [OK] HW variance normal (0.1σ from ideal)

  --- CONDITIONAL SAC ---
  Worst input bit  : 73
  Max |P0-P1|      : 0.001852
  EV-normalized z  : -0.57σ

  Top 10 asymmetric input bits:
    bit  73 : max|P0-P1| = 0.001852  mean = 0.000339  RMS = 0.000431  EV-z = -0.57σ
    bit  79 : max|P0-P1| = 0.001847  mean = 0.000377  RMS = 0.000478  EV-z = -0.58σ
    bit 204 : max|P0-P1| = 0.001846  mean = 0.000399  RMS = 0.000499  EV-z = -0.58σ
    bit  38 : max|P0-P1| = 0.001838  mean = 0.000343  RMS = 0.000435  EV-z = -0.60σ
    bit 185 : max|P0-P1| = 0.001773  mean = 0.000371  RMS = 0.000479  EV-z = -0.75σ
    bit  68 : max|P0-P1| = 0.001771  mean = 0.000386  RMS = 0.000491  EV-z = -0.75σ
    bit  55 : max|P0-P1| = 0.001727  mean = 0.000364  RMS = 0.000460  EV-z = -0.85σ
    bit  92 : max|P0-P1| = 0.001709  mean = 0.000388  RMS = 0.000481  EV-z = -0.89σ
    bit 193 : max|P0-P1| = 0.001685  mean = 0.000366  RMS = 0.000461  EV-z = -0.94σ
    bit 113 : max|P0-P1| = 0.001670  mean = 0.000376  RMS = 0.000482  EV-z = -0.97σ

  [OK] no conditional bias
[OK] Test B2 finished in 495.96s.

[*] Running test: B2...

[>>>] B2: AVALANCHE / SAC
[>>>] Samples: 20,000,000
[>>>] Single-bit flips: 256
[>>>] Second-order pairs: 512
  [1/5] single-bit flips...
  [2/5] second-order SAC (512 pairs)...
  [3/5] structured flips (108 masks)...
  [4/5] conditional SAC (256 bits)...
  [5/5] analysis...

[B2] RESULTS (samples=20,000,000)

  --- SAC MATRIX (single-bit) ---
  Max deviation    : 0.000463  (ideal 0.0)
  Mean deviation   : 0.000089
  RMS deviation    : 0.000112
  Worst cell       : (np.int64(250), np.int64(78))
  EV-normalized z  : -0.57σ
  [OK] uniform

  --- LANE s0 -> o0 ---
  Max deviation    : 0.000449  (ideal 0.0)
  Mean deviation   : 0.000089
  RMS deviation    : 0.000112
  Worst cell       : (np.int64(82), np.int64(6))
  EV-normalized z  : -0.39σ
  [OK] uniform

  --- LANE s0 -> o1 ---
  Max deviation    : 0.000445  (ideal 0.0)
  Mean deviation   : 0.000090
  RMS deviation    : 0.000113
  Worst cell       : (np.int64(66), np.int64(103))
  EV-normalized z  : -0.43σ
  [OK] uniform

  --- LANE s1 -> o0 ---
  Max deviation    : 0.000463  (ideal 0.0)
  Mean deviation   : 0.000089
  RMS deviation    : 0.000112
  Worst cell       : (np.int64(122), np.int64(78))
  EV-normalized z  : -0.26σ
  [OK] uniform

  --- LANE s1 -> o1 ---
  Max deviation    : 0.000416  (ideal 0.0)
  Mean deviation   : 0.000089
  RMS deviation    : 0.000112
  Worst cell       : (np.int64(110), np.int64(63))
  EV-normalized z  : -0.69σ
  [OK] uniform

  --- SECOND-ORDER SAC ---
  Max deviation    : 0.000521  (ideal 0.0)
  Mean deviation   : 0.000089
  RMS deviation    : 0.000112
  Worst cell       : (np.int64(73), np.int64(182))
  EV-normalized z  : -0.20σ
  [OK] uniform

  --- STRUCTURED FLIPS ---
  Max deviation    : 0.000490  (ideal 0.0)
  Mean deviation   : 0.000089
  RMS deviation    : 0.000112
  Worst cell       : (np.int64(30), np.int64(7))
  EV-normalized z  : -0.14σ
  [OK] uniform

  --- HW: single-bit flips ---
  Avg HW           : 128.0002  (ideal 128.0)
  Variance HW      : 63.9988  (ideal ~64.0)
  Avg HW deviation : 0.0002
  [OK] no diffusion anomaly detected
  [OK] HW variance normal (0.1σ from ideal)

  --- HW: second-order flips ---
  Avg HW           : 128.0000  (ideal 128.0)
  Variance HW      : 64.0018  (ideal ~64.0)
  Avg HW deviation : 0.0000
  [OK] no diffusion anomaly detected
  [OK] HW variance normal (0.1σ from ideal)

  --- HW: structured flips ---
  Avg HW           : 128.0002  (ideal 128.0)
  Variance HW      : 64.0004  (ideal ~64.0)
  Avg HW deviation : 0.0002
  [OK] no diffusion anomaly detected
  [OK] HW variance normal (0.0σ from ideal)

  --- CONDITIONAL SAC ---
  Worst input bit  : 198
  Max |P0-P1|      : 0.000978
  EV-normalized z  : -0.34σ

  Top 10 asymmetric input bits:
    bit 198 : max|P0-P1| = 0.000978  mean = 0.000184  RMS = 0.000234  EV-z = -0.34σ
    bit 132 : max|P0-P1| = 0.000927  mean = 0.000197  RMS = 0.000247  EV-z = -0.56σ
    bit 181 : max|P0-P1| = 0.000927  mean = 0.000179  RMS = 0.000227  EV-z = -0.57σ
    bit  32 : max|P0-P1| = 0.000897  mean = 0.000190  RMS = 0.000237  EV-z = -0.70σ
    bit  27 : max|P0-P1| = 0.000884  mean = 0.000179  RMS = 0.000231  EV-z = -0.76σ
    bit 208 : max|P0-P1| = 0.000855  mean = 0.000178  RMS = 0.000221  EV-z = -0.89σ
    bit 180 : max|P0-P1| = 0.000853  mean = 0.000174  RMS = 0.000219  EV-z = -0.90σ
    bit 223 : max|P0-P1| = 0.000838  mean = 0.000179  RMS = 0.000225  EV-z = -0.96σ
    bit  55 : max|P0-P1| = 0.000822  mean = 0.000194  RMS = 0.000242  EV-z = -1.03σ
    bit  96 : max|P0-P1| = 0.000820  mean = 0.000181  RMS = 0.000231  EV-z = -1.04σ

  [OK] no conditional bias
[OK] Test B2 finished in 1964.82s.

[*] Running test: B13...

[>>>] B13: STRUCTURED & TRUNCATED HIGHER-ORDER DIFFERENTIAL
[>>>] Samples: 200,000,000
[>>>] Pairs: 13 | Sources: 5 | Projections: LOW8/LOW12/LOW16

[>>>] B13 PHASE A — STRUCTURAL Δ² (HW distribution per pair)

  pair          class           avg_hw    var_hw     z_hw     z_ev   zeros   max_dev  verdict
  ----------------------------------------------------------------------------------------------------
  (63,64)       lane          128.0006   63.9880    1.09σ   -1.17σ       0  0.000112  [OK]
  (127,128)     lane          127.9995   63.9991    0.91σ   -1.36σ       0  0.000106  [OK]
  (191,192)     lane          128.0002   64.0054    0.36σ   -1.90σ       0  0.000104  [OK]
  (0,1)         carry         127.9996   64.0086    0.69σ   -1.57σ       0  0.000130  [OK]
  (62,63)       carry         127.9999   63.9986    0.24σ   -2.03σ       0  0.000102  [OK]
  (64,65)       carry         128.0004   63.9909    0.62σ   -1.65σ       0  0.000097  [OK]
  (126,127)     carry         128.0003   64.0059    0.60σ   -1.66σ       0  0.000084  [OK]
  (0,32)        rotational    127.9994   64.0029    1.06σ   -1.20σ       0  0.000102  [OK]
  (0,64)        rotational    127.9995   64.0055    0.93σ   -1.33σ       0  0.000107  [OK]
  (63,127)      rotational    128.0000   63.9862    0.01σ   -2.26σ       0  0.000098  [OK]
  (0,128)       cross         128.0005   64.0120    0.81σ   -1.45σ       0  0.000144  [OK]
  (127,191)     cross         128.0001   63.9894    0.24σ   -2.03σ       0  0.000097  [OK]
  (0,255)       mirror        127.9999   64.0001    0.25σ   -2.02σ       0  0.000108  [OK]

  --- CLASS SUMMARY (Phase A) ---
  lane         : avg_hw=128.0001  max_z=1.09σ  ev_corr=-1.17σ  zeros=0  [OK]
  carry        : avg_hw=128.0000  max_z=0.69σ  ev_corr=-1.57σ  zeros=0  [OK]
  rotational   : avg_hw=127.9996  max_z=1.06σ  ev_corr=-1.20σ  zeros=0  [OK]
  cross        : avg_hw=128.0003  max_z=0.81σ  ev_corr=-1.45σ  zeros=0  [OK]
  mirror       : avg_hw=127.9999  max_z=0.25σ  ev_corr=-2.02σ  zeros=0  [OK]

[>>>] B13 PHASE B — TRUNCATED Δ² PROJECTIONS (KL vs uniform)

  pair          source  proj       z_ev          KL  verdict
  ----------------------------------------------------------
  (63,64)       d_w0    LOW8      +0.07σ    0.000001  [OK]
  (63,64)       d_w0    LOW12     -0.38σ    0.000015  [OK]
  (63,64)       d_w0    LOW16     -0.07σ    0.000235  [OK]
  (63,64)       d_w1    LOW8      +0.04σ    0.000001  [OK]
  (63,64)       d_w1    LOW12     -0.68σ    0.000015  [OK]
  (63,64)       d_w1    LOW16     -0.14σ    0.000236  [OK]
  (63,64)       d_w2    LOW8      -0.20σ    0.000001  [OK]
  (63,64)       d_w2    LOW12     -0.45σ    0.000014  [OK]
  (63,64)       d_w2    LOW16     -0.32σ    0.000235  [OK]
  (63,64)       d_w3    LOW8      +0.16σ    0.000001  [OK]
  (63,64)       d_w3    LOW12     -0.70σ    0.000015  [OK]
  (63,64)       d_w3    LOW16     -0.16σ    0.000241  [OK]
  (63,64)       fold    LOW8      +0.02σ    0.000001  [OK]
  (63,64)       fold    LOW12     -0.27σ    0.000015  [OK]
  (63,64)       fold    LOW16     -0.40σ    0.000236  [OK]

  (127,128)     d_w0    LOW8      +0.52σ    0.000001  [OK]
  (127,128)     d_w0    LOW12     -0.48σ    0.000015  [OK]
  (127,128)     d_w0    LOW16     -0.60σ    0.000233  [OK]
  (127,128)     d_w1    LOW8      -0.05σ    0.000001  [OK]
  (127,128)     d_w1    LOW12     -0.59σ    0.000015  [OK]
  (127,128)     d_w1    LOW16     +0.01σ    0.000235  [OK]
  (127,128)     d_w2    LOW8      -0.08σ    0.000001  [OK]
  (127,128)     d_w2    LOW12     -0.37σ    0.000015  [OK]
  (127,128)     d_w2    LOW16     -0.16σ    0.000236  [OK]
  (127,128)     d_w3    LOW8      -0.32σ    0.000001  [OK]
  (127,128)     d_w3    LOW12     +0.02σ    0.000015  [OK]
  (127,128)     d_w3    LOW16     -0.31σ    0.000235  [OK]
  (127,128)     fold    LOW8      +0.76σ    0.000001  [OK]
  (127,128)     fold    LOW12     -0.32σ    0.000015  [OK]
  (127,128)     fold    LOW16     -0.26σ    0.000238  [OK]

  (191,192)     d_w0    LOW8      -0.37σ    0.000001  [OK]
  (191,192)     d_w0    LOW12     -0.16σ    0.000015  [OK]
  (191,192)     d_w0    LOW16     -0.58σ    0.000235  [OK]
  (191,192)     d_w1    LOW8      -0.50σ    0.000001  [OK]
  (191,192)     d_w1    LOW12     -0.06σ    0.000015  [OK]
  (191,192)     d_w1    LOW16     -0.52σ    0.000237  [OK]
  (191,192)     d_w2    LOW8      -0.61σ    0.000001  [OK]
  (191,192)     d_w2    LOW12     -0.06σ    0.000015  [OK]
  (191,192)     d_w2    LOW16     -0.41σ    0.000237  [OK]
  (191,192)     d_w3    LOW8      -0.45σ    0.000001  [OK]
  (191,192)     d_w3    LOW12     -0.01σ    0.000015  [OK]
  (191,192)     d_w3    LOW16     +0.13σ    0.000235  [OK]
  (191,192)     fold    LOW8      -0.18σ    0.000001  [OK]
  (191,192)     fold    LOW12     -0.06σ    0.000015  [OK]
  (191,192)     fold    LOW16     -0.60σ    0.000236  [OK]

  (0,1)         d_w0    LOW8      -0.02σ    0.000001  [OK]
  (0,1)         d_w0    LOW12     +0.01σ    0.000015  [OK]
  (0,1)         d_w0    LOW16     -0.20σ    0.000236  [OK]
  (0,1)         d_w1    LOW8      -0.17σ    0.000001  [OK]
  (0,1)         d_w1    LOW12     -0.61σ    0.000015  [OK]
  (0,1)         d_w1    LOW16     +0.46σ    0.000234  [OK]
  (0,1)         d_w2    LOW8      -0.37σ    0.000001  [OK]
  (0,1)         d_w2    LOW12     -0.73σ    0.000014  [OK]
  (0,1)         d_w2    LOW16     -0.36σ    0.000236  [OK]
  (0,1)         d_w3    LOW8      -0.02σ    0.000001  [OK]
  (0,1)         d_w3    LOW12     +0.25σ    0.000015  [OK]
  (0,1)         d_w3    LOW16     -0.25σ    0.000238  [OK]
  (0,1)         fold    LOW8      -0.32σ    0.000001  [OK]
  (0,1)         fold    LOW12     -0.02σ    0.000015  [OK]
  (0,1)         fold    LOW16     -0.03σ    0.000235  [OK]

  (62,63)       d_w0    LOW8      -0.45σ    0.000001  [OK]
  (62,63)       d_w0    LOW12     -0.34σ    0.000015  [OK]
  (62,63)       d_w0    LOW16     -0.70σ    0.000235  [OK]
  (62,63)       d_w1    LOW8      -0.19σ    0.000001  [OK]
  (62,63)       d_w1    LOW12     -0.48σ    0.000015  [OK]
  (62,63)       d_w1    LOW16     +0.02σ    0.000238  [OK]
  (62,63)       d_w2    LOW8      -0.35σ    0.000001  [OK]
  (62,63)       d_w2    LOW12     -0.50σ    0.000015  [OK]
  (62,63)       d_w2    LOW16     -0.48σ    0.000238  [OK]
  (62,63)       d_w3    LOW8      -0.42σ    0.000001  [OK]
  (62,63)       d_w3    LOW12     -0.20σ    0.000015  [OK]
  (62,63)       d_w3    LOW16     -0.31σ    0.000236  [OK]
  (62,63)       fold    LOW8      -0.23σ    0.000001  [OK]
  (62,63)       fold    LOW12     +0.03σ    0.000015  [OK]
  (62,63)       fold    LOW16     -0.25σ    0.000236  [OK]

  (64,65)       d_w0    LOW8      -0.95σ    0.000001  [OK]
  (64,65)       d_w0    LOW12     -0.66σ    0.000015  [OK]
  (64,65)       d_w0    LOW16     -0.38σ    0.000235  [OK]
  (64,65)       d_w1    LOW8      -0.66σ    0.000001  [OK]
  (64,65)       d_w1    LOW12     -0.14σ    0.000015  [OK]
  (64,65)       d_w1    LOW16     -0.60σ    0.000237  [OK]
  (64,65)       d_w2    LOW8      -0.83σ    0.000001  [OK]
  (64,65)       d_w2    LOW12     -0.20σ    0.000015  [OK]
  (64,65)       d_w2    LOW16     -0.34σ    0.000238  [OK]
  (64,65)       d_w3    LOW8      -0.37σ    0.000001  [OK]
  (64,65)       d_w3    LOW12     -0.45σ    0.000015  [OK]
  (64,65)       d_w3    LOW16     +0.00σ    0.000236  [OK]
  (64,65)       fold    LOW8      -0.41σ    0.000001  [OK]
  (64,65)       fold    LOW12     -0.67σ    0.000015  [OK]
  (64,65)       fold    LOW16     -0.14σ    0.000235  [OK]

  (126,127)     d_w0    LOW8      +0.47σ    0.000001  [OK]
  (126,127)     d_w0    LOW12     +0.18σ    0.000015  [OK]
  (126,127)     d_w0    LOW16     -0.73σ    0.000236  [OK]
  (126,127)     d_w1    LOW8      -0.66σ    0.000001  [OK]
  (126,127)     d_w1    LOW12     -0.37σ    0.000015  [OK]
  (126,127)     d_w1    LOW16     -0.13σ    0.000237  [OK]
  (126,127)     d_w2    LOW8      -0.17σ    0.000001  [OK]
  (126,127)     d_w2    LOW12     -0.48σ    0.000015  [OK]
  (126,127)     d_w2    LOW16     -0.45σ    0.000236  [OK]
  (126,127)     d_w3    LOW8      -0.67σ    0.000001  [OK]
  (126,127)     d_w3    LOW12     -0.41σ    0.000015  [OK]
  (126,127)     d_w3    LOW16     -0.47σ    0.000238  [OK]
  (126,127)     fold    LOW8      -0.46σ    0.000001  [OK]
  (126,127)     fold    LOW12     -0.26σ    0.000014  [OK]
  (126,127)     fold    LOW16     -0.25σ    0.000234  [OK]

  (0,32)        d_w0    LOW8      -0.17σ    0.000001  [OK]
  (0,32)        d_w0    LOW12     -0.13σ    0.000014  [OK]
  (0,32)        d_w0    LOW16     -0.12σ    0.000237  [OK]
  (0,32)        d_w1    LOW8      -0.58σ    0.000001  [OK]
  (0,32)        d_w1    LOW12     -0.43σ    0.000015  [OK]
  (0,32)        d_w1    LOW16     +0.14σ    0.000235  [OK]
  (0,32)        d_w2    LOW8      -0.36σ    0.000001  [OK]
  (0,32)        d_w2    LOW12     -0.50σ    0.000014  [OK]
  (0,32)        d_w2    LOW16     -0.67σ    0.000235  [OK]
  (0,32)        d_w3    LOW8      -0.67σ    0.000001  [OK]
  (0,32)        d_w3    LOW12     -0.40σ    0.000016  [OK]
  (0,32)        d_w3    LOW16     -0.32σ    0.000237  [OK]
  (0,32)        fold    LOW8      -0.41σ    0.000001  [OK]
  (0,32)        fold    LOW12     -0.11σ    0.000015  [OK]
  (0,32)        fold    LOW16     -0.22σ    0.000237  [OK]

  (0,64)        d_w0    LOW8      -0.36σ    0.000001  [OK]
  (0,64)        d_w0    LOW12     -0.08σ    0.000015  [OK]
  (0,64)        d_w0    LOW16     -0.36σ    0.000238  [OK]
  (0,64)        d_w1    LOW8      -0.14σ    0.000001  [OK]
  (0,64)        d_w1    LOW12     +0.23σ    0.000015  [OK]
  (0,64)        d_w1    LOW16     +0.47σ    0.000236  [OK]
  (0,64)        d_w2    LOW8      +0.38σ    0.000001  [OK]
  (0,64)        d_w2    LOW12     -0.46σ    0.000015  [OK]
  (0,64)        d_w2    LOW16     -0.44σ    0.000239  [OK]
  (0,64)        d_w3    LOW8      -0.62σ    0.000001  [OK]
  (0,64)        d_w3    LOW12     -0.47σ    0.000014  [OK]
  (0,64)        d_w3    LOW16     -0.25σ    0.000236  [OK]
  (0,64)        fold    LOW8      -0.45σ    0.000001  [OK]
  (0,64)        fold    LOW12     -0.10σ    0.000015  [OK]
  (0,64)        fold    LOW16     -0.18σ    0.000236  [OK]

  (63,127)      d_w0    LOW8      -0.62σ    0.000001  [OK]
  (63,127)      d_w0    LOW12     -0.54σ    0.000015  [OK]
  (63,127)      d_w0    LOW16     -0.19σ    0.000239  [OK]
  (63,127)      d_w1    LOW8      -0.19σ    0.000001  [OK]
  (63,127)      d_w1    LOW12     -0.40σ    0.000015  [OK]
  (63,127)      d_w1    LOW16     -0.53σ    0.000235  [OK]
  (63,127)      d_w2    LOW8      -0.62σ    0.000001  [OK]
  (63,127)      d_w2    LOW12     -0.35σ    0.000015  [OK]
  (63,127)      d_w2    LOW16     -0.06σ    0.000236  [OK]
  (63,127)      d_w3    LOW8      -0.57σ    0.000001  [OK]
  (63,127)      d_w3    LOW12     -0.49σ    0.000014  [OK]
  (63,127)      d_w3    LOW16     +0.00σ    0.000235  [OK]
  (63,127)      fold    LOW8      -0.28σ    0.000001  [OK]
  (63,127)      fold    LOW12     -0.36σ    0.000014  [OK]
  (63,127)      fold    LOW16     +0.41σ    0.000238  [OK]

  (0,128)       d_w0    LOW8      -0.56σ    0.000001  [OK]
  (0,128)       d_w0    LOW12     -0.40σ    0.000014  [OK]
  (0,128)       d_w0    LOW16     -0.12σ    0.000236  [OK]
  (0,128)       d_w1    LOW8      -0.46σ    0.000001  [OK]
  (0,128)       d_w1    LOW12     -0.28σ    0.000015  [OK]
  (0,128)       d_w1    LOW16     -0.47σ    0.000235  [OK]
  (0,128)       d_w2    LOW8      -0.70σ    0.000001  [OK]
  (0,128)       d_w2    LOW12     -0.34σ    0.000015  [OK]
  (0,128)       d_w2    LOW16     -0.50σ    0.000235  [OK]
  (0,128)       d_w3    LOW8      +0.16σ    0.000001  [OK]
  (0,128)       d_w3    LOW12     -0.63σ    0.000014  [OK]
  (0,128)       d_w3    LOW16     -0.66σ    0.000235  [OK]
  (0,128)       fold    LOW8      -0.57σ    0.000001  [OK]
  (0,128)       fold    LOW12     +0.14σ    0.000015  [OK]
  (0,128)       fold    LOW16     -0.42σ    0.000236  [OK]

  (127,191)     d_w0    LOW8      -0.33σ    0.000001  [OK]
  (127,191)     d_w0    LOW12     -0.30σ    0.000015  [OK]
  (127,191)     d_w0    LOW16     -0.35σ    0.000236  [OK]
  (127,191)     d_w1    LOW8      -0.46σ    0.000001  [OK]
  (127,191)     d_w1    LOW12     -0.12σ    0.000015  [OK]
  (127,191)     d_w1    LOW16     +0.08σ    0.000239  [OK]
  (127,191)     d_w2    LOW8      +0.01σ    0.000001  [OK]
  (127,191)     d_w2    LOW12     +0.04σ    0.000015  [OK]
  (127,191)     d_w2    LOW16     -0.45σ    0.000237  [OK]
  (127,191)     d_w3    LOW8      -0.74σ    0.000001  [OK]
  (127,191)     d_w3    LOW12     -0.41σ    0.000015  [OK]
  (127,191)     d_w3    LOW16     +0.03σ    0.000235  [OK]
  (127,191)     fold    LOW8      -0.05σ    0.000001  [OK]
  (127,191)     fold    LOW12     -0.12σ    0.000014  [OK]
  (127,191)     fold    LOW16     -0.13σ    0.000235  [OK]

  (0,255)       d_w0    LOW8      -0.74σ    0.000001  [OK]
  (0,255)       d_w0    LOW12     -0.31σ    0.000015  [OK]
  (0,255)       d_w0    LOW16     -0.14σ    0.000236  [OK]
  (0,255)       d_w1    LOW8      -0.55σ    0.000001  [OK]
  (0,255)       d_w1    LOW12     -0.17σ    0.000015  [OK]
  (0,255)       d_w1    LOW16     -0.30σ    0.000235  [OK]
  (0,255)       d_w2    LOW8      -0.89σ    0.000001  [OK]
  (0,255)       d_w2    LOW12     -0.48σ    0.000015  [OK]
  (0,255)       d_w2    LOW16     -0.35σ    0.000236  [OK]
  (0,255)       d_w3    LOW8      -0.50σ    0.000001  [OK]
  (0,255)       d_w3    LOW12     -0.59σ    0.000015  [OK]
  (0,255)       d_w3    LOW16     +0.06σ    0.000239  [OK]
  (0,255)       fold    LOW8      -0.49σ    0.000001  [OK]
  (0,255)       fold    LOW12     +0.25σ    0.000015  [OK]
  (0,255)       fold    LOW16     -0.52σ    0.000236  [OK]

  --- VERDICT ---
  [OK] no second-order structural bias detected at tested pairs
  [OK] no truncated projection signal above detection threshold
[OK] Test B13 finished in 191.19s.

[*] Running test: B16...

[>>>] B16: RANDOMIZED JACOBIAN ESTIMATION
[>>>] Samples: 500,000,000

  --- GLOBAL METRICS ---
  Active input bits    : 256
  Total samples        : 500,000,000
  Mean |P - 0.5|       : 0.000286  (ideal 0.000000)
  Max  |P - 0.5|       : 0.001526  (ideal 0.000000)
  RMSE                 : 0.000359  (ideal 0.000000)
  Frac cells < 0.05    : 1.0000  (ideal 1.0000)

  --- WORST 10 CELLS ---
  #     in  in_dom    out  out_dom         P   |P-0.5|      count
  -----------------------------------------------------------------
  1     84  s0_hi     174  s1_lo      0.4985    0.0015  1,953,120
  2    228  s1_hi      72  s0_hi      0.4985    0.0015  1,953,120
  3     98  s0_hi     227  s1_hi      0.5015    0.0015  1,953,120
  4    151  s1_lo     248  s1_hi      0.5015    0.0015  1,953,120
  5    172  s1_lo     135  s1_lo      0.5015    0.0015  1,953,120
  6    240  s1_hi      91  s0_hi      0.4985    0.0015  1,953,120
  7    151  s1_lo     223  s1_hi      0.5015    0.0015  1,953,120
  8    245  s1_hi      19  s0_lo      0.4986    0.0014  1,953,120
  9    248  s1_hi     166  s1_lo      0.4986    0.0014  1,953,120
  10   114  s0_hi     128  s1_lo      0.4986    0.0014  1,953,120

  --- INPUT INFLUENCE (top 10 by row_abs_dev) ---
  bit  domain        count   row_abs_dev   row_entropy   hw_mean   hw_std   hw_min
  ------------------------------------------------------------------------------------
   68  s0_hi     1,953,120      0.000321      1.000000    128.00    7.996       88
   35  s0_lo     1,953,144      0.000320      1.000000    128.00    8.004       84
   40  s0_lo     1,953,143      0.000316      1.000000    128.01    8.006       88
  114  s0_hi     1,953,120      0.000316      1.000000    128.00    8.001       88
   81  s0_hi     1,953,120      0.000316      1.000000    128.00    8.001       90
    8  s0_lo     1,953,144      0.000314      1.000000    128.01    8.009       84
  216  s1_hi     1,953,120      0.000311      1.000000    128.01    8.002       90
   45  s0_lo     1,953,143      0.000311      1.000000    128.00    8.002       83
  239  s1_hi     1,953,120      0.000310      1.000000    128.00    8.003       90
  227  s1_hi     1,953,120      0.000309      1.000000    128.00    7.996       90

  --- INPUT INFLUENCE (top 10 lowest entropy — corridors) ---
  bit  domain     row_entropy   row_abs_dev
  ---------------------------------------------
   68  s0_hi         1.000000      0.000321
  114  s0_hi         1.000000      0.000316
   35  s0_lo         1.000000      0.000320
    8  s0_lo         1.000000      0.000314
  216  s1_hi         1.000000      0.000311
  227  s1_hi         1.000000      0.000309
  140  s1_lo         1.000000      0.000309
  204  s1_hi         1.000000      0.000305
  152  s1_lo         1.000000      0.000304
   42  s0_lo         1.000000      0.000307

  --- OUTPUT SENSITIVITY (top 10 by col_abs_dev) ---
  bit  domain     col_entropy   col_abs_dev
  ---------------------------------------------
  112  s0_hi         1.000000      0.000334
   15  s0_lo         1.000000      0.000324
  242  s1_hi         1.000000      0.000317
   72  s0_hi         1.000000      0.000317
  227  s1_hi         1.000000      0.000316
   77  s0_hi         1.000000      0.000316
  162  s1_lo         1.000000      0.000314
  125  s0_hi         1.000000      0.000313
   69  s0_hi         1.000000      0.000313
   47  s0_lo         1.000000      0.000312

  --- OUTPUT SENSITIVITY (top 10 lowest entropy — dead zones) ---
  bit  domain     col_entropy   col_abs_dev
  ---------------------------------------------
  112  s0_hi         1.000000      0.000334
   72  s0_hi         1.000000      0.000317
  227  s1_hi         1.000000      0.000316
   19  s0_lo         1.000000      0.000304
   15  s0_lo         1.000000      0.000324
  125  s0_hi         1.000000      0.000313
   77  s0_hi         1.000000      0.000316
  242  s1_hi         1.000000      0.000317
  170  s1_lo         1.000000      0.000309
   47  s0_lo         1.000000      0.000312

  --- LANE BIAS (mean |P-0.5| per 64-bit block) ---
                 →s0_lo     →s0_hi     →s1_lo     →s1_hi
  ------------------------------------------------------
  s0_lo↓       0.000283   0.000287   0.000285   0.000290
  s0_hi↓       0.000289   0.000289   0.000284   0.000285
  s1_lo↓       0.000284   0.000289   0.000278   0.000284
  s1_hi↓       0.000286   0.000291   0.000284   0.000285

  --- MONTE CARLO BASELINE (n=50,000 simulations) ---
  Cell N (mean)        : 1953125
  Cell σ               : 0.000358
  MC row max|z|        : mean=3.04σ  p99=4.11σ  p99.9=4.59σ
  MC global max|z|     : mean=4.44σ  p99=5.56σ  p99.9=5.69σ
  MC row entropy       : mean=0.99999963  std=3.28e-08  p0.1=0.99999952
  MC min row entropy   : p1=0.99999949  p0.1=0.99999948

  Observed:
  max |z| raw          : 4.27σ
  MC-normalized z      : -0.61σ  (p99=5.56σ, p99.9=5.69σ)
  [OK] global max within MC expectation

  Top 10 input bits by maximum cell z-score (per-row):
  bit  domain     row_entropy    max|z|     H_z(MC)
  -------------------------------------------------------
   84  s0_hi         1.000000      4.27σ        0.13σ
  228  s1_hi         1.000000      4.26σ       -1.19σ
   98  s0_hi         1.000000      4.24σ       -1.08σ
  151  s1_lo         1.000000      4.23σ       -0.57σ
  172  s1_lo         1.000000      4.13σ       -0.54σ
  240  s1_hi         1.000000      4.11σ       -1.05σ
  245  s1_hi         1.000000      4.02σ       -0.63σ
  248  s1_hi         1.000000      4.00σ        0.12σ
  114  s0_hi         1.000000      3.95σ       -2.70σ
  220  s1_hi         1.000000      3.87σ        1.01σ

  Top 10 output bits by maximum cell z-score (per-col):
  bit  domain     col_entropy    max|z|     H_z(MC)
  -------------------------------------------------------
  174  s1_lo         1.000000      4.27σ        0.08σ
   72  s0_hi         1.000000      4.26σ       -2.64σ
  227  s1_hi         1.000000      4.24σ       -2.62σ
  248  s1_hi         1.000000      4.23σ       -0.21σ
  135  s1_lo         1.000000      4.13σ       -0.90σ
   91  s0_hi         1.000000      4.11σ        1.05σ
  223  s1_hi         1.000000      4.10σ       -0.64σ
   19  s0_lo         1.000000      4.02σ       -2.56σ
  166  s1_lo         1.000000      4.00σ       -0.14σ
  128  s1_lo         1.000000      3.95σ       -0.26σ

  Top 10 lowest entropy rows (corridor detection):
  bit  domain     row_entropy    max|z|     H_z(MC)
  ---------------------------------------------------------
   68  s0_hi         1.000000      3.06σ       -2.78σ
  114  s0_hi         1.000000      3.95σ       -2.70σ
   35  s0_lo         1.000000      3.17σ       -2.24σ
    8  s0_lo         1.000000      3.37σ       -2.19σ
  216  s1_hi         1.000000      3.18σ       -2.08σ
  227  s1_hi         1.000000      2.89σ       -2.04σ
  140  s1_lo         1.000000      3.02σ       -1.85σ
  204  s1_hi         1.000000      2.96σ       -1.85σ
  152  s1_lo         1.000000      3.43σ       -1.84σ
   42  s0_lo         1.000000      3.18σ       -1.81σ

  [OK] Heatmap saved → 

  --- VERDICT ---
  Mean row entropy     : 1.000000  (ideal 1.000000)
  Mean col entropy     : 1.000000  (ideal 1.000000)
  [OK] corridor metric below detection threshold at current sample size
[OK] Test B16 finished in 154.41s.

[*] Running test: B22...

[>>>] B22: ROTATIONAL PER-BIT BIAS + CHAIN PERSISTENCE
[>>>] Samples: 200,000,000 | Chain steps: 3
[>>>] Rotations 2x128: [1, 3, 7, 13, 16, 32, 47, 63]
[>>>] Rotations 256:   [1, 7, 13, 32, 64, 96, 128, 192]

  [1/2] 2x128 chain + bias...

  --- 2x128 CHAIN PERSISTENCE (steps=3) ---
  Expected baseline (200M samples):  fail: p96 < 1e-6  |  warn: p104 or p112 < 1e-3
   <112 (-2σ) : 1477.5
   <104 (-3σ) : 0.2
    <96 (-4σ) : 10^-5.7
    <88 (-5σ) : 10^-12.0
    <80 (-6σ) : 10^-19.8

   rot     lt112     lt104      lt96      lt88      lt80  verdict
  -----------------------------------------------------------------
     1      1516         0         0         0         0  [OK]
     3      1453         0         0         0         0  [OK]
     7      1499         0         0         0         0  [OK]
    13      1468         0         0         0         0  [OK]
    16      1516         1         0         0         0  [OK]
    32      1469         0         0         0         0  [OK]
    47      1524         1         0         0         0  [OK]
    63      1438         0         0         0         0  [OK]

  --- 2x128 PER-BIT BIAS (from chain step 1) ---
  EVT per-rot: 3.33σ  |  EVT global: 3.91σ  (8 rot × 256 bits)
   rot    max_z   mean_z     z_ev  worst_bit  verdict
  ---------------------------------------------------------
     1    2.74σ    0.83σ   -1.17σ         27  [OK]
     3    2.88σ    0.80σ   -1.02σ         25  [OK]
     7    2.66σ    0.81σ   -1.24σ        132  [OK]
    13    3.29σ    0.83σ   -0.61σ        201  [OK]
    16    3.10σ    0.74σ   -0.81σ        111  [OK]
    32    2.82σ    0.78σ   -1.09σ         21  [OK]
    47    3.34σ    0.72σ   -0.57σ        219  [OK]
    63    3.00σ    0.82σ   -0.90σ        128  [OK]

  [2/2] 256-bit chain + bias...

  --- 256-BIT CHAIN PERSISTENCE (steps=3) ---
  Expected baseline (200M samples):  fail: p96 < 1e-6  |  warn: p104 or p112 < 1e-3
   <112 (-2σ) : 1477.5
   <104 (-3σ) : 0.2
    <96 (-4σ) : 10^-5.7
    <88 (-5σ) : 10^-12.0
    <80 (-6σ) : 10^-19.8

   rot     lt112     lt104      lt96      lt88      lt80  verdict
  -----------------------------------------------------------------
     1      1478         0         0         0         0  [OK]
     7      1468         0         0         0         0  [OK]
    13      1568         0         0         0         0  [OK]
    32      1465         0         0         0         0  [OK]
    64      1477         0         0         0         0  [OK]
    96      1475         0         0         0         0  [OK]
   128      1556         1         0         0         0  [OK]
   192      1508         0         0         0         0  [OK]

  --- 256-BIT PER-BIT BIAS (from chain step 1) ---
  EVT per-rot: 3.33σ  |  EVT global: 3.91σ  (8 rot × 256 bits)
   rot    max_z   mean_z     z_ev  worst_bit  verdict
  ---------------------------------------------------------
     1    3.07σ    0.80σ   -0.84σ        234  [OK]
     7    2.80σ    0.75σ   -1.11σ          8  [OK]
    13    3.29σ    0.84σ   -0.61σ        178  [OK]
    32    3.67σ    0.76σ   -0.23σ        136  [OK]
    64    2.90σ    0.83σ   -1.00σ         68  [OK]
    96    2.93σ    0.79σ   -0.98σ         48  [OK]
   128    2.88σ    0.77σ   -1.02σ        231  [OK]
   192    2.76σ    0.78σ   -1.14σ        241  [OK]

  --- VERDICT ---
  [OK] no rotational bias at tested rotations
[OK] Test B22 finished in 186.00s.

[*] Running test: B32...

[>>>] B32A: GLOBAL CONVERGENCE TEST
[>>>] Samples: 2,000,000
[>>>] DP bits: 16 | FP bits: 32
[>>>] Max steps: 65,536

  --- RESULTS ---
  Total samples      : 2,000,000
  DP hits            : 1,264,098
  Runaways           : 735,902
  Runaway rate       : 3.679510e-01
  Expected runaway   : 3.678794e-01
  Runaway deviation  : +7.155883e-05

  [FINGERPRINT SPACE]
  Unique fingerprints: 1,263,910
  Collisions         : 188
  Expected           : 186.02
  Z-score            : +0.14σ
  Max bucket         : 2

  [TRAJECTORY STATS]
  Avg steps (all)    : 41431.56
  Avg steps (DP only): 27399.02
  Max steps observed : 65,536

  [ENTROPY]
  Entropy            : 20.2694 bits
  Max entropy        : 20.2697 bits
  Entropy loss       : 0.0003

  --- VERDICT ---
  [OK] fingerprint distribution normal
  [diagnostic] entropy_loss=0.0003  (informational only)
  Runaway z-score    : +0.21σ
  [OK] runaway dynamics match theory

[>>>] B32B: XOR-PROJECTION OCCUPANCY
[>>>] Samples: 10,000,000 | Steps/state: 128 | Buckets: 65,536
[>>>] Projection: upper 16 bits of s0^s1^s2^s3

  --- XOR-PROJECTION OCCUPANCY RESULTS ---
  Total visits         : 1,280,000,000
  Expected per bucket  : 19531.25
  EVT baseline (max z) : 4.71σ
  Max bucket visits    : 20,175  (z=+4.61σ, EV-corr=-0.10σ)
  Chi-square           : 65600.84  (dof=65535, z=+0.18σ)
  Bucket entropy       : 15.999963 / 16.000000 bits
  Entropy loss         : 0.000037
  [OK] XOR-projection uniform — no concentration detected

  [>>>] B32B: XOR-PROJECTION OCCUPANCY
[>>>] Samples: 10,000,000 | Steps/state: 1024 | Buckets: 65,536
[>>>] Projection: upper 16 bits of s0^s1^s2^s3

  --- XOR-PROJECTION OCCUPANCY RESULTS ---
  Total visits         : 10,240,000,000
  Expected per bucket  : 156250.00
  EVT baseline (max z) : 4.71σ
  Max bucket visits    : 157,917  (z=+4.22σ, EV-corr=-0.49σ)
  Chi-square           : 65892.47  (dof=65535, z=+0.99σ)
  Bucket entropy       : 15.999995 / 16.000000 bits
  Entropy loss         : 0.000005
  [OK] XOR-projection uniform — no concentration detected

[>>>] B32C: ORBIT MIXING UNDER ITERATION
[>>>] Samples: 10,000,000 | Steps: 128

  Per-bit density analysis:
  Max |density - 0.5|  : 0.000790  (bit 126, step 4)
  Bit z_raw            : 5.00σ
  Bit z_ev             : +0.44σ  (EVT baseline 4.56σ)

  --- ORBIT MIXING RESULTS ---
  σ(HW mean)           : 0.0025
  σ(word mean)         : 0.0013
  Max |HW - 128| / σ   : 2.15σ  (over 128 steps)
  Max |word - 32| / σ  : 3.85σ

  HW mean by step (first 16 and last 4):
   step   hw_mean       dev        z
  -----------------------------------
      0  127.9994    0.0006     0.23σ
      1  128.0012    0.0012     0.47σ
      2  127.9953    0.0047     1.85σ
      3  128.0032    0.0032     1.27σ
      4  128.0013    0.0013     0.52σ
      5  127.9976    0.0024     0.94σ
      6  127.9953    0.0047     1.84σ
      7  127.9999    0.0001     0.06σ
      8  127.9992    0.0008     0.33σ
      9  127.9953    0.0047     1.86σ
     10  128.0003    0.0003     0.14σ
     11  128.0002    0.0002     0.07σ
     12  127.9990    0.0010     0.39σ
     13  128.0003    0.0003     0.12σ
     14  128.0008    0.0008     0.33σ
     15  128.0009    0.0009     0.34σ
    124  128.0054    0.0054     2.14σ
    125  128.0006    0.0006     0.25σ
    126  128.0011    0.0011     0.45σ
    127  128.0004    0.0004     0.16σ

  Autocorrelation of HW series:
  lag 1  :  +0.054254
  lag 2  :  -0.018507
  lag 3  :  +0.078621
  lag 4  :  +0.060448
  lag 5  :  +0.108305

  [diagnostic] hw_z_ev=-0.96σ  w_z_ev=+0.74σ  bit_z_ev=+0.44σ  (EVT assumes independence — informational only)
  [diagnostic] ac_z=1.23σ  (H0 distribution not derived — autocorrelation informational only)

[>>>] B32C: ORBIT MIXING UNDER ITERATION
[>>>] Samples: 10,000,000 | Steps: 1024

  Per-bit density analysis:
  Max |density - 0.5|  : 0.000790  (bit 126, step 4)
  Bit z_raw            : 5.00σ
  Bit z_ev             : +0.00σ  (EVT baseline 5.00σ)

  --- ORBIT MIXING RESULTS ---
  σ(HW mean)           : 0.0025
  σ(word mean)         : 0.0013
  Max |HW - 128| / σ   : 3.45σ  (over 1024 steps)
  Max |word - 32| / σ  : 4.18σ

  HW mean by step (first 16 and last 4):
   step   hw_mean       dev        z
  -----------------------------------
      0  127.9994    0.0006     0.23σ
      1  128.0012    0.0012     0.47σ
      2  127.9953    0.0047     1.85σ
      3  128.0032    0.0032     1.27σ
      4  128.0013    0.0013     0.52σ
      5  127.9976    0.0024     0.94σ
      6  127.9953    0.0047     1.84σ
      7  127.9999    0.0001     0.06σ
      8  127.9992    0.0008     0.33σ
      9  127.9953    0.0047     1.86σ
     10  128.0003    0.0003     0.14σ
     11  128.0002    0.0002     0.07σ
     12  127.9990    0.0010     0.39σ
     13  128.0003    0.0003     0.12σ
     14  128.0008    0.0008     0.33σ
     15  128.0009    0.0009     0.34σ
   1020  128.0025    0.0025     1.00σ
   1021  127.9995    0.0005     0.19σ
   1022  127.9980    0.0020     0.77σ
   1023  127.9982    0.0018     0.72σ

  Autocorrelation of HW series:
  lag 1  :  -0.010595
  lag 2  :  -0.034505
  lag 3  :  +0.002003
  lag 4  :  -0.000331
  lag 5  :  -0.003652

  [diagnostic] hw_z_ev=-0.27σ  w_z_ev=+0.46σ  bit_z_ev=+0.00σ  (EVT assumes independence — informational only)
  [diagnostic] ac_z=1.10σ  (H0 distribution not derived — autocorrelation informational only)

[>>>] B32D: ORBIT FINGERPRINT RECURRENCE
[>>>] Samples: 2,000,000 | Max orbit: 8,192 | FP bits: 32
  Building H0 baseline (50,000 simulated orbits, Rust)...

  --- H0 BASELINE (uniform iid fp(t), Rust, n=50,000) ---
  FP space             : 2^32 = 4,294,967,296
  H0 recur. rate       : 7.960000e-03  (n=50,000 orbits)
  H0 mean gap          : 2746.96  (conditional on recurrence)
  E[first recurrence]  : 8.21e+04 steps  (birthday paradox reference, absolute t2 — not used in verdict)

  --- ORBIT FINGERPRINT RECURRENCE RESULTS ---
  States sampled       : 2,000,000
  Recurrences found    : 15,690  (0.7845%)
  H0 expected rate     : 0.7960%  (z=-0.29σ)
  No recurrence        : 1,984,310  (orbit > 8,192)
  Min recurrence dist  : 1
  Max recurrence dist  : 8,114
  Mean recurrence dist : 2705.58  (conditional on recurrence found)
  Median recur. dist   : 2346.00

  Recurrence gap distribution  (H0 baseline from Rust simulation):
  range                      obs    obs_frac     h0_frac    ratio
  --------------------------------------------------------------
  [1, 2)                       4    0.000002    0.000000      nan
  [2, 4)                      11    0.000005    0.000000      nan
  [4, 8)                      13    0.000006    0.000000      nan
  [8, 16)                     30    0.000015    0.000000      nan
  [16, 32)                    57    0.000029    0.000020     1.43
  [32, 64)                   124    0.000062    0.000060     1.03
  [64, 128)                  245    0.000122    0.000120     1.02
  [128, 256)                 470    0.000235    0.000260     0.90
  [256, 512)               1,015    0.000508    0.000440     1.15
  [512, 1024)              1,737    0.000869    0.001080     0.80
  [1024, 8193)            11,984    0.005992    0.005980     1.00

  Adjacent-step FP collisions (distance=1)  [diagnostic only]:
  Observed             : 4
  FP collisions        : 0  (unique=15,690 / total=15,690)

  [OK] FP recurrence consistent with H0 baseline

[>>>] B32D: ORBIT FINGERPRINT RECURRENCE
[>>>] Samples: 4,000,000 | Max orbit: 8,192 | FP bits: 32
  Building H0 baseline (50,000 simulated orbits, Rust)...

  --- H0 BASELINE (uniform iid fp(t), Rust, n=50,000) ---
  FP space             : 2^32 = 4,294,967,296
  H0 recur. rate       : 7.960000e-03  (n=50,000 orbits)
  H0 mean gap          : 2746.96  (conditional on recurrence)
  E[first recurrence]  : 8.21e+04 steps  (birthday paradox reference, absolute t2 — not used in verdict)

  --- ORBIT FINGERPRINT RECURRENCE RESULTS ---
  States sampled       : 4,000,000
  Recurrences found    : 31,046  (0.7762%)
  H0 expected rate     : 0.7960%  (z=-0.50σ)
  No recurrence        : 3,968,954  (orbit > 8,192)
  Min recurrence dist  : 1
  Max recurrence dist  : 8,114
  Mean recurrence dist : 2724.95  (conditional on recurrence found)
  Median recur. dist   : 2378.50

  Recurrence gap distribution  (H0 baseline from Rust simulation):
  range                      obs    obs_frac     h0_frac    ratio
  --------------------------------------------------------------
  [1, 2)                       4    0.000001    0.000000      nan
  [2, 4)                      23    0.000006    0.000000      nan
  [4, 8)                      30    0.000008    0.000000      nan
  [8, 16)                     51    0.000013    0.000000      nan
  [16, 32)                   113    0.000028    0.000020     1.41
  [32, 64)                   238    0.000060    0.000060     0.99
  [64, 128)                  479    0.000120    0.000120     1.00
  [128, 256)                 964    0.000241    0.000260     0.93
  [256, 512)               1,978    0.000495    0.000440     1.12
  [512, 1024)              3,377    0.000844    0.001080     0.78
  [1024, 8193)            23,789    0.005947    0.005980     0.99

  Adjacent-step FP collisions (distance=1)  [diagnostic only]:
  Observed             : 4
  FP collisions        : 0  (unique=31,046 / total=31,046)

  [OK] FP recurrence consistent with H0 baseline

[>>>] B32D: ORBIT FINGERPRINT RECURRENCE
[>>>] Samples: 4,000,000 | Max orbit: 65,536 | FP bits: 32
  Building H0 baseline (50,000 simulated orbits, Rust)...

  --- H0 BASELINE (uniform iid fp(t), Rust, n=50,000) ---
  FP space             : 2^32 = 4,294,967,296
  H0 recur. rate       : 3.912800e-01  (n=50,000 orbits)
  H0 mean gap          : 20678.37  (conditional on recurrence)
  E[first recurrence]  : 8.21e+04 steps  (birthday paradox reference, absolute t2 — not used in verdict)

  --- ORBIT FINGERPRINT RECURRENCE RESULTS ---
  States sampled       : 4,000,000
  Recurrences found    : 1,574,337  (39.3584%)
  H0 expected rate     : 39.1280%  (z=+1.05σ)
  No recurrence        : 2,425,663  (orbit > 65,536)
  Min recurrence dist  : 1
  Max recurrence dist  : 65,519
  Mean recurrence dist : 20736.35  (conditional on recurrence found)
  Median recur. dist   : 17912.00

  Recurrence gap distribution  (H0 baseline from Rust simulation):
  range                      obs    obs_frac     h0_frac    ratio
  --------------------------------------------------------------
  [1, 2)                      52    0.000013    0.000000      nan
  [2, 4)                     118    0.000029    0.000000      nan
  [4, 8)                     198    0.000049    0.000020     2.47
  [8, 16)                    401    0.000100    0.000080     1.25
  [16, 32)                   887    0.000222    0.000200     1.11
  [32, 64)                 1,660    0.000415    0.000380     1.09
  [64, 128)                3,372    0.000843    0.000900     0.94
  [128, 256)               6,773    0.001693    0.001360     1.25
  [256, 512)              13,507    0.003377    0.003180     1.06
  [512, 1024)             26,094    0.006523    0.006740     0.97
  [1024, 65537)         1,521,275    0.380319    0.378420     1.01

  Adjacent-step FP collisions (distance=1)  [diagnostic only]:
  Observed             : 52
  FP collisions        : 285  (unique=1,574,052 / total=1,574,337)

  [OK] FP recurrence consistent with H0 baseline

[>>>] B32E: STATE-SPACE PROFILE
[>>>] Samples: 10,000,000 | Checkpoints: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 4096]
[>>>] Windows: 16 | Buckets/window: 65,536
[>>>] λ = N/K = 152.59 | MM bias = 0.004727

  --- MILLER-MADOW FINITE-SAMPLE BASELINE ---
  Theoretical MM bias  : 0.004727
  Observed range       : 0.004724 .. 0.004741
  Deviation from MM    : -3.47e-06 .. +1.41e-05

  --- ENTROPY LOSS PER CHECKPOINT (mean ± std over 16 windows) ---
    checkpoint       mean_el      std_el   max_bkt_zev    occupied  verdict
  ----------------------------------------------------------------------------
             1      0.004733    2.64e-05         +0.59σ     65536.0  [OK]
             2      0.004737    2.68e-05         +0.34σ     65536.0  [OK]
             4      0.004738    2.25e-05         +0.18σ     65536.0  [OK]
             8      0.004724    2.44e-05         +0.59σ     65536.0  [OK]
            16      0.004735    3.83e-05         +0.18σ     65536.0  [OK]
            32      0.004737    2.34e-05         +0.50σ     65536.0  [OK]
            64      0.004741    2.59e-05         +0.59σ     65536.0  [OK]
           128      0.004724    2.47e-05         +0.26σ     65536.0  [OK]
           256      0.004728    2.57e-05         +0.10σ     65536.0  [OK]
           512      0.004733    2.23e-05         +0.26σ     65536.0  [OK]
          1024      0.004731    2.05e-05         +0.42σ     65536.0  [OK]
          4096      0.004726    1.90e-05         +0.75σ     65536.0  [OK]

  --- DELTA ENTROPY LOSS ---
  Δ entropy_loss (cp4096 - cp1) : -0.000006
  max - min across checkpoints  : 0.000018

  --- GLOBAL MAX BUCKET ---
  Global max occupancy : 220  (z=+5.46σ, EV-corr=+0.75σ)
  Expected λ           : 152.59
  Expected occupied    : 65536.0 / 65,536

  --- FANO FACTOR (Var/Mean, ideal = 1.0) ---
    checkpoint     mean_fano      max_fano  [diagnostic only]
  --------------------------------------------------
             1      1.000050      1.008918
             2      1.000844      1.012763
             4      1.001302      1.009062
             8      0.998195      1.007289
            16      1.000526      1.021336
            32      1.000780      1.009238
            64      1.001851      1.011903
           128      0.998108      1.008068
           256      0.999158      1.011206
           512      0.999969      1.006546
          1024      0.999616      1.006330
          4096      0.998719      1.004727

  --- OCCUPANCY SPECTRUM — worst (cp=4096, window=2) ---
  Entropy loss         : 0.004675
  Fano factor          : 0.988127
  λ = 152.6  σ = 12.4  spectrum around mode:
       k    observed  gauss_exp         z        k    observed  gauss_exp         z        k    observed  gauss_exp         z
  ---------------------------------------   ---------------------------------------   ---------------------------------------
     140       1,328     1259.3    +1.94σ      149       2,073     2029.1    +0.97σ      158       1,914     1922.9    -0.20σ
     141       1,401     1363.1    +1.03σ      150       2,102     2070.6    +0.69σ      159       1,750     1849.8    -2.32σ
     142       1,475     1465.9    +0.24σ      151       2,168     2099.1    +1.50σ      160       1,717     1767.9    -1.21σ
     143       1,616     1566.1    +1.26σ      152       2,085     2114.2    -0.63σ      161       1,577     1678.5    -2.48σ
     144       1,731     1662.2    +1.69σ      153       2,147     2115.4    +0.69σ      162       1,565     1583.3    -0.46σ
     145       1,733     1752.6    -0.47σ      154       2,128     2102.8    +0.55σ      163       1,444     1483.7    -1.03σ
     146       1,907     1836.0    +1.66σ      155       2,109     2076.6    +0.71σ      164       1,363     1381.3    -0.49σ
     147       1,989     1910.7    +1.79σ      156       2,007     2037.3    -0.67σ
     148       1,955     1975.5    -0.46σ      157       1,963     1985.8    -0.51σ
  p99.9  : 192.0  |  p99.99 : 197.4

  --- TREND ANALYSIS (Spearman: log2(cp) vs mean_entropy_loss) ---
  Spearman r           : -0.4615
  p-value              : 0.1309
  [OK] no systematic entropy loss trend

  --- VERDICT ---
  [OK] entropy loss consistent with Miller-Madow finite-sample baseline
  [OK] no concentration trend detected

[>>>] B32E: STATE-SPACE PROFILE
[>>>] Samples: 10,000,000 | Checkpoints: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 4096, 8192, 16384, 32768, 65536]
[>>>] Windows: 16 | Buckets/window: 65,536
[>>>] λ = N/K = 152.59 | MM bias = 0.004727

  --- MILLER-MADOW FINITE-SAMPLE BASELINE ---
  Theoretical MM bias  : 0.004727
  Observed range       : 0.004709 .. 0.004741
  Deviation from MM    : -1.81e-05 .. +1.41e-05

  --- ENTROPY LOSS PER CHECKPOINT (mean ± std over 16 windows) ---
    checkpoint       mean_el      std_el   max_bkt_zev    occupied  verdict
  ----------------------------------------------------------------------------
             1      0.004733    2.64e-05         +0.59σ     65536.0  [OK]
             2      0.004737    2.68e-05         +0.34σ     65536.0  [OK]
             4      0.004738    2.25e-05         +0.18σ     65536.0  [OK]
             8      0.004724    2.44e-05         +0.59σ     65536.0  [OK]
            16      0.004735    3.83e-05         +0.18σ     65536.0  [OK]
            32      0.004737    2.34e-05         +0.50σ     65536.0  [OK]
            64      0.004741    2.59e-05         +0.59σ     65536.0  [OK]
           128      0.004724    2.47e-05         +0.26σ     65536.0  [OK]
           256      0.004728    2.57e-05         +0.10σ     65536.0  [OK]
           512      0.004733    2.23e-05         +0.26σ     65536.0  [OK]
          1024      0.004731    2.05e-05         +0.42σ     65536.0  [OK]
          4096      0.004726    1.90e-05         +0.75σ     65536.0  [OK]
          8192      0.004709    3.20e-05         +0.75σ     65536.0  [OK]
         16384      0.004732    2.68e-05         +0.59σ     65536.0  [OK]
         32768      0.004721    2.08e-05         +0.34σ     65536.0  [OK]
         65536      0.004724    3.05e-05         +0.02σ     65536.0  [OK]

  --- DELTA ENTROPY LOSS ---
  Δ entropy_loss (cp4096 - cp1) : -0.000009
  max - min across checkpoints  : 0.000032

  --- GLOBAL MAX BUCKET ---
  Global max occupancy : 220  (z=+5.46σ, EV-corr=+0.75σ)
  Expected λ           : 152.59
  Expected occupied    : 65536.0 / 65,536

  --- FANO FACTOR (Var/Mean, ideal = 1.0) ---
    checkpoint     mean_fano      max_fano  [diagnostic only]
  --------------------------------------------------
             1      1.000050      1.008918
             2      1.000844      1.012763
             4      1.001302      1.009062
             8      0.998195      1.007289
            16      1.000526      1.021336
            32      1.000780      1.009238
            64      1.001851      1.011903
           128      0.998108      1.008068
           256      0.999158      1.011206
           512      0.999969      1.006546
          1024      0.999616      1.006330
          4096      0.998719      1.004727
          8192      0.994982      1.009802
         16384      0.999895      1.013988
         32768      0.997701      1.005557
         65536      0.998212      1.010078

  --- OCCUPANCY SPECTRUM — worst (cp=4096, window=2) ---
  Entropy loss         : 0.004675
  Fano factor          : 0.988127
  λ = 152.6  σ = 12.4  spectrum around mode:
       k    observed  gauss_exp         z        k    observed  gauss_exp         z        k    observed  gauss_exp         z
  ---------------------------------------   ---------------------------------------   ---------------------------------------
     140       1,328     1259.3    +1.94σ      149       2,073     2029.1    +0.97σ      158       1,914     1922.9    -0.20σ
     141       1,401     1363.1    +1.03σ      150       2,102     2070.6    +0.69σ      159       1,750     1849.8    -2.32σ
     142       1,475     1465.9    +0.24σ      151       2,168     2099.1    +1.50σ      160       1,717     1767.9    -1.21σ
     143       1,616     1566.1    +1.26σ      152       2,085     2114.2    -0.63σ      161       1,577     1678.5    -2.48σ
     144       1,731     1662.2    +1.69σ      153       2,147     2115.4    +0.69σ      162       1,565     1583.3    -0.46σ
     145       1,733     1752.6    -0.47σ      154       2,128     2102.8    +0.55σ      163       1,444     1483.7    -1.03σ
     146       1,907     1836.0    +1.66σ      155       2,109     2076.6    +0.71σ      164       1,363     1381.3    -0.49σ
     147       1,989     1910.7    +1.79σ      156       2,007     2037.3    -0.67σ
     148       1,955     1975.5    -0.46σ      157       1,963     1985.8    -0.51σ
  p99.9  : 192.0  |  p99.99 : 197.4

  --- TREND ANALYSIS (Spearman: log2(cp) vs mean_entropy_loss) ---
  Spearman r           : -0.6529
  p-value              : 0.0061
  [OK] no systematic entropy loss trend

  --- VERDICT ---
  [OK] entropy loss consistent with Miller-Madow finite-sample baseline
  [OK] no concentration trend detected

[>>>] B32E: STATE-SPACE PROFILE
[>>>] Samples: 10,000,000 | Checkpoints: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 4096, 8192, 16384, 32768, 65536]
[>>>] Windows: 32 | Buckets/window: 256
[>>>] λ = N/K = 39062.50 | MM bias = 0.000018

  --- MILLER-MADOW FINITE-SAMPLE BASELINE ---
  Theoretical MM bias  : 0.000018
  Observed range       : 0.000018 .. 0.000019
  Deviation from MM    : -4.13e-07 .. +5.07e-07

  --- ENTROPY LOSS PER CHECKPOINT (mean ± std over 32 windows) ---
    checkpoint       mean_el      std_el   max_bkt_zev    occupied  verdict
  ----------------------------------------------------------------------------
             1      0.000018    1.67e-06         +0.97σ       256.0  [OK]
             2      0.000019    1.41e-06         +0.35σ       256.0  [OK]
             4      0.000018    1.19e-06         +0.03σ       256.0  [OK]
             8      0.000018    1.10e-06         +0.54σ       256.0  [OK]
            16      0.000019    1.36e-06         +0.54σ       256.0  [OK]
            32      0.000018    1.64e-06         +1.26σ       256.0  [OK]
            64      0.000018    1.95e-06         +0.48σ       256.0  [OK]
           128      0.000018    1.37e-06         +0.83σ       256.0  [OK]
           256      0.000018    1.62e-06         +0.51σ       256.0  [OK]
           512      0.000019    1.69e-06         +0.48σ       256.0  [OK]
          1024      0.000018    1.09e-06         +0.34σ       256.0  [OK]
          4096      0.000019    1.73e-06         +0.65σ       256.0  [OK]
          8192      0.000018    1.27e-06         +0.99σ       256.0  [OK]
         16384      0.000018    1.59e-06         +0.25σ       256.0  [OK]
         32768      0.000019    1.39e-06         -0.02σ       256.0  [OK]
         65536      0.000019    1.91e-06         +0.58σ       256.0  [OK]

  --- DELTA ENTROPY LOSS ---
  Δ entropy_loss (cp4096 - cp1) : +0.000001
  max - min across checkpoints  : 0.000001

  --- GLOBAL MAX BUCKET ---
  Global max occupancy : 39,970  (z=+4.59σ, EV-corr=+1.26σ)
  Expected λ           : 39062.50
  Expected occupied    : 256.0 / 256

  --- FANO FACTOR (Var/Mean, ideal = 1.0) ---
    checkpoint     mean_fano      max_fano  [diagnostic only]
  --------------------------------------------------
             1      0.989194      1.189375
             2      1.014297      1.185648
             4      0.981592      1.100891
             8      0.984179      1.107490
            16      1.010812      1.170511
            32      0.982516      1.174576
            64      0.987107      1.203268
           128      0.993501      1.187768
           256      0.992326      1.267915
           512      1.015322      1.174448
          1024      0.989190      1.136647
          4096      1.011362      1.293660
          8192      0.973727      1.113784
         16384      0.975335      1.135062
         32768      1.010315      1.187661
         65536      1.023483      1.207073

  --- OCCUPANCY SPECTRUM — worst (cp=32, window=16) ---
  Entropy loss         : 0.000017
  Fano factor          : 0.897472
  λ = 39062.5  σ = 197.6  spectrum around mode:
       k    observed  gauss_exp         z        k    observed  gauss_exp         z        k    observed  gauss_exp         z
  ---------------------------------------   ---------------------------------------   ---------------------------------------
   38864           0        0.3    -0.31σ    38997           1        0.5    +0.51σ    39130           0        0.5    -0.49σ
   38865           0        0.3    -0.31σ    38998           0        0.5    -0.49σ    39131           2        0.5    +1.51σ
   38866           0        0.3    -0.32σ    38999           1        0.5    +0.51σ    39132           0        0.5    -0.49σ
   38867           0        0.3    -0.32σ    39000           0        0.5    -0.49σ    39133           0        0.5    -0.48σ
   38868           1        0.3    +0.68σ    39001           0        0.5    -0.49σ    39134           2        0.5    +1.52σ
   38869           0        0.3    -0.32σ    39002           2        0.5    +1.51σ    39135           0        0.5    -0.48σ
   38870           0        0.3    -0.32σ    39003           2        0.5    +1.51σ    39136           1        0.5    +0.52σ
   38871           0        0.3    -0.32σ    39004           2        0.5    +1.51σ    39137           0        0.5    -0.48σ
   38872           0        0.3    -0.32σ    39005           0        0.5    -0.50σ    39138           1        0.5    +0.52σ
   38873           0        0.3    -0.33σ    39006           1        0.5    +0.50σ    39139           0        0.5    -0.48σ
   38874           1        0.3    +0.67σ    39007           2        0.5    +1.50σ    39140           0        0.5    -0.48σ
   38875           0        0.3    -0.33σ    39008           0        0.5    -0.50σ    39141           0        0.5    -0.48σ
   38876           2        0.3    +1.67σ    39009           0        0.5    -0.50σ    39142           0        0.5    -0.48σ
   38877           1        0.3    +0.67σ    39010           1        0.5    +0.50σ    39143           3        0.5    +2.52σ
   38878           0        0.3    -0.33σ    39011           1        0.5    +0.50σ    39144           0        0.5    -0.47σ
   38879           2        0.3    +1.66σ    39012           1        0.5    +0.50σ    39145           0        0.5    -0.47σ
   38880           1        0.3    +0.66σ    39013           1        0.5    +0.50σ    39146           1        0.5    +0.53σ
   38881           1        0.3    +0.66σ    39014           0        0.5    -0.50σ    39147           0        0.5    -0.47σ
   38882           1        0.3    +0.66σ    39015           0        0.5    -0.50σ    39148           0        0.5    -0.47σ
   38883           0        0.3    -0.34σ    39016           1        0.5    +0.50σ    39149           0        0.5    -0.47σ
   38884           1        0.3    +0.66σ    39017           2        0.5    +1.50σ    39150           0        0.5    -0.47σ
   38885           0        0.3    -0.35σ    39018           1        0.5    +0.50σ    39151           0        0.5    -0.47σ
   38886           0        0.3    -0.35σ    39019           0        0.5    -0.50σ    39152           0        0.5    -0.47σ
   38887           0        0.3    -0.35σ    39020           0        0.5    -0.50σ    39153           1        0.5    +0.53σ
   38888           0        0.3    -0.35σ    39021           1        0.5    +0.49σ    39154           0        0.5    -0.46σ
   38889           0        0.4    -0.35σ    39022           1        0.5    +0.49σ    39155           1        0.5    +0.54σ
   38890           0        0.4    -0.35σ    39023           2        0.5    +1.49σ    39156           0        0.5    -0.46σ
   38891           0        0.4    -0.35σ    39024           1        0.5    +0.49σ    39157           1        0.5    +0.54σ
   38892           1        0.4    +0.64σ    39025           1        0.5    +0.49σ    39158           0        0.5    -0.46σ
   38893           0        0.4    -0.36σ    39026           1        0.5    +0.49σ    39159           1        0.5    +0.54σ
   38894           0        0.4    -0.36σ    39027           0        0.5    -0.51σ    39160           0        0.5    -0.46σ
   38895           0        0.4    -0.36σ    39028           1        0.5    +0.49σ    39161           0        0.5    -0.46σ
   38896           1        0.4    +0.64σ    39029           0        0.5    -0.51σ    39162           2        0.5    +1.54σ
   38897           0        0.4    -0.36σ    39030           0        0.5    -0.51σ    39163           0        0.5    -0.45σ
   38898           0        0.4    -0.37σ    39031           1        0.5    +0.49σ    39164           0        0.5    -0.45σ
   38899           1        0.4    +0.63σ    39032           0        0.5    -0.51σ    39165           0        0.5    -0.45σ
   38900           2        0.4    +1.63σ    39033           1        0.5    +0.49σ    39166           0        0.5    -0.45σ
   38901           0        0.4    -0.37σ    39034           0        0.5    -0.51σ    39167           1        0.4    +0.55σ
   38902           1        0.4    +0.63σ    39035           1        0.5    +0.49σ    39168           1        0.4    +0.55σ
   38903           1        0.4    +0.63σ    39036           0        0.5    -0.51σ    39169           3        0.4    +2.55σ
   38904           1        0.4    +0.63σ    39037           1        0.5    +0.49σ    39170           0        0.4    -0.45σ
   38905           1        0.4    +0.62σ    39038           0        0.5    -0.51σ    39171           1        0.4    +0.56σ
   38906           0        0.4    -0.38σ    39039           1        0.5    +0.49σ    39172           1        0.4    +0.56σ
   38907           0        0.4    -0.38σ    39040           0        0.5    -0.51σ    39173           1        0.4    +0.56σ
   38908           1        0.4    +0.62σ    39041           0        0.5    -0.51σ    39174           0        0.4    -0.44σ
   38909           0        0.4    -0.38σ    39042           0        0.5    -0.51σ    39175           0        0.4    -0.44σ
   38910           2        0.4    +1.62σ    39043           1        0.5    +0.49σ    39176           0        0.4    -0.44σ
   38911           0        0.4    -0.39σ    39044           0        0.5    -0.51σ    39177           0        0.4    -0.44σ
   38912           0        0.4    -0.39σ    39045           2        0.5    +1.49σ    39178           2        0.4    +1.56σ
   38913           0        0.4    -0.39σ    39046           0        0.5    -0.51σ    39179           0        0.4    -0.43σ
   38914           0        0.4    -0.39σ    39047           0        0.5    -0.52σ    39180           0        0.4    -0.43σ
   38915           0        0.4    -0.39σ    39048           0        0.5    -0.52σ    39181           0        0.4    -0.43σ
   38916           1        0.4    +0.61σ    39049           0        0.5    -0.52σ    39182           1        0.4    +0.57σ
   38917           0        0.4    -0.39σ    39050           0        0.5    -0.52σ    39183           1        0.4    +0.57σ
   38918           1        0.4    +0.60σ    39051           0        0.5    -0.52σ    39184           0        0.4    -0.43σ
   38919           1        0.4    +0.60σ    39052           1        0.5    +0.48σ    39185           1        0.4    +0.57σ
   38920           1        0.4    +0.60σ    39053           0        0.5    -0.52σ    39186           1        0.4    +0.57σ
   38921           1        0.4    +0.60σ    39054           0        0.5    -0.52σ    39187           0        0.4    -0.42σ
   38922           1        0.4    +0.60σ    39055           1        0.5    +0.48σ    39188           0        0.4    -0.42σ
   38923           0        0.4    -0.40σ    39056           1        0.5    +0.48σ    39189           1        0.4    +0.58σ
   38924           0        0.4    -0.40σ    39057           0        0.5    -0.52σ    39190           1        0.4    +0.58σ
   38925           2        0.4    +1.59σ    39058           0        0.5    -0.52σ    39191           1        0.4    +0.58σ
   38926           1        0.4    +0.59σ    39059           0        0.5    -0.52σ    39192           0        0.4    -0.42σ
   38927           0        0.4    -0.41σ    39060           2        0.5    +1.48σ    39193           0        0.4    -0.42σ
   38928           0        0.4    -0.41σ    39061           0        0.5    -0.52σ    39194           1        0.4    +0.59σ
   38929           0        0.4    -0.41σ    39062           2        0.5    +1.48σ    39195           0        0.4    -0.41σ
   38930           3        0.4    +2.59σ    39063           0        0.5    -0.52σ    39196           1        0.4    +0.59σ
   38931           1        0.4    +0.59σ    39064           0        0.5    -0.52σ    39197           1        0.4    +0.59σ
   38932           0        0.4    -0.42σ    39065           0        0.5    -0.52σ    39198           1        0.4    +0.59σ
   38933           1        0.4    +0.58σ    39066           0        0.5    -0.52σ    39199           0        0.4    -0.41σ
   38934           0        0.4    -0.42σ    39067           1        0.5    +0.48σ    39200           0        0.4    -0.41σ
   38935           1        0.4    +0.58σ    39068           0        0.5    -0.52σ    39201           1        0.4    +0.60σ
   38936           1        0.4    +0.58σ    39069           0        0.5    -0.52σ    39202           0        0.4    -0.40σ
   38937           0        0.4    -0.42σ    39070           1        0.5    +0.48σ    39203           0        0.4    -0.40σ
   38938           2        0.4    +1.58σ    39071           0        0.5    -0.52σ    39204           1        0.4    +0.60σ
   38939           0        0.4    -0.43σ    39072           0        0.5    -0.52σ    39205           0        0.4    -0.40σ
   38940           0        0.4    -0.43σ    39073           2        0.5    +1.48σ    39206           0        0.4    -0.40σ
   38941           1        0.4    +0.57σ    39074           1        0.5    +0.48σ    39207           0        0.4    -0.40σ
   38942           0        0.4    -0.43σ    39075           1        0.5    +0.48σ    39208           1        0.4    +0.61σ
   38943           3        0.4    +2.57σ    39076           0        0.5    -0.52σ    39209           0        0.4    -0.39σ
   38944           0        0.4    -0.43σ    39077           0        0.5    -0.52σ    39210           1        0.4    +0.61σ
   38945           0        0.4    -0.43σ    39078           0        0.5    -0.52σ    39211           1        0.4    +0.61σ
   38946           0        0.4    -0.43σ    39079           1        0.5    +0.49σ    39212           0        0.4    -0.39σ
   38947           0        0.4    -0.44σ    39080           1        0.5    +0.49σ    39213           1        0.4    +0.61σ
   38948           1        0.4    +0.56σ    39081           0        0.5    -0.51σ    39214           0        0.4    -0.39σ
   38949           0        0.4    -0.44σ    39082           2        0.5    +1.49σ    39215           0        0.4    -0.38σ
   38950           0        0.4    -0.44σ    39083           1        0.5    +0.49σ    39216           0        0.4    -0.38σ
   38951           1        0.4    +0.56σ    39084           0        0.5    -0.51σ    39217           2        0.4    +1.62σ
   38952           2        0.4    +1.56σ    39085           0        0.5    -0.51σ    39218           2        0.4    +1.62σ
   38953           0        0.4    -0.44σ    39086           0        0.5    -0.51σ    39219           0        0.4    -0.38σ
   38954           0        0.4    -0.44σ    39087           0        0.5    -0.51σ    39220           0        0.4    -0.38σ
   38955           0        0.4    -0.45σ    39088           1        0.5    +0.49σ    39221           0        0.4    -0.37σ
   38956           0        0.4    -0.45σ    39089           0        0.5    -0.51σ    39222           0        0.4    -0.37σ
   38957           0        0.4    -0.45σ    39090           0        0.5    -0.51σ    39223           0        0.4    -0.37σ
   38958           0        0.4    -0.45σ    39091           0        0.5    -0.51σ    39224           2        0.4    +1.63σ
   38959           0        0.5    -0.45σ    39092           0        0.5    -0.51σ    39225           0        0.4    -0.37σ
   38960           0        0.5    -0.45σ    39093           0        0.5    -0.51σ    39226           0        0.4    -0.37σ
   38961           2        0.5    +1.55σ    39094           0        0.5    -0.51σ    39227           0        0.4    -0.37σ
   38962           0        0.5    -0.45σ    39095           1        0.5    +0.49σ    39228           0        0.4    -0.36σ
   38963           0        0.5    -0.46σ    39096           0        0.5    -0.51σ    39229           0        0.4    -0.36σ
   38964           0        0.5    -0.46σ    39097           0        0.5    -0.51σ    39230           0        0.4    -0.36σ
   38965           0        0.5    -0.46σ    39098           1        0.5    +0.49σ    39231           1        0.4    +0.64σ
   38966           1        0.5    +0.54σ    39099           1        0.5    +0.49σ    39232           0        0.4    -0.36σ
   38967           0        0.5    -0.46σ    39100           0        0.5    -0.51σ    39233           0        0.4    -0.36σ
   38968           2        0.5    +1.54σ    39101           1        0.5    +0.49σ    39234           0        0.4    -0.35σ
   38969           0        0.5    -0.46σ    39102           0        0.5    -0.51σ    39235           0        0.4    -0.35σ
   38970           0        0.5    -0.46σ    39103           1        0.5    +0.49σ    39236           0        0.4    -0.35σ
   38971           0        0.5    -0.46σ    39104           0        0.5    -0.51σ    39237           2        0.3    +1.65σ
   38972           0        0.5    -0.47σ    39105           0        0.5    -0.50σ    39238           1        0.3    +0.65σ
   38973           0        0.5    -0.47σ    39106           0        0.5    -0.50σ    39239           0        0.3    -0.35σ
   38974           0        0.5    -0.47σ    39107           0        0.5    -0.50σ    39240           0        0.3    -0.35σ
   38975           0        0.5    -0.47σ    39108           0        0.5    -0.50σ    39241           0        0.3    -0.34σ
   38976           0        0.5    -0.47σ    39109           0        0.5    -0.50σ    39242           0        0.3    -0.34σ
   38977           0        0.5    -0.47σ    39110           0        0.5    -0.50σ    39243           0        0.3    -0.34σ
   38978           0        0.5    -0.47σ    39111           0        0.5    -0.50σ    39244           0        0.3    -0.34σ
   38979           1        0.5    +0.53σ    39112           1        0.5    +0.50σ    39245           0        0.3    -0.34σ
   38980           0        0.5    -0.47σ    39113           0        0.5    -0.50σ    39246           0        0.3    -0.34σ
   38981           0        0.5    -0.47σ    39114           0        0.5    -0.50σ    39247           0        0.3    -0.33σ
   38982           0        0.5    -0.48σ    39115           2        0.5    +1.50σ    39248           1        0.3    +0.67σ
   38983           0        0.5    -0.48σ    39116           2        0.5    +1.50σ    39249           0        0.3    -0.33σ
   38984           0        0.5    -0.48σ    39117           0        0.5    -0.50σ    39250           1        0.3    +0.67σ
   38985           0        0.5    -0.48σ    39118           1        0.5    +0.50σ    39251           0        0.3    -0.33σ
   38986           0        0.5    -0.48σ    39119           0        0.5    -0.50σ    39252           1        0.3    +0.67σ
   38987           1        0.5    +0.52σ    39120           0        0.5    -0.50σ    39253           0        0.3    -0.32σ
   38988           2        0.5    +1.52σ    39121           0        0.5    -0.49σ    39254           1        0.3    +0.68σ
   38989           1        0.5    +0.52σ    39122           0        0.5    -0.49σ    39255           0        0.3    -0.32σ
   38990           1        0.5    +0.52σ    39123           1        0.5    +0.51σ    39256           0        0.3    -0.32σ
   38991           0        0.5    -0.48σ    39124           0        0.5    -0.49σ    39257           0        0.3    -0.32σ
   38992           0        0.5    -0.48σ    39125           1        0.5    +0.51σ    39258           1        0.3    +0.68σ
   38993           1        0.5    +0.51σ    39126           1        0.5    +0.51σ    39259           0        0.3    -0.32σ
   38994           2        0.5    +1.51σ    39127           0        0.5    -0.49σ    39260           1        0.3    +0.69σ
   38995           0        0.5    -0.49σ    39128           2        0.5    +1.51σ
   38996           0        0.5    -0.49σ    39129           1        0.5    +0.51σ
  p99.9  : 39852.7  |  p99.99 : 39958.3

  --- TREND ANALYSIS (Spearman: log2(cp) vs mean_entropy_loss) ---
  Spearman r           : +0.1206
  p-value              : 0.6564
  [OK] no systematic entropy loss trend

  --- VERDICT ---
  [OK] entropy loss consistent with Miller-Madow finite-sample baseline
  [OK] no concentration trend detected

[>>>] B32F: NEAR-NEIGHBOUR DISTANCE RETENTION
[>>>] Pairs: 102,400 | Max steps: 4,096
[>>>] Checkpoints: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 4096]
[>>>] H0 reference: HD ~ Binomial(256, 0.5)  μ=128.0  σ=8.0

  --- HD PER CHECKPOINT ---
  H0 analytic tails (Binomial(256,0.5), approximate baseline):
  P(HD<8)=1.17e-64  P(HD<16)=6.16e-54  P(HD<32)=8.28e-38  P(HD<64)=8.04e-17
  P(HD<96)=0.0000  P(HD<104)=0.0011  P(HD<112)=0.0195

      cp     mean     std   p01   p05   med   p95   p99        P<96       P<104       P<112    z_mean
  ------------------------------------------------------------------------------------------------
       1  127.987   8.020   109   115   128   141   147      0.0000      0.0011      0.0199     -0.50σ
       2  127.999   8.014   109   115   128   141   147      0.0000      0.0012      0.0197     -0.03σ
       4  127.972   7.956   109   115   128   141   146      0.0000      0.0011      0.0191     -1.12σ
       8  127.994   7.978   110   115   128   141   147      0.0000      0.0009      0.0187     -0.24σ
      16  128.003   8.021   109   115   128   141   147      0.0000      0.0014      0.0200     +0.11σ
      32  127.986   8.008   109   115   128   141   147      0.0000      0.0011      0.0191     -0.58σ
      64  128.019   7.988   110   115   128   141   147      0.0000      0.0010      0.0186     +0.77σ
     128  128.014   8.001   110   115   128   141   147      0.0000      0.0011      0.0187     +0.57σ
     256  128.002   7.996   110   115   128   141   147      0.0000      0.0010      0.0190     +0.10σ
     512  128.001   8.009   109   115   128   141   147      0.0000      0.0011      0.0195     +0.02σ
    1024  127.986   8.000   109   115   128   141   147      0.0000      0.0013      0.0193     -0.58σ
    4096  128.048   7.996   110   115   128   141   146      0.0000      0.0010      0.0191     +1.93σ

  --- min_HD ACROSS FULL TRAJECTORY (T=4096) ---
Independent-sample reference (iid order-statistics model)
  H0 P(min<=8)=0.00e+00  P(min<=16)=0.00e+00  P(min<=32)=0.00e+00  P(min<=64)=9.09e-13

  Observed:
  P(min_HD<=8) =0.00e+00  P(min_HD<=16)=0.00e+00  P(min_HD<=32)=0.00e+00  P(min_HD<=64)=0.00e+00

  --- TREND (Spearman: log2(cp) vs mean_HD) ---
  Spearman r = +0.4196  p = 0.1745

  --- VERDICT ---
  [OK] no trajectory convergence detected
  [OK] close-orbit population consistent with H0 reference

[>>>] B32F: NEAR-NEIGHBOUR DISTANCE RETENTION
[>>>] Pairs: 102,400 | Max steps: 65,536
[>>>] Checkpoints: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 4096, 8192, 16384, 32768, 65536]
[>>>] H0 reference: HD ~ Binomial(256, 0.5)  μ=128.0  σ=8.0

  --- HD PER CHECKPOINT ---
  H0 analytic tails (Binomial(256,0.5), approximate baseline):
  P(HD<8)=1.17e-64  P(HD<16)=6.16e-54  P(HD<32)=8.28e-38  P(HD<64)=8.04e-17
  P(HD<96)=0.0000  P(HD<104)=0.0011  P(HD<112)=0.0195

      cp     mean     std   p01   p05   med   p95   p99        P<96       P<104       P<112    z_mean
  ------------------------------------------------------------------------------------------------
       1  127.987   8.020   109   115   128   141   147      0.0000      0.0011      0.0199     -0.50σ
       2  127.999   8.014   109   115   128   141   147      0.0000      0.0012      0.0197     -0.03σ
       4  127.972   7.956   109   115   128   141   146      0.0000      0.0011      0.0191     -1.12σ
       8  127.994   7.978   110   115   128   141   147      0.0000      0.0009      0.0187     -0.24σ
      16  128.003   8.021   109   115   128   141   147      0.0000      0.0014      0.0200     +0.11σ
      32  127.986   8.008   109   115   128   141   147      0.0000      0.0011      0.0191     -0.58σ
      64  128.019   7.988   110   115   128   141   147      0.0000      0.0010      0.0186     +0.77σ
     128  128.014   8.001   110   115   128   141   147      0.0000      0.0011      0.0187     +0.57σ
     256  128.002   7.996   110   115   128   141   147      0.0000      0.0010      0.0190     +0.10σ
     512  128.001   8.009   109   115   128   141   147      0.0000      0.0011      0.0195     +0.02σ
    1024  127.986   8.000   109   115   128   141   147      0.0000      0.0013      0.0193     -0.58σ
    4096  128.048   7.996   110   115   128   141   146      0.0000      0.0010      0.0191     +1.93σ
    8192  128.009   8.014   109   115   128   141   147      0.0000      0.0009      0.0196     +0.36σ
   16384  127.985   8.011   109   115   128   141   147      0.0000      0.0012      0.0200     -0.59σ
   32768  128.003   7.999   109   115   128   141   147      0.0000      0.0010      0.0195     +0.13σ
   65536  128.028   7.981   110   115   128   141   147      0.0000      0.0011      0.0186     +1.11σ

  --- min_HD ACROSS FULL TRAJECTORY (T=65536) ---
Independent-sample reference (iid order-statistics model)
  H0 P(min<=8)=0.00e+00  P(min<=16)=0.00e+00  P(min<=32)=0.00e+00  P(min<=64)=1.46e-11

  Observed:
  P(min_HD<=8) =0.00e+00  P(min_HD<=16)=0.00e+00  P(min_HD<=32)=0.00e+00  P(min_HD<=64)=0.00e+00

  --- TREND (Spearman: log2(cp) vs mean_HD) ---
  Spearman r = +0.4147  p = 0.1102

  --- VERDICT ---
  [OK] no trajectory convergence detected
  [OK] close-orbit population consistent with H0 reference
[OK] Test B32 finished in 551.18s.

[*] Running test: B51...

[>>>] B51: ALGEBRAIC DEGREE TEST
[>>>] EXACT  — degrees: 17..24  | trials per degree: 64
[>>>] PROB   — degrees: 25..31  | cubes: 16  (2 tasks × 8 cubes)
[>>>] Batch states: 65,536
[>>>] PROB tests full 256-bit output vector: nonzero = at least one output bit at degree d

  [1/2] exact degree test...
    degree   nonzero_trials   total_trials    result  verdict
  --------------------------------------------------------------
        17               38             64   nonzero  [OK]
        18               27             64   nonzero  [OK]
        19               31             64   nonzero  [OK]
        20               34             64   nonzero  [OK]
        21               35             64   nonzero  [OK]
        22               32             64   nonzero  [OK]
        23               25             64   nonzero  [OK]
        24               29             64   nonzero  [OK]

  [2/2] probabilistic degree test...
    degree   nonzero_cubes   cubes    result  verdict
  -------------------------------------------------------
        25              16      16   nonzero  [OK]
        26              16      16   nonzero  [OK]
        27              16      16   nonzero  [OK]
        28              16      16   nonzero  [OK]
        29              16      16   nonzero  [OK]
        30              16      16   nonzero  [OK]
        31              16      16   nonzero  [OK]

  --- VERDICT ---
  [OK] at least one output component has a nonzero degree-31 cube sum
  [OK] no algebraic degeneracy detected
[OK] Test B51 finished in 521.44s.

[*] Running test: B53...

[>>>] B53: LINEAR CORRELATION / WALSH SPECTRUM TEST
[>>>] Samples / batch     : 15,000,000
[>>>] σ_single (1/√N)     : 0.000258
[>>>] [A] Random masks    : 64 × 128 = 8,192 trials
[>>>] [B] Single-bit masks: 32 × 128 = 4,096 trials

  [1/4] MC baseline — random masks...

  ── MC baseline — random masks ──
  n Z-scores              : 8,192
  max |Z|                 :   3.6917σ
  mean |Z|                :   0.8042σ
  std Z                   :   1.0049  (expected ~1.0000)

  Tail counts  (observed  expected  ratio):
    |Z| > 3σ :      28 obs     22.12 exp  ratio =  1.27
    |Z| > 4σ :       0 obs      0.52 exp  ratio =  0.00
    |Z| > 5σ :       0 obs      0.00 exp  ratio =  0.00

  Anderson-Darling : stat = 0.7066  crit(5%) = 0.7520  crit(1%) = 1.0350  OK
  KS test          : stat = 0.0175  p = 0.0132
  EVT thresholds   : p99=4.8513σ  p99.9=5.2903σ  (M=8192, E[max]≈4.4055σ)
  MC max|Z|        : 3.6917σ

  [2/4] Engine — random masks...

  ── Engine — random masks ──
  n Z-scores              : 8,192
  max |Z|                 :   3.9799σ  (MC: 3.6917σ)
  mean |Z|                :   0.8062σ  (MC: 0.8042σ)
  std Z                   :   1.0141  (expected ~1.0000)

  Tail counts  (observed  expected  ratio):
    |Z| > 3σ :      32 obs     22.12 exp  ratio =  1.45
    |Z| > 4σ :       0 obs      0.52 exp  ratio =  0.00
    |Z| > 5σ :       0 obs      0.00 exp  ratio =  0.00

  Anderson-Darling : stat = 0.2815  crit(5%) = 0.7520  crit(1%) = 1.0350  OK
  KS test          : stat = 0.0066  p = 0.8711
  EVT thresholds   : p99=4.8513σ  p99.9=5.2903σ  (M=8192, E[max]≈4.4055σ)
  Engine max|Z|    : 3.9799σ
  MC max|Z|        : 3.6917σ
  Δ vs MC max      : +0.2881σ

  [3/4] MC baseline — single-bit masks...

  ── MC baseline — single-bit masks ──
  n Z-scores              : 4,096
  max |Z|                 :   3.8647σ
  mean |Z|                :   0.8003σ
  std Z                   :   1.0070  (expected ~1.0000)

  Tail counts  (observed  expected  ratio):
    |Z| > 3σ :      18 obs     11.06 exp  ratio =  1.63
    |Z| > 4σ :       0 obs      0.26 exp  ratio =  0.00
    |Z| > 5σ :       0 obs      0.00 exp  ratio =  0.00

  Anderson-Darling : stat = 0.5525  crit(5%) = 0.7520  crit(1%) = 1.0350  OK
  KS test          : stat = 0.0143  p = 0.3645
  EVT thresholds   : p99=4.7119σ  p99.9=5.1620σ  (M=4096, E[max]≈4.2452σ)
  MC max|Z|        : 3.8647σ

  [4/4] Engine — single-bit masks...

  ── Engine — single-bit masks ──
  n Z-scores              : 4,096
  max |Z|                 :   4.1405σ  (MC: 3.8647σ)
  mean |Z|                :   0.8086σ  (MC: 0.8003σ)
  std Z                   :   1.0145  (expected ~1.0000)

  Tail counts  (observed  expected  ratio):
    |Z| > 3σ :      12 obs     11.06 exp  ratio =  1.09
    |Z| > 4σ :       1 obs      0.26 exp  ratio =  3.85
    |Z| > 5σ :       0 obs      0.00 exp  ratio =  0.00

  Anderson-Darling : stat = 0.2505  crit(5%) = 0.7520  crit(1%) = 1.0350  OK
  KS test          : stat = 0.0111  p = 0.6927
  EVT thresholds   : p99=4.7119σ  p99.9=5.1620σ  (M=4096, E[max]≈4.2452σ)
  Engine max|Z|    : 4.1405σ
  MC max|Z|        : 3.8647σ
  Δ vs MC max      : +0.2758σ

  --- RESULTS SUMMARY ---
  branch                          max|Z|   AD stat  tail4σ obs  tail4σ exp
  ------------------------------------------------------------------------
  MC — random masks               3.6917    0.7066           0        0.52
  Engine — random masks           3.9799    0.2815           0        0.52
  MC — single-bit                 3.8647    0.5525           0        0.26
  Engine — single-bit             4.1405    0.2505           1        0.26

  --- VERDICT ---
  [A] Random masks    : OK
  [B] Single-bit masks: OK
  [OK] Walsh spectrum consistent with random-permutation baseline
  [OK] No linear bias above detection threshold
[OK] Test B53 finished in 123.30s.
```
