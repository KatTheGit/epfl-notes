# Determinants

Only work on $n \times n$ matrices.

## Simple determinants

$det(\begin{pmatrix} a & b \\ c & d \end{pmatrix}) = ad-bc$

## Cofactor Expansion

We define the cofactor $C_{ij} = (-1)^{i+j}\cdot M_{ij}$.
- $M_{ij}$ is the is the **minor** matrix of $A$ with rows and colums $j, i$ removed.
- $(-1)^{i+j}$ is to toggle the sign.

We now have: $det(A) = \displaystyle \sum_{j=1}^{n}a_{1j}C_{1j}$.
- In other words, we iterate over the top row, and multiply it to the cofactor, and add everything, toggling the sign according to $(-1)^{i+j}$

## Behaviour of determinant after E.R.O.

- Swap rows: $\quad det(B) = -1 \cdot det(A)$
- Scale row by $\lambda \not = 0$: $\quad det(B) = \lambda \cdot det(A)$
- Add multiple of row: $\quad det(B) = det(A)$

NOTE: Never can become 0

### Triangular Matrix META

For a triangular matrix: det = mult of all diagonal elements

To find the det of a big matrix, make it a trinagle

## Determinant of Elementary Matrix (AKA derived from EROs)


Never 0.


## Properties of Determinant

- $det(AB) = det(A)\cdot det(B)$
- $det(A) = 0 \iff$
  - A **row** or **column** of **zeros**.
  - Two identical or proportional rows/columns.
    - Vectors are **linearly dependent**.
- A matrix is invertible if its determinant is nonzero
- $det(A^t) = det(A)$
- $a \cdot (b \times c) = det(\big (a | b | c\big ))$ in $\R^3$

## Geometric Interpretation

$det((a_1 | a_2)) =$ area of parallelogram made by $a_1, a_2$. Same in 3D, volume of parallelepiped.

For a lintrans $T(x) = Ax$:$\quad$ Area of $T(S) = |det(A)| \cdot ($Area of $S)$

