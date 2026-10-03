# Sets

A set is an unordered collection of objects.
- Objects are called **elements**.
- A set **contains** elements.
- $a \in A$ means a is an element in set A
- $a \not \in A$ means a is **not** an element in set a

Order is not important and neither is repetition.

Sets of numbers are sets, like $\N, \Z, \R$.

## Notation

- Explicit (Roster method): $V = \{a, e, i, o, u\}$
- Set Builder Notation: $\{x | P(x)\}$.
  - $P(x)$ can be natural language or predicate logic.
- Interval Notation: $[a, b]$ or $(a, b]$, with "(" being an open interval.

### Set members

Sets can be members of other sets.

### Empty set

- No elements
- AKA null set
- Noted $\empty = \{\}$

### Singleton set

- One element

### Universal set

Often noted $U$, contains everything under consideration.

## Venn Diagram

- Universal set $U$ is a rectangle (the frame)
- Sets are circles
- Elements are points.

## Subsets

A is a **subset** of B $\iff$ Every element of A is an element of B. Here B is the **superset** of A.

- $A \sube B$, A subset B
- $B \supe A$, B superset A

### Proof

A subset B $\iff \forall x (x \in A \implies x \in B)$

To prove the opposite, find a counterexample.

### Proper subset

- $A \sube B$ but $A \not = B$, A is a **proper subset** of B.
  - Written $A \subset B$
  - $\forall x (x \in A \implies x \in B) \land \exists x (x \in B \land x \not \in A)$

### Equal sets

- $A = B$
- $\forall x (x \in A \iff x \in B)$

### Power set

The set of **all** subsets of set $A$, denoted $\mathcal P (A)$. Called the **power set** of A.
- Includes all possible combinations + the null set because the null set is always a subset.

## Tuple

- **ordered n-tuple** is the ordered collection of n elements, with $(a_1, a_2, ..., a_n)$.
- 2-tuples are called **ordered pairs**.

## Cartesian product

$A \times B$
- $A \times B = \{(a, b) | a \in A \land b \in B\}$
- $A \times B \not = B \times A$
- $(A \times B) \times C \not = A \times B \times C$

## Truth Set

With predicate $P$ and domain $D$, we define **truth set** of $P$ to be all elements of $D$ for which $p(x)$ is true.

- $\set{ x \in D | P(x)}$

## Cardinality

Number of **distinct** elements. Noted $|S|$
- If set has $n$ elements, $|\mathcal P (n)| = 2^n$
- If $|A| = n$ and $|B| = n$, then $|A \times B | = n \cdot m$.

## Union

- Noted $A \cup B$
  - $\set{x | x \in A \lor x \in B}$
- $A \cup (B \cup C) = (A \cup B) \cup C$, same with intersection. So no brackets needed

## Intersection

- Noted $A \cap B$
  - $\set{x | x \in A \land x \in B}$
  - If this set is empty, $A$ and $B$ are said to be **disjoint**.

### Generalised

$\displaystyle \bigcup_{i = 1}^n A_i = A_1 \cup A_2 \cup ... \cup A_n$.

Same with intersections.

### Cardinality of set union

$| A \cup B | = |A| + |B| - |A \cap B|$

## Difference

$A - B$
- $A - B = \set{x | x \in A \land x \not \in B}$
- Aka **complement** of B with respect to A

## Complement

Complement of $A$ with respect to $U$, noted $\overline A$
- $\overline A = U - A = \set{x \in U | x \not \in A}$

## Symmetric difference

$A \bigoplus B = (A - B) \cup (B - A)$
  - In venn diagram, both sets colored except intersection.

# Functions

$A, B$ are nonempty sets.

 $f: A \to B$

$f(a) = b$

- $f$ maps $A$ to $B$
- $A$ is the domain of $f$
- $B$ is the codomain of $f$
- $a$ is the preimage of $b$
- $b$ is the image of $a$
- range of $f$ is the set of all images of points in $A$, noted $f(A)$.
  - Always subset of codomain.
- $S \sube A \implies f(S) = \set{f(s) | s \in S}$

## Adding & Multiplying

Only if both functions are both integer-valued (codomain is integers) or both real-valued.

- $(f_1 + f_2) (a) = f_1(a) + f_2(a)$
- $(f_1 \cdot f_2) (a) = f_1(a) \cdot f_2(a)$

## Injection

Function is said to be **injective** or **one-to-one** iff:

$f(a) = f(b) \implies a = b$

## Surjection

Function is said to be **surjective** or **onto** iff:

$\forall b \in B \space \space \space \exist a \in A  \space | \space f(a) = b$

## Bijection

A function is **bijective**, or a **one-to-one correspondence**, if it is both injective and surjective.

### Inverse

$B \to A$

$f^{-1}(y) = x \iff f(x) = y$

Must be bijective.

## Partial Functions

A partial function $A \to B$ is a mapping of **some** elements of $A$, in other word a mapping of all elements of a subset of $A$. This subdomain is called the **domain of definition of $f$**.

$f$ is said **undefined** for elements that are not in the domain of definition.

$f$ is a **total function** if the domain of definition is the same as the domain.