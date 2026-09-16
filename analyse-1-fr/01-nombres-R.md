# Nombres Réels

$\N := \{0, 1, 2, 3,...\}$ (nombres naturels)

$\Z := \{..., -2, -1, 0, 1, 2,...\}$ (entiers relatifs)

$\mathbb{Q} := \{ \frac{p}{q}: p, q \in \Z, q \neq 0\}$

$\R = \mathbb{Q}$ + irrationels

## Règles de calcul

L'ensemble des réels est un ensemble dans lequel on peut faire de l'arithmétique, c'est-à-dire utiliser des operations. ($+$, $-$, $*$, $\div$). Un tel ensemble est appelé un **corps**.

### L'Addition:

Associe deux réels $x$, $y$ à un nouveau réel noté $x + y$

1. $x+y = y + x \space \space \forall x, y \in \R$
2. $x + (y + z) = (x + y) + z \space \space \forall x, y, z \in \R$
3. $\exist 0 \in \R$ appelé **élément neutre pour l'addition** $: x + 0 = 0 + x = 0 \space \space \forall x \in \R$
4. $\forall x \in \R, \exists -x \in \R$, appelé **opposé** de $x$, $: x + (-x) = 0$.
5. Ainsi si $x, y \in \R, x - y:= x + (-y)$

### La Multiplication

Associe deux réels $x, y$ à un nouveau réel noté $x * y$.

1. $x * y = y * x$
2. $x * (y * z) = (x * y) * z$
3. $x * (y + z) = x * y + x * z$
4. $\exists \space 1 \in \R,$ **élément neutre de la multiplication** $: 1 * x = x * 1 = x \space \space \forall x \in \R$
5. $\forall x \in \R, \exist x^{-1}$, appelée l'inverse de $x$, $:x*x^{-1} = 1$
6. si $x, y \in \R, y \neq 0$, on peut définir leur division: $x \div y := x * y^{-1}$

## Ordre


Propriétés (toutes les variables ci-dessous sont des réels):

1. $x \leq y, y \leq x <=> x = y$
2. $x \leq x$
3. $a \leq b, b \leq c <=> a \leq c$
4. $a \leq b <=> a + c \leq b + c$, on a donc $x \leq y, s \leq t <=> x+s\leq y+t$
5. $0 \leq a, 0 \leq b <=> 0 \leq a * b$

## Intervalles

$[a, b] := \{x\in \R : a \leq x \leq b\}$ <br>
$[a, b[ := \{x\in \R : a \leq x < b\}$ <br>
$]a, b] := \{x\in \R : a < x \leq b\}$ <br>
$]a, b[ := \{x\in \R : a < x < b\}$

