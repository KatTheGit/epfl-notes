# Relations

## Binary relation

A **binary relation** from $A$ to $B$ is a subset belonging to $A \times B$ ([cartesian product](./04-sets.md#cartesian-product)).

## Functions

A function ca be represented as a subset of $A \times B$ (a relation).

A function$A \to B$ contains one and only one ordered pair $(a, b)$ for every element $a \in A$.

A relation can be from $A \to A$, said "on set $A$"

## Reflexive

On set $A$

$(a, a) \in R \space \space \forall a \in A$

## Symmetric

$(a, b) \in R \implies (b, a) \in R \quad \forall a, b \in A$

## Antisymmetric

$(a, b) \in R \land (b, a) \in R \implies a = b \quad \forall a \forall b$

## Transitive

$(a, b) \in R \land (b, c) \in R \implies (a, c) \in R$

## Composite relations

Relations $R: A \to B$ and $S: B \to C$.

$S(R) = S \circ R = \set{(a, c) : \exists b \in B | (a, b) \in R \land (b, c) \in S}$

## Equivalence relations

- reflexive
- symmetric
- transitive

elements $a, b$ related by equivalence relation arenoted $a \sim b$

## Equivalence classes

$R$ equivalence relation on $A$.

**Equivalence class** is the set of all elements related to an element $a$.

$[a]_R = \set{s | (a, s) \in R}$

## Partition of a set

A partition of $S$ is a collection of **disjoint** (different) subsets, that have $S$ as their union.

## Partial Ordering

a partial ordering of $R$ on $S$, noted $(R, S)$



- reflexive $(a, a) \forall a$
- antisymmetric $(a, b), (b, a) \implies a = b$
- transitive $(a, b), (b,c) \implies (a,c)$

Called a poset.

$\preceq$ used to show ordering relation in arbitrary poset.

### Comparability

Two elements from a poset are comparable if we can write $a \preceq b$. If not they are incomparable.

### Total Order

Every element is comparable

### Well Ordered


## Partial ordering on Cartesian Product

**Lexographic Ordering** on $A_1$ and $A_2$ is defined as $(a_1, a_2) \preceq (b_1, b_2$).

if $a_1 \preceq b_1$ or ($a_1 = b_1$ and $a_2 \preceq b_2$ ).

AKA **Dictionary Ordering**.

## Formal Power Sum

An expression of the form

$A(x) = \displaystyle \sum_{n=0}^{\infin} a_n x^n$

$a_n$ are coefficients.

It is *formal* because "we are not concerned if this infinite sum converges." (aka it is finite)

- $A(x) + B(x) = \displaystyle \sum_{n=0}^{\infin} (a_n + b_n) x^n$
- $A(x)B(x) = \displaystyle \sum^{\infin}_{n= 0} \sum_{k=0}^{n} (a_k \cdot b_{n-k}) x^n$

### Generating function

If we encode a sequence $a_0, a_1, a_2$