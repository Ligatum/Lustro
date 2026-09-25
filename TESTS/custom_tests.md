```text
=================================================================
                 LUSTRO CORE V1 - INTERNAL AUDIT                 
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
[OK] Test B2 finished in 513.05s.

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
[OK] Test B13 finished in 273.78s.

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
  228  s1_hi         1.000000      4.26σ       -1.20σ
   98  s0_hi         1.000000      4.24σ       -1.08σ
  151  s1_lo         1.000000      4.23σ       -0.57σ
  172  s1_lo         1.000000      4.13σ       -0.54σ
  240  s1_hi         1.000000      4.11σ       -1.05σ
  245  s1_hi         1.000000      4.02σ       -0.63σ
  248  s1_hi         1.000000      4.00σ        0.12σ
  114  s0_hi         1.000000      3.95σ       -2.71σ
  220  s1_hi         1.000000      3.87σ        1.01σ

  Top 10 output bits by maximum cell z-score (per-col):
  bit  domain     col_entropy    max|z|     H_z(MC)
  -------------------------------------------------------
  174  s1_lo         1.000000      4.27σ        0.08σ
   72  s0_hi         1.000000      4.26σ       -2.65σ
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
  114  s0_hi         1.000000      3.95σ       -2.71σ
   35  s0_lo         1.000000      3.17σ       -2.24σ
    8  s0_lo         1.000000      3.37σ       -2.19σ
  216  s1_hi         1.000000      3.18σ       -2.08σ
  227  s1_hi         1.000000      2.89σ       -2.05σ
  140  s1_lo         1.000000      3.02σ       -1.85σ
  204  s1_hi         1.000000      2.96σ       -1.85σ
  152  s1_lo         1.000000      3.43σ       -1.84σ
   42  s0_lo         1.000000      3.18σ       -1.81σ

  --- VERDICT ---
  Mean row entropy     : 1.000000  (ideal 1.000000)
  Mean col entropy     : 1.000000  (ideal 1.000000)
  [OK] corridor metric below detection threshold at current sample size
[OK] Test B16 finished in 224.09s.

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
     1      1507         0         0         0         0  [OK]
     3      1520         0         0         0         0  [OK]
     7      1496         1         0         0         0  [OK]
    13      1452         0         0         0         0  [OK]
    16      1423         1         0         0         0  [OK]
    32      1470         0         0         0         0  [OK]
    47      1488         1         0         0         0  [OK]
    63      1509         1         0         0         0  [OK]

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
     1      1452         0         0         0         0  [OK]
     7      1437         0         0         0         0  [OK]
    13      1470         0         0         0         0  [OK]
    32      1392         0         0         0         0  [OK]
    64      1487         0         0         0         0  [OK]
    96      1497         0         0         0         0  [OK]
   128      1406         1         0         0         0  [OK]
   192      1480         0         0         0         0  [OK]

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
[OK] Test B22 finished in 194.54s.

[*] Running test: B32...

[>>>] B32A: GLOBAL CONVERGENCE TEST
[>>>] Samples: 2,000,000
[>>>] DP bits: 16 | FP bits: 32
[>>>] Max steps: 65,536

  --- RESULTS ---
  Total samples      : 2,000,000
  DP hits            : 1,264,974
  Runaways           : 735,026
  Runaway rate       : 3.675130e-01
  Expected runaway   : 3.678794e-01
  Runaway deviation  : -3.664412e-04

  [FINGERPRINT SPACE]
  Unique fingerprints: 1,264,781
  Collisions         : 193
  Expected           : 186.28
  Z-score            : +0.49σ
  Max bucket         : 2

  [TRAJECTORY STATS]
  Avg steps (all)    : 41429.00
  Avg steps (DP only): 27421.38
  Max steps observed : 65,536

  [ENTROPY]
  Entropy            : 20.2704 bits
  Max entropy        : 20.2707 bits
  Entropy loss       : 0.0003

  --- VERDICT ---
  [OK] fingerprint distribution normal
  [diagnostic] entropy_loss=0.0003  (informational only)
  Runaway z-score    : -1.07σ
  [OK] runaway dynamics match theory

[>>>] B32B: XOR-PROJECTION OCCUPANCY
[>>>] Samples: 10,000,000 | Steps/state: 128 | Buckets: 65,536
[>>>] Projection: upper 16 bits of s0^s1^s2^s3

  --- XOR-PROJECTION OCCUPANCY RESULTS ---
  Total visits         : 1,280,000,000
  Expected per bucket  : 19531.25
  EVT baseline (max z) : 4.71σ
  Max bucket visits    : 20,080  (z=+3.93σ, EV-corr=-0.78σ)
  Chi-square           : 65130.97  (dof=65535, z=-1.12σ)
  Bucket entropy       : 15.999963 / 16.000000 bits
  Entropy loss         : 0.000037
  [OK] XOR-projection uniform — no concentration detected

[>>>] B32C: ORBIT MIXING UNDER ITERATION
[>>>] Samples: 10,000,000 | Steps: 128

  Per-bit density analysis:
  Max |density - 0.5|  : 0.000622  (bit 29, step 4)
  Bit z_raw            : 3.93σ
  Bit z_ev             : -0.63σ  (EVT baseline 4.56σ)

  --- ORBIT MIXING RESULTS ---
  σ(HW mean)           : 0.0025
  σ(word mean)         : 0.0013
  Max |HW - 128| / σ   : 2.40σ  (over 128 steps)
  Max |word - 32| / σ  : 2.72σ

  HW mean by step (first 16 and last 4):
   step   hw_mean       dev        z
  -----------------------------------
      0  127.9994    0.0006     0.23σ
      1  128.0042    0.0042     1.65σ
      2  128.0014    0.0014     0.57σ
      3  127.9995    0.0005     0.19σ
      4  128.0037    0.0037     1.46σ
      5  128.0052    0.0052     2.06σ
      6  127.9981    0.0019     0.75σ
      7  127.9991    0.0009     0.36σ
      8  128.0061    0.0061     2.40σ
      9  127.9983    0.0017     0.66σ
     10  127.9998    0.0002     0.06σ
     11  127.9979    0.0021     0.82σ
     12  127.9996    0.0004     0.17σ
     13  128.0010    0.0010     0.38σ
     14  128.0005    0.0005     0.18σ
     15  127.9985    0.0015     0.58σ
    124  127.9984    0.0016     0.63σ
    125  128.0032    0.0032     1.28σ
    126  128.0002    0.0002     0.08σ
    127  128.0036    0.0036     1.43σ

  Autocorrelation of HW series:
  lag 1  :  -0.101302
  lag 2  :  +0.029696
  lag 3  :  +0.069382
  lag 4  :  +0.122335
  lag 5  :  -0.089460

  [diagnostic] hw_z_ev=-0.71σ  w_z_ev=-0.39σ  bit_z_ev=-0.63σ  (EVT assumes independence — informational only)
  [diagnostic] ac_z=1.38σ  (H0 distribution not derived — autocorrelation informational only)

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
  Recurrences found    : 15,564  (0.7782%)
  H0 expected rate     : 0.7960%  (z=-0.44σ)
  No recurrence        : 1,984,436  (orbit > 8,192)
  Min recurrence dist  : 1
  Max recurrence dist  : 8,138
  Mean recurrence dist : 2745.70  (conditional on recurrence found)
  Median recur. dist   : 2423.00

  Recurrence gap distribution  (H0 baseline from Rust simulation):
  range                      obs    obs_frac     h0_frac    ratio
  --------------------------------------------------------------
  [1, 2)                       5    0.000003    0.000000      nan
  [2, 4)                       7    0.000003    0.000000      nan
  [4, 8)                       9    0.000005    0.000000      nan
  [8, 16)                     24    0.000012    0.000000      nan
  [16, 32)                    68    0.000034    0.000020     1.70
  [32, 64)                   124    0.000062    0.000060     1.03
  [64, 128)                  235    0.000117    0.000120     0.98
  [128, 256)                 444    0.000222    0.000260     0.85
  [256, 512)                 913    0.000456    0.000440     1.04
  [512, 1024)              1,773    0.000887    0.001080     0.82
  [1024, 8193)            11,962    0.005981    0.005980     1.00

  Adjacent-step FP collisions (distance=1)  [diagnostic only]:
  Observed             : 5
  FP collisions        : 0  (unique=15,564 / total=15,564)

  [OK] FP recurrence consistent with H0 baseline

[>>>] B32E: STATE-SPACE PROFILE
[>>>] Samples: 10,000,000 | Checkpoints: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 4096]
[>>>] Windows: 16 | Buckets/window: 65,536
[>>>] λ = N/K = 152.59 | MM bias = 0.004727

  --- MILLER-MADOW FINITE-SAMPLE BASELINE ---
  Theoretical MM bias  : 0.004727
  Observed range       : 0.004725 .. 0.004737
  Deviation from MM    : -2.42e-06 .. +9.27e-06

  --- ENTROPY LOSS PER CHECKPOINT (mean ± std over 16 windows) ---
    checkpoint       mean_el      std_el   max_bkt_zev    occupied  verdict
  ----------------------------------------------------------------------------
             1      0.004733    2.64e-05         +0.59σ     65536.0  [OK]
             2      0.004732    2.53e-05         +0.26σ     65536.0  [OK]
             4      0.004733    2.00e-05         +0.59σ     65536.0  [OK]
             8      0.004736    1.96e-05         +0.34σ     65536.0  [OK]
            16      0.004737    1.78e-05         +0.50σ     65536.0  [OK]
            32      0.004725    2.57e-05         +0.50σ     65536.0  [OK]
            64      0.004729    2.27e-05         +0.42σ     65536.0  [OK]
           128      0.004731    2.05e-05         +1.31σ     65536.0  [OK]
           256      0.004726    2.82e-05         +0.26σ     65536.0  [OK]
           512      0.004731    2.82e-05         +0.34σ     65536.0  [OK]
          1024      0.004733    2.90e-05         +0.91σ     65536.0  [OK]
          4096      0.004725    2.75e-05         +0.18σ     65536.0  [OK]

  --- DELTA ENTROPY LOSS ---
  Δ entropy_loss (cp4096 - cp1) : -0.000008
  max - min across checkpoints  : 0.000012

  --- GLOBAL MAX BUCKET ---
  Global max occupancy : 227  (z=+6.02σ, EV-corr=+1.31σ)
  Expected λ           : 152.59
  Expected occupied    : 65536.0 / 65,536

  --- FANO FACTOR (Var/Mean, ideal = 1.0) ---
    checkpoint     mean_fano      max_fano  [diagnostic only]
  --------------------------------------------------
             1      1.000050      1.008918
             2      0.999776      1.008689
             4      1.000168      1.010595
             8      1.000639      1.008975
            16      1.000816      1.006578
            32      0.998387      1.006798
            64      0.999404      1.006408
           128      0.999675      1.007094
           256      0.998724      1.009752
           512      0.999729      1.009811
          1024      0.999947      1.010699
          4096      0.998420      1.007392

  --- OCCUPANCY SPECTRUM — worst (cp=128, window=10) ---
  Entropy loss         : 0.004744
  Fano factor          : 1.002773
  λ = 152.6  σ = 12.4  spectrum around mode:
       k    observed  gauss_exp         z        k    observed  gauss_exp         z        k    observed  gauss_exp         z
  ---------------------------------------   ---------------------------------------   ---------------------------------------
     140       1,279     1259.3    +0.55σ      149       1,963     2029.1    -1.47σ      158       1,931     1922.9    +0.19σ
     141       1,421     1363.1    +1.57σ      150       2,086     2070.6    +0.34σ      159       1,801     1849.8    -1.13σ
     142       1,473     1465.9    +0.19σ      151       2,120     2099.1    +0.46σ      160       1,739     1767.9    -0.69σ
     143       1,638     1566.1    +1.82σ      152       2,188     2114.2    +1.61σ      161       1,680     1678.5    +0.04σ
     144       1,724     1662.2    +1.52σ      153       2,015     2115.4    -2.18σ      162       1,482     1583.3    -2.55σ
     145       1,773     1752.6    +0.49σ      154       2,091     2102.8    -0.26σ      163       1,502     1483.7    +0.47σ
     146       1,896     1836.0    +1.40σ      155       2,025     2076.6    -1.13σ      164       1,363     1381.3    -0.49σ
     147       1,942     1910.7    +0.72σ      156       2,007     2037.3    -0.67σ                                          
     148       1,995     1975.5    +0.44σ      157       1,946     1985.8    -0.89σ                                          
  p99.9  : 192.5  |  p99.99 : 200.0

  --- TREND ANALYSIS (Spearman: log2(cp) vs mean_entropy_loss) ---
  Spearman r           : -0.5385
  p-value              : 0.0709
  [OK] no increasing entropy-loss trend detected

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
       2  127.982   8.013   109   115   128   141   147      0.0000      0.0011      0.0198     -0.73σ
       4  127.960   7.988   109   115   128   141   146      0.0000      0.0012      0.0195     -1.61σ
       8  127.995   7.977   109   115   128   141   147      0.0000      0.0012      0.0191     -0.19σ
      16  127.981   8.017   109   115   128   141   147      0.0000      0.0012      0.0199     -0.77σ
      32  127.979   7.985   110   115   128   141   147      0.0000      0.0010      0.0191     -0.84σ
      64  127.995   7.974   109   115   128   141   147      0.0000      0.0010      0.0192     -0.19σ
     128  127.991   8.033   109   115   128   141   147      0.0000      0.0010      0.0202     -0.34σ
     256  127.996   7.988   110   115   128   141   147      0.0000      0.0011      0.0188     -0.17σ
     512  127.935   7.985   109   115   128   141   146      0.0000      0.0011      0.0195     -2.60σ
    1024  128.039   7.992   110   115   128   141   147      0.0000      0.0010      0.0189     +1.56σ
    4096  128.024   8.024   109   115   128   141   147      0.0000      0.0009      0.0200     +0.97σ

  --- min_HD ACROSS FULL TRAJECTORY (T=4096) ---
Independent-sample reference (iid order-statistics model)
  H0 P(min<=8)=0.00e+00  P(min<=16)=0.00e+00  P(min<=32)=0.00e+00  P(min<=64)=9.09e-13

  Observed:
  P(min_HD<=8) =0.00e+00  P(min_HD<=16)=0.00e+00  P(min_HD<=32)=0.00e+00  P(min_HD<=64)=0.00e+00

  --- TREND (Spearman: log2(cp) vs mean_HD) ---
  Spearman r = +0.4755  p = 0.1182

  --- VERDICT ---
  [OK] no trajectory convergence detected
  [OK] close-orbit population consistent with H0 reference
[OK] Test B32 finished in 419.17s.

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
[OK] Test B51 finished in 335.57s.

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
[OK] Test B53 finished in 129.07s.

```
