# Proofs

## Arguments

An argument form is a logical structure containing **premises** and **a conclusion**. It is valid if the premises imply the conclusion. If valid, it is true for every proposition in the propositional variables.

An argument can be written as such:

$a$ (premise 1) <br>
$a \implies b$ (premise 2) <br>
$-----$ <br>
$\therefore b$ (conclusion) <br>

Whenever all premises are true, the conclusion is true.

### Inference rules

Inference rules are specific argument forms that are useful. They have been proven already and can be used freely. There will be a cheat sheet with these in the exam.

## Proving theorems

- lemma: helping theorem
- corollary: direct result following from a theorem
- proposition: less important theorem
- conjecture: thing proposed to be true. Once true, becomes a theorem.

### a -> b proofs

We need to show that $b$ is true, if $a$ is true.

If we know $a$ is false then $a \to b$ is true. (Vacuous proof)

### Direct proof

Directly prove $a \to b$ using theorems, axioms, etc.

### Indirect: proof by contraposition

Assume $\neg b$, show $\neg a$.

$a \to b \equiv \neg b \to \neg a$

### Indirect: proof by contradiction (AKA by absurdity)

Assume that $a$ and $\neg b$ are true.

Then through a direct proof show: $a \land \neg b \to False$, since $a \to b \equiv (a \land \neg b) \to False$

### Proof by cases

Prove something in individual cases. Can be individual elements, can be ranges, whatever.

Such a proof is exhaustive if it is done for every element.

### Counterexample

To disprove $\forall x P(x)$, we can prove $\exists x \neg P(x)$

### Equivalence

$a \iff b \equiv (a \to b) \land (b \to a)$

### Existence

$\exists x P(x)$

- Constructive: Find $c$ such that $P(c)$
- Nonconstructive: Prove $\neg \exists x P(x) \to False$ (proof by contradiction)

### Uniqueness proof

$\exists !x P(x)$

1. Show $\exists x P(x)$.
2. Show if $x$ and $y$ satisfy $P$, $x = y$

$$