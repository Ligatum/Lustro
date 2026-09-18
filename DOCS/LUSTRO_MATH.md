# IDM — Mathematical Notation

IDM performs its internal mixing on 64-bit channels and packs them into 128-bit words at the boundary.

* $\boxplus$ — addition modulo $2^{64}$.
* $\oplus$ — bitwise XOR operation.
* $\odot$ — multiplication modulo $2^{64}$.
* $\mathrm{ROL}_k(x)$ — cyclic left rotation of $x$ by $k$ positions within the width of $x$.
* $x \gg k$ — logical right shift of $x$ by $k$ positions.
* $x \bmod 2^n$ — reduction modulo, corresponding to retaining the $n$ least significant bits.

$$
\phi = \mathrm{0x9E3779B97F4A7C15}
$$

$$
\phi_{23} = \mathrm{ROL}_{23}(\phi)
$$

$$
\phi_{17} = \mathrm{ROL}_{17}(\phi)
$$

$$
a = \left\lfloor \frac{s_0}{2^{64}} \right\rfloor
$$

$$
b = s_0 \bmod 2^{64}
$$

$$
c = \left\lfloor \frac{s_1}{2^{64}} \right\rfloor
$$

$$
d = s_1 \bmod 2^{64}
$$

$$
a \leftarrow a \boxplus b
$$

$$
c \leftarrow c \boxplus d
$$

$$
b \leftarrow b \oplus \mathrm{ROL}_{11}(a)
$$

$$
d \leftarrow d \oplus \mathrm{ROL}_{19}(c)
$$

$$
a \leftarrow a \boxplus \phi
$$

$$
c \leftarrow c \boxplus \phi_{23}
$$

$$
a \leftarrow a \oplus \mathrm{ROL}_{37}(c)
$$

$$
d \leftarrow d \oplus \mathrm{ROL}_{43}(b)
$$

$$
b \leftarrow b \boxplus a
$$

$$
d \leftarrow d \boxplus c
$$

$$
a \leftarrow a \oplus \mathrm{ROL}_{31}(b)
$$

$$
c \leftarrow c \oplus \mathrm{ROL}_{47}(d)
$$

$$
m = (a \oplus c) \odot \phi
$$

$$
b \leftarrow b \oplus m
$$

$$
d \leftarrow d \oplus \mathrm{ROL}_{33}(m)
$$

$$
\mathrm{mix}_0 = a \oplus c
$$

$$
m_0 =
\left(
\mathrm{mix}_0
\oplus
\mathrm{ROL}_{32}(\mathrm{mix}_0)
\right)
\odot \phi
$$

$$
m_1 = (b \oplus d) \odot \phi_{17}
$$

$$
a \leftarrow a \oplus m_0
$$

$$
c \leftarrow c \oplus \mathrm{ROL}_{23}(m_0)
$$

$$
b \leftarrow b \oplus m_1
$$

$$
d \leftarrow d \oplus \mathrm{ROL}_{41}(m_1)
$$

$$
a \leftarrow a \boxplus b
$$

$$
d \leftarrow d \oplus \mathrm{ROL}_{33}(a)
$$

$$
b \leftarrow b \oplus \mathrm{ROL}_{21}(c \oplus d)
$$

$$
a \leftarrow a \boxplus d
$$

$$
c \leftarrow c \boxplus b
$$

$$
d \leftarrow d \oplus \mathrm{ROL}_{41}(a)
$$

$$
b \leftarrow b \oplus \mathrm{ROL}_{23}(c)
$$

$$
b \leftarrow b \boxplus a
$$

$$
d \leftarrow d \boxplus c
$$

$$
a \leftarrow a \oplus \mathrm{ROL}_{17}(b)
$$

$$
c \leftarrow c \oplus \mathrm{ROL}_{31}(d)
$$

$$
s'_0 = 2^{64}a + b
$$

$$
s'_1 = 2^{64}c + d
$$


# ERD — Mathematical Notation

* $\boxplus$ — addition modulo $2^n$, where $n$ denotes the operand width; specifically, modulo $2^{128}$ for base values and modulo $2^{64}$ for working channels.
* $\oplus$ — bitwise XOR operation.
* $\odot$ — multiplication modulo $2^{64}$.
* $\lor$ — bitwise OR operation.
* $\mathrm{ROL}_k(x)$ — cyclic left rotation of $x$ by $k$ positions within the width of $x$.
* $x \gg k$ — logical right shift of $x$ by $k$ positions.
* $x \bmod 2^n$ — reduction modulo, corresponding to retaining the $n$ least significant bits.
* $v_{0,\mathrm{base}},v_{1,\mathrm{base}},s_0,s_1$ — 128-bit values.
* $v_0,v_1,r_0,r_1,x_0,x_1$ — 64-bit values.
* $k_0,k_1,\mathrm{rot}_0,\mathrm{rot}_1$ — 32-bit rotation amounts.

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
x_0 \leftarrow x_0 \odot (x_0 \lor 1)
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
x_1 \leftarrow x_1 \odot (x_1 \lor 1)
$$

$$
k_0 = (x_0 \gg 58) \lor 1
$$

$$
k_1 = (x_1 \gg 58) \lor 1
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

# ERD Round with Weyl Counter — Mathematical Notation

* $\boxplus$ — addition modulo $2^{64}$.
* $\oplus$ — bitwise XOR operation.
* $\odot$ — multiplication modulo $2^{64}$.
* $\lor$ — bitwise OR operation.
* $\mathrm{ROL}_k(x)$ — cyclic left rotation of $x$ by $k$ positions within the width of $x$.
* $\mathrm{rc}$ — 64-bit value.
* $\mathrm{step}$ — 64-bit value.
* $\mathrm{rc}_{128}$ — 128-bit value.
* $\mathrm{rot}_0,\mathrm{rot}_1$ — 32-bit rotation amounts.

$$
\phi = \mathrm{0x9E3779B97F4A7C15}
$$

$$
\mathrm{rc} = \phi \odot (\mathrm{step} \boxplus 2)
$$

$$
\mathrm{rc}_{128} = \left(2^{64} \cdot \mathrm{ROL}_{17}(\mathrm{rc})\right) \lor \mathrm{rc}
$$

$$
s_0 \leftarrow s_0 \oplus \mathrm{rc}_{128}
$$

$$
s_1 \leftarrow s_1 \oplus \mathrm{ROL}_{17}(\mathrm{rc}_{128})
$$

$$
(\mathrm{rot}_0,\mathrm{rot}_1) = \mathrm{ERD}(s_0,s_1)
$$

$$
s_0 \leftarrow \mathrm{ROL}_{\mathrm{rot}_0}(s_0)
$$

$$
s_1 \leftarrow \mathrm{ROL}_{\mathrm{rot}_1}(s_1)
$$
