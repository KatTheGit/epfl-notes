

# Linear Systems, Matrix Equations...

## REF

### Row reduction algorithm

- find leftmost nonzero column.
- Create all zeroes below the pivot in column 1.
- Now treat the submatrix below row 1, and repeat.
  - After having done all the steps, also remove the zeroes above the pivot in the column.

## Link between linear systems and matrix equations

Given a matrix equation $Ax = b$, with $A \in \mathbb{M}_{n \times m}(\R)$, $b \in \R^n$, (n rows, m columns)

A linear system is equivalent to a matrix equation probably.

The below three statements are equivalent:

- ($Ax = b, x \in \R$)
- the vector $b$ is a linear combination of $A$'s columns, i.e. $b$ lies in $Span\{a_1, ..., a_m\}$
- The augmented matrix $(A | B)$ is consistent (has at least 1 solution).

Furthermore, if there exists a solution for any $b \in \R^n$:
- $\forall b \in \R, Ax = b$ has a solution
- Each $b \in R^n$ is a linear combination of the columns of $A$
- The columns of $A$ span $\R$, and $A$ has a pivot position in every row.

## Homogenity

There are two types of matrix equations:

- **Homogeneous** linear systems ($Ax = 0$)
- **Nonhomogeneous** linear systems ($Ax \neq 0$)

### Homogeneous systems

- Always consistent (since x = 0 is always a solution)
- It will have a nontrivial solution when there is at least 1 free variable.

if columns (m) > rows (n), then there are more variables than equations so the system has infinite nontrivial solutions.

If $S$ is the solution of $Ax = 0$, then $S$ is a subspace of $\R^m$. Proof:
- For any two solutions, $u$ and $v$, and any scalars $a$ and $b$, we have $au + bv \in S$
  - $A(au + bv) = a(Au) + b(Av) = 0 + 0 = 0$


### Nonhomogeneous systems

We suppose that the equation $Ax = b$ is consistent. $S_p$ is a particular solution. The solution $S$ is the set with all vectors of the form $S_p + S_h$, where $S_h$ is a solution to the homogeneous equation $Ax = 0$.



## Linear Independence/Dependence

The columns of a matrix are linearly independent <=> $Ax=0$ only has the trivial solution. Inversely, they are linearly dependent if there are more solutions, i.e. when there is a free var.

- If S is linearly dependent, at least one vector $v_j$ in $S$ is a linear combination of all the vectors in $S$ {$v_1\neq 0, ..., vj, ..., v_m$}
- If m>n ("wide"), then any solution set $S \sub \R^n$ is **linearly dependent**
- If a set contains 0, it is linearly dependent.

