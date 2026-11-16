# Eigen-stuff

## Eigenvector

- $A$ an $n \times n$ **matrix**.
- $\lambda \in \R$ a **scalar**

An **eigenvector** of $A$ is a nonzero **vector** $x \in \R^n$ s.t.

$Ax = \lambda x$

For some $\lambda$, called **eigenvalue** of $A$. $x$ is called an eigenvector corresponding to $\lambda$.  

## Eigenspace

A is an $n \times n$ matrix, $\lambda$ an eigenvalue of $A$.

The **eigenspace** of $A$ **corresponding to** $\lambda$ is the subspace

$E_{\lambda} = \set{x \in \R^n | Ax = \lambda x} \sub \R^n = Nul(A - \lambda I_n)$ (Set of all eigenvectors of an eigenvalue.)

## Properties, Theorems

### 1

The eigenvalues of a triangular matrix are the entries on its main diagonal.

### 2

An $n \times n$ matrix is invertible $\iff$ $0$ is not an eigenvalue of that matrix.

### 3

A set of **eigenvectors**, each corresponding to distinct eigenvalues of a matrix, is a linearly independent set.

## Eigenvalue of Linear Transformation

### Formal Definition of an Eigenvector

- $V$ a vector space
- $T: V \to V$ a lintrans
- $v \in V$ non-zero vector
- $\lambda$ scalar

$v$ is an **eigenvector** of $T$ if $t(v) = \lambda v$ for some **eigenvalue** of $T$ $\lambda$.

### Eigenspace

The eigenspace of $T$ **corresponding** to $\lambda$ is:

$\set{v \in V | T(v) = \lambda v} = Ker(T - \lambda \cdot id_V)$

## Characteristic Polynomial

- $A$ a $n \times n$ matrix
- $\lambda$ a scalar.

$\lambda$ is an **eigenvalue** of $A \iff \lambda$ satisfies the **characteristic equation**:

$det(A - \lambda I_n) = 0$.

