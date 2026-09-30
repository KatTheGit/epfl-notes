# Matrix Operations

Why do we learn this after transformations and systems? XD

## Matrix Addition

$A + B$

Only works on matrices of the same size.

All respective elements are added.

## Matrix SCALAR Multiplication

$\lambda A = (\lambda a_{ij})$

Each element is multiplied by the scalar.

## Matrix Multiplication

$\displaystyle (AB)_{cd} = \sum_{k = 1}^{n} A_{ck} B_{kd}$

- Requirement: $A_{m \times n}$ & $B_{o \times p}$ then $n = o$
  - Size of new matrix will be $m \times p$

### Linear transformation

Given $T_1$ and $T_2$ with $A$, $B$ their respective standard matrices, $T_1(T_2(x)) = BAx$.

### Properties

$A, B, C$ are matrices where we assume multiplication is possible. $\lambda$ is a scalar.

- $A(BC) = (AB)C$
- $A(B + C) = AB + AC$
- $(B+C)A = BA + CA$
- $\lambda (AB) = A (\lambda B) = (\lambda A) B$
- $I_pA = A = AI_n, for A ∈ M_{p×n(\R)}$, $I$ being an identity matrix.

### Transpose

$(A^t)_{ij} = A_{ji}$

- $(A^t)^t = A$
- $(A+B)^t = A^t + B^t$
- $(\lambda A)^t = \lambda A^t$
- $(AB)^t = B^tA^t$

### Inverse

A square matrix is said to be invertible if there exists $C$ such that:

$AC = I_n$ and $CA = I_n$

# Matrix Properties

A matrix is:
- **diagonal** - all entries aside the main diagonal are zero
- **lower diagonal** - all above diagonal are zero
- **upper diagonal** - all below diagonal are zero
