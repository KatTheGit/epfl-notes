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

- $(A^{-1})^{-1} = A$
- $(AB)^{-1} = B^{-1} A^{-1}$
- If $A$ invertible, transpose invertible.
  - $(A^{-1})^t = (A^t)^{-1}$
- If a matrix is row equivalent to an identity matrix, it is invertible.
<br>
<br>

2x2 case $\begin{pmatrix} a & b \\ c & d \end{pmatrix}$
- $A^{-1} = \frac{1}{ad-bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$

### Algorithm to find $A^{-1}$

- Create augmented matrix $(A | I_a)$
- Perform row operations until $I_a$ appears in the first part
- The second part will be $A^{-1}.$

## Elementary matrix

- A matrix created using **one elementary row operation** on an identity matrix.

## Properties of square matrices

Let $A$ be an $n \times n$ matrix.

- $A$ invertible.
- $A$ is row equivalent to $I_n$
- $A$ has $n$ pivot positions
- $Ax = 0$ has only trivial solution.
- Columns of $A$ form a linearly independent set in $\R^n$
- Linear transformation $x \mapsto Ax$ is one-to-one (injective)
- $Ax = b$ has at least one solution $\forall b \in \R^n$ (surjective)
- $A^t$ is invertible.
- $\exists C, D \in \mathbb{M}_{n \times n}(\R) \quad | \quad CA = I_n, \space \space AD = I_n$

# Matrix Properties

A matrix is:
- **diagonal** - all entries aside the main diagonal are zero
- **lower diagonal** - all above diagonal are zero
- **upper diagonal** - all below diagonal are zero
