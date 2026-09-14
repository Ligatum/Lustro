\# ERD — Mathematical Notation



\* $\\boxplus$ — addition modulo $2^n$, where $n$ denotes the operand width; specifically, modulo $2^{128}$ for base values and modulo $2^{64}$ for working channels.

\* $\\oplus$ — bitwise XOR operation.

\* $\\odot$ — multiplication modulo $2^{64}$.

\* $\\mathrm{ROL}\_k(x)$ — cyclic left rotation of $x$ by $k$ positions within the width of $x$.

\* $x \\gg k$ — logical right shift of $x$ by $k$ positions.

\* $x \\bmod 2^n$ — reduction modulo, corresponding to retaining the $n$ least significant bits.



\## ERD



$$

v\_{0,\\mathrm{base}} = s\_0 \\boxplus s\_1

$$



$$

v\_{1,\\mathrm{base}} = s\_0 \\oplus \\mathrm{ROL}\_{42}(s\_1)

$$



$$

v\_{0,\\mathrm{base}}

\\leftarrow

v\_{0,\\mathrm{base}}

\\oplus

\\left(v\_{0,\\mathrm{base}} \\gg 64\\right)

\\oplus

\\mathrm{ROL}\_{37}(v\_{0,\\mathrm{base}})

$$



$$

v\_{1,\\mathrm{base}}

\\leftarrow

v\_{1,\\mathrm{base}}

\\oplus

\\left(v\_{1,\\mathrm{base}} \\gg 64\\right)

\\oplus

\\mathrm{ROL}\_{43}(v\_{1,\\mathrm{base}})

$$



$$

v\_0 = v\_{0,\\mathrm{base}} \\bmod 2^{64}

$$



$$

v\_1 = v\_{1,\\mathrm{base}} \\bmod 2^{64}

$$



$$

v\_0 \\leftarrow v\_0 \\boxplus \\mathrm{ROL}\_{31}(v\_1)

$$



$$

v\_1 \\leftarrow v\_1 \\oplus \\mathrm{ROL}\_{27}(v\_0)

$$



$$

v\_0 \\leftarrow v\_0 \\boxplus \\mathrm{ROL}\_{17}(v\_1)

$$



$$

v\_1 \\leftarrow v\_1 \\oplus \\mathrm{ROL}\_{29}(v\_0)

$$



$$

r\_0 = \\mathrm{ROL}\_{11}(v\_1),

\\qquad

r\_1 = \\mathrm{ROL}\_{13}(v\_0)

$$



$$

x\_0 =

\\left(v\_0 \\oplus r\_0\\right)

\\oplus

\\left(

\\left(v\_0 \\oplus r\_0\\right) \\gg 32

\\right)

$$



$$

x\_0 \\leftarrow x\_0 \\odot (x\_0 \\mid 1)

$$



$$

x\_1 =

\\left(v\_1 \\oplus r\_1\\right)

\\oplus

\\left(

\\left(v\_1 \\oplus r\_1\\right) \\gg 32

\\right)

$$



$$

x\_1 \\leftarrow x\_1 \\odot (x\_1 \\mid 1)

$$



$$

k\_0 = (x\_0 \\gg 58) \\mid 1

$$



$$

k\_1 = (x\_1 \\gg 58) \\mid 1

$$



$$

v\_0

\\leftarrow

v\_0

\\boxplus

\\left(

\\mathrm{ROL}\_{k\_0}(v\_1)

\\oplus

(v\_1 \\gg 7)

\\right)

$$



$$

v\_1

\\leftarrow

v\_1

\\oplus

\\left(

(v\_0 \\gg 7)

\\oplus

\\mathrm{ROL}\_{k\_1}(v\_0)

\\right)

$$



$$

v\_0 \\leftarrow v\_0 \\boxplus \\mathrm{ROL}\_{17}(v\_1)

$$



$$

v\_1 \\leftarrow v\_1 \\oplus \\mathrm{ROL}\_{40}(v\_0)

$$



$$

v\_0 \\leftarrow v\_0 \\oplus (v\_0 \\gg 29)

$$



$$

\\mathrm{rot}\_0 =

\\left\\lfloor

\\frac{v\_0 \\cdot 127}{2^{64}}

\\right\\rfloor + 1,

\\qquad

\\mathrm{rot}\_1 =

\\left\\lfloor

\\frac{v\_1 \\cdot 113}{2^{64}}

\\right\\rfloor + 1

$$



