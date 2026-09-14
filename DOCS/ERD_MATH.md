# ERD — Mathematical Notation

* $\boxplus$ — addition modulo $2^n$, where $n$ denotes the operand width; specifically, modulo $2^{128}$ for base values and modulo $2^{64}$ for working channels.
* $\oplus$ — bitwise XOR operation.
* $\odot$ — multiplication modulo $2^{64}$.
* $\mathrm{ROL}_k(x)$ — cyclic left rotation of $x$ by $k$ positions within the width of $x$.
* $x \gg k$ — logical right shift of $x$ by $k$ positions.
* $x \bmod 2^n$ — reduction modulo, corresponding to retaining the $n$ least significant bits.

## ERD

$$
v_{0,\mathrm{base}} = s_0 \boxplus s_1
$$

$$
v_{1,\mathrm{base}} = s_0 \oplus \mathrm{ROL}_{42}(s_1)
$$

$$
v_{0,\mathrm{base}}
\leftarrow
v_{0,\mathrm{base}}
\oplus
\left(v_{0,\mathrm{base}} \gg 64\right)
\oplus
\mathrm{ROL}_{37}(v_{0,\mathrm{base}})
$$

$$
v_{1,\mathrm{base}}
\leftarrow
v_{1,\mathrm{base}}
\oplus
\left(v_{1,\mathrm{base}} \gg 64\right)
\oplus
\mathrm{ROL}_{43}(v_{1,\mathrm{base}})
$$

$$
v_0 = v_{0,\mathrm{base}} \bmod 2^{64}
$$

$$
v_1 = v_{1,\mathrm{base}} \bmod 2^{64}
$$

$$
v_0 \leftarrow v_0 \boxplus \mathrm{ROL}_{31}(v_1)
$$

$$
v_1 \leftarrow v_1 \oplus \mathrm{ROL}_{27}(v_0)
$$

$$
v_0 \leftarrow v_0 \boxplus \mathrm{ROL}_{17}(v_1)
$$

$$
v_1 \leftarrow v_1 \oplus \mathrm{ROL}_{29}(v_0)
$$

$$
r_0 = \mathrm{ROL}_{11}(v_1),
\qquad
r_1 = \mathrm{ROL}_{13}(v_0)
$$

$$
x_0 =
\left(v_0 \oplus r_0\right)
\oplus
\left(
\left(v_0 \oplus r_0\right) \gg 32
\right)
$$

$$
x_0 \leftarrow x_0 \odot (x_0 \mid 1)
$$

$$
x_1 =
\left(v_1 \oplus r_1\right)
\oplus
\left(
\left(v_1 \oplus r_1\right) \gg 32
\right)
$$

$$
x_1 \leftarrow x_1 \odot (x_1 \mid 1)
$$

$$
k_0 = (x_0 \gg 58) \mid 1
$$

$$
k_1 = (x_1 \gg 58) \mid 1
$$

$$
v_0
\leftarrow
v_0
\boxplus
\left(
\mathrm{ROL}_{k_0}(v_1)
\oplus
(v_1 \gg 7)
\right)
$$

$$
v_1
\leftarrow
v_1
\oplus
\left(
(v_0 \gg 7)
\oplus
\mathrm{ROL}_{k_1}(v_0)
\right)
$$

$$
v_0 \leftarrow v_0 \boxplus \mathrm{ROL}_{17}(v_1)
$$

$$
v_1 \leftarrow v_1 \oplus \mathrm{ROL}_{40}(v_0)
$$

$$
v_0 \leftarrow v_0 \oplus (v_0 \gg 29)
$$

$$
\mathrm{rot}_0 =
\left\lfloor
\frac{v_0 \cdot 127}{2^{64}}
\right\rfloor + 1,
\qquad
\mathrm{rot}_1 =
\left\lfloor
\frac{v_1 \cdot 113}{2^{64}}
\right\rfloor + 1
$$
