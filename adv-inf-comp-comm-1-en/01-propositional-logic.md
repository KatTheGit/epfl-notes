## Propositional logic

A proposition is a **declarative sentence** that is **true** or **false**, noted $T$ or $F$.

Such a proposition can be expressed by a variable, represented by a letter, i.e. $p$.

## Compound propositions, logical connectives

A compound proposition is a set of propositions connected by logical connectives.

Below are some logical connectives:

NOTE: we are doing $p$ \<connective\> $q$

- ($\neg$) Negation (NOT)
    - Reverses the truth value.
- ($\land$) Conjunction (AND)
- ($\lor$) Disjunction (OR)
    - This is an INCLUSIVE or.
- ($\bigoplus$) Exclusive or (XOR)
    - "either this or that"
- ($\implies$) Implication
    - AKA **"if then"**
    - If p, then q's value. Otherwise true.
    - "If it rains tomorrow, I'll be unhappy".
        - If it rains, and I'm unhappy -> true
        - If it rains, and I'm happy -> false
        - If it does not rain, my statement was true
- ($\iff$) Biconditional (IFF)
    - If and only if. Something can only be true if the other thing is true. If that other thing is true, that means the first something was true too. Same with falseness.
    - A.K.A. "Are different"


## Truth Table

| $p$ | $q$ | | $\neg p$ | $p \land q$ | $p \lor q$ | $p \bigoplus q$ | $p \implies q$ | $p \iff q$
|--|--|--|--|--|--|--|--|--|
| T | T | | F | T | T | F | T | T
| T | F | | F | F | T | T | F | F
| F | T | | T | F | T | T | T | F
| F | F | | T | F | F | F | T | T

TRUTH NUKE!!!1!!

## Precedence of logical connectives

| Operator | Precedence |
|--|--|
| $\neg$ | 1 |
| $\land$ | 2 |
| $\lor$ | 3 |
| $\implies$ | 4 |
| $\iff$ | 5 |

## DNF

A disjunctive normal form is a conjunction if disjunctions, called **minterms**.

It can be constructed from a truth table by taking all true lines, and for each one, creating a minterm that is a disjunction of all variables, negated if they are false, and then creating a disjunction of all these minterms.

These can be constructed without a truth table.
1. Eliminate equivalences and implications
2. Move negations inward (to only be in front of variables)
3. Use distributive and associative laws.

## CNF.

A Conjunctive Normal Form is a disjunction of conjunctions, called **clauses**.

ALl clauses can be constructed from a truth table by taking all false lines, and creating a disjunction of all variables, this time negated only if true.