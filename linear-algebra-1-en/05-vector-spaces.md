# Vector Spaces, Subspaces

## (real) Vector Space

A non-empty set equipped with
- addition
- multiplication

The following axioms must be satisfied, for a vector space $V$:
- $\vec a + \vec b = \vec b + \vec a$
- $\vec a + (\vec b + \vec c) = (\vec a + \vec b) + \vec c$
- $\exists \vec 0 \in V\quad |\quad \vec u + \vec 0 = \vec u$
- $\forall \vec u \in V \space \space \exists space \vec{-u} \space \space|\space \space \vec u + (\vec{-u}) = 0$
- $\beta (\vec a + \vec b) = \beta \vec a + \beta \vec b$
- $(\beta + \gamma) \vec a = \beta \vec a + \gamma \vec a$
- $\gamma (\beta \vec a) = (\gamma \beta) \vec a$
- $1 \vec u = \vec u$

Furthermore:
- $0u = 0$
- $\alpha 0 = 0$
- $−u = (−1)u$

## Subspaces

A subspace of a vector space $V$ is a subset $H$ that satisfies ($H \sube V$):

- $(\vec 0\in V) \in H$ (vector 0 of V is in H)
- $\forall \vec a, \vec b \in H \quad \vec a + \vec b \in H$ (closed under vector addition)
- $\forall \vec a \in H, \beta \in \R \quad \beta \vec a \in H$ (closed under scalar multiplication)

The span of vectors, noted $Span\set{\vec a, \vec b, \vec c, ...}$, is the set of all linear combinations of those vectors in $V$, and is a **subspace** of $V$. This is the subspace generated, or spanned by those vectors.

## Null Space

Null space of $A_{n \times m}$ is the set of all solutions to $Ax = 0$.

$\set{x \in \R^m | Ax = 0}$

AKA Set of all (**vector**) solutions to $Ax = 0$ for matrix $A$.

A null space is a subspace.

## Column Space

The column space of $A_{n \times m}$ matrix, $Col(A) = Span \set{col_1, col_2, ..., col_m}$


$\set{b \in \R^n | Ax = b \space \space \exists x}$

Column space is a subspace

## Linear transformations

$T: V \to W$ (both vector spaces) assigns to each $x \in V$ a unique $T(x) \in W$, with the following rules:

- $T(u + v) = T(u) + T(v)$
- $T( \alpha u) = \alpha T(u)$

$Ker(T) = \set{u \in V | T(u) = 0_W}$ (subspace of V)

$Im(T) = \set{T(u) \in W | u \in V}$ (subspace of W)

## Linear Independence

A set of vectors $\set{v_1, v_2, ..., v_n}$ in a vector space $V$

Is **linearly independent** if $\alpha_1 v_1 + \alpha_2 v_2 + ... + \alpha_n v_n = 0_V$ has **only** the trivial solution. ($\alpha$s are scalars)

Otherwise it is **linearly dependent**.

### How to Prove Linear Independence

- Write the matrix equation $\alpha_1 v_1 + \alpha_2 v_2 + ... + \alpha_n v_n = 0_V$.
- Explicit and multiply matrices by alpha
- Add all matrices together, we end up with Matrix $= 0$ Matrix
- Each set of components is an equation, and solve the equation set.
- Usually we will find a free variable if it is linearly independent, otherwise nothing.

## Theorems

An indexed set of vectors $\set{v_1, ..., v_n}$ with $v_1 \neq 0$ is **linearly dependent** $\iff$ some $v_{j>1}$ is a **linear combination** of the preceeding vectors $\set{v_1, ..., v_{j-1}}$.

# Bases

$H$ **subspace** of vector space $V$. A set of vectors $B = \set{b_1, ..., b_n}$ in $V$ is a **basis** for $H$ if:
- $B$ is **linearly independent**
- $H = Span \set{B}$

In other words, the **minimal set of vectors** that span $H$.

## Finding a Basis

### Basis for Null Space of Matrix $A$

- row reduce the matrix, we call $U$
- solve $Ux = 0$
- The solution in $\sum$ variable $\cdot$ vector form. (parametric form)
- $x \in Nul(A) \iff x \in Span \set{vectors}$
- These two vectors are the basis for the null space.

### Basis for Column Space of Matrix $A$

- Row reduce, call it U.
- look at columns where there are pivots (in the row reduced matrix) in the original matrix
- The set formed by these columns is the **basis** for the column space of $A$

## Random Bullshit

If $b \in \R^4$, how do i know if $b \in Col(A)$?

$\iff Ax = b$ consistent.

