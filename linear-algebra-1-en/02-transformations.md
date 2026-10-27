# Linear transformations

$T: \R^m \to \R^n$ <br>
$x \mapsto T(x)$

Maps / transforms a vector with $m$ elements ($\in \R^m$) to a vector with $n$ ($\in \R^n$) elements.

The set of all "$T(x)$" is the **image** (sometimes called range) of T.

Any transformation T is linear if it satisfies:
- $T(x + y) = T(x) + T(y)$
- $\alpha T(x) = T(\alpha x)$
- $T(0) = 0$

A singular test:
- $T(\alpha x + \beta y) = \alpha T(x) + \beta T(y) \quad \forall \alpha, \beta \in \R$

For any $x, y \in \R^m$ and $\alpha \in \R$

## Matrix transformations

$T: \R^m \to \R^n$ <br>
$x \mapsto Ax$

$A \in \mathbb{M}_{n \times m}(\R)$ (an n*m real matrix)

Matrix transformations are linear.

### Standard matrix of T

There exists a unique matrix $A \in \mathbb{M}_{n \times m}(\R)$ such that $T(x) = Ax \quad \forall x \in \R^m$.

More precisely, $A = (T(e_1) | ... | T(e_m))$, $e_1$ through $e_m$ being unit vectors along each coordinate of $\R^m$.

It is unique because $T(e_j) = Ae_j = j^{th}$ column of $A$.

## Onto (surjective) and One-to-one (injective)

$T: \R^a \to \R^b$ <br>
$\space \space T(x) \mapsto Ax$

### Onto (surjective)

- every vector in $\R^b$ is the image of **at least** one vector in $\R^a$
- Columns of $A$ span $\R^b$
- cannot have $b < a$
- Every row of $A$ has pivot position, no rows of 0s in row echelon form.

### One-to-one (injective)

- Each vector in $R^b$ is the image of **at most** one vector in $R^a$.
- $Ax = 0$ has only **trivial solution**.
- cannot have $a < b$
- $\iff$ every column of $A$ has pivot. (aka columns linearly independent, no free var)