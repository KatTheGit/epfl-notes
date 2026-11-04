# Transformations in Bases n whatnot


## Matrix of a Linear Transformation Relative to Two Bases

$n \times m$ matrix of $T$ relative to the bases $B$ and $C$ unique: $[T(x)]_{B \to C} = \begin{pmatrix} [T(b_1)]_C && ... && [T(b_m)]_C \end{pmatrix}$

Such that: $[T(x)]_C = [T]_{B \to C} [x]_B$

### Theorem 1

- $T: V \to W$
  - $B_V$ basis of $V$
  - $B_W$ basis of $W$
  - $M = [T]_{B_V \to B_W}$

1. $u \in Ker(T) \iff [u]_{B_V} \in Nul(M)$
2. $w \in Im(T) \iff [w]_{B_W} \in Col(M)$

## Change of Basis

$P_{B_V \to B_W} = [id_V]_{B_V \to B_W}$

With $id_V$ being the identity transformation in $V$.

### Theorem

let $B$ and $C$ be bases.

$P_{B \to C} = \begin{pmatrix} [b_1]_C && ... && [b_n]_C \end{pmatrix}$