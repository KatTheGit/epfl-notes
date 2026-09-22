# Linear transformations

$T: \R^m \to \R^n$ <br>
$x \mapsto T(x)$

Maps / transforms a vector with $m$ elements ($\in \R^m$) to a vector with $n$ ($\in \R^n$) elements.

The set of all "$T(x)$" is the **image** (sometimes called range) of T.

Any transformation T is linear if it satisfies:
- $T(x + y) = T(x) + T(y)$
- $\alpha T(x) = T(\alpha x)$

For any $x, y \in \R^m$ and $\alpha \in \R$

## Matrix transformations

$T: \R^m \to \R^n$ <br>
$x \mapsto Ax$

$A \in \mathbb{M}_{n \times m}(\R)$ (an n*m real matrix)

Matrix transformations are linear.

### Standard matrix of T

There exists a unique matrix $A \in \mathbb{M}_{n \times m}(\R)$ such that $T(x) = Ax \space \forall x \in \R^m$.

More precisely, $A = (T(e_1) | ... | T(e_m))$, $e_1$ through $e_m$ being unit vectors along each coordinate of $\R^m$.

It is unique because $T(e_j) = Ae_j = j^{th}$ column of $A$.