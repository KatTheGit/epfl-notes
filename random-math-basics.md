## Symbols

$:=$ defined as

$:$ such as / tel que

$=>$ implies

$<=$ implies, freaky style

$<=>$ if and only if

## Vectors

$|| a \times b|| = ||a||*||b||*sin(\theta)$ (0 = parallel, returns area!!!)

ALSO NOTED $|| a \land b||$

$a \times b = ||a||*||b||*sin(\theta) * \vec{n}$, n being the fucky wucky perpendicular vector, aka normal unit vector.


$a * b = ||a||*||b||*cos(\theta)$ (0 = perpendicular)

$\hat{v} = \frac{\vec{v}}{||\vec{v}||}$ (normalized, unit vector, norm 1, whatever idfk)

## Random SI units

| Unit | SI |
|--|--|
| Force | m * kg / s²
| Power | m² * kg / s³

## Derivation

| $F$ | $F'$ |
|--|--|
| $k$ | $0$ |
| $x$ | $1$ |
| $x^n$ | $nx^{n+1}$ |
| $\frac{1}{x^n}$ | $\frac{-n}{x^n+1}$ |
| $\sqrt x$ | $\frac{1}{2\sqrt x}$ |
| $ln(x)$ | $\frac{1}{x}$ |
| $e^x$ | $e^x$ |
| $cos(x)$ | $-sin(x)$ |
| $sin(x)$ | $cos(x)$ |
| $tan(x)$ | $\frac{x'}{cos^2(x)}$ |
| $tan(x)$ | $x'*(1+tan^2(x))$ |
| $k^x$ | $k^xln(x)$ |
| $u * v$ | $u' * v + u * v'$ |
| $\frac{u}{v}$ | $\frac{u' * v - u * v'}{v^2}$ |
| $v(u(x))$ | $v'(u(x)) *u'(x)$ |

## Integration

Always add the integration constant.

with known x and y, we can find this constant.

| $F$ | $\int F dx$ |
|--|--|
| $x^n$ | $\frac{x^{n+1}}{n+1} + c$
| $k \in \R$ | $kx + c$
| $\frac{1}{\sqrt x}$ | $2 \sqrt x + c$
| $\frac{1}{x^n}, n\in \N \backslash \{0, 1\}$ | $\frac{-1}{(n-1)x^{n-1}} + c$
| $cos(x)$ | $sin(x) + c$
| $sin(x)$ | $-cos(x)+c$
| $e^x$ | $e^x + c$