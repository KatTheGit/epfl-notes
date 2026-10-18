# Vector Spaces, Subspaces

## (real) Vector Space

A non-empty set equipped with
- addition
- multiplication

The following axioms are satisfied, for a vector space $V$:
- $\vec a + \vec b = \vec b + \vec a$
- $\vec a + (\vec b + \vec c) = (\vec a + \vec b) + \vec c$
- $\exists \vec 0 \in V\quad |\quad \vec u + \vec 0 = \vec u$
- $\forall \vec u \in V \space \space \exist \vec{-u} \space \space|\space \space \vec u + (\vec{-u}) = 0$
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

