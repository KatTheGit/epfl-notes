# Predicate logic

Involves variables and predicates.

- "x is a mammal"
  - x: variable
  - is a mammal: predicate

We can make these statements into propositional functions, P(x). Once a value to the variable x is assigned, P(x) becomes a proposition.

## Universe of discourse

Truth value P(x) depends on x. We define a domain U, from which x comes from. i.e. all animals.

## Predicates and Propositional Logic

Connectives can be applied to predicates

We can construct expressions (P(x)) from predicates and logical connectives containing vatriables.

## Quantifiers

Quantifiers express to which extent a propositional fanction is True over the values of the domain $U$ of its variables.

### 1. Universal quantifier

P(x) is true for all x in U. Domain must always be specified!

- written $\forall x P(x)$
- $\forall$ is **universal quantifier**

### 2. Existential quantifier

There exists x in U such that P(x)

- $\exist x P(x)$
- $\exist$ called **existential quantifier**

A specific x that is true is called a **witness**.

### 3. Uniqueness quantifier

There exists a unique x in U for which P(x)

- $\exist ! x P(x)$
- $\exist!$ is **uniqueness quantifier**

### Quantifiers over finite domains

$\forall$ is the same as a conjunction.

$\exist$ is the same as a disjunction.

### Validity

A statement with predicates is:
- **valid** if true for all domains
- **satisfiable** if true for some domains
- **unsatisfiable** if always false.