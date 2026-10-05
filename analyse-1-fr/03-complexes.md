# Nombres complexes

Un ensemble noté $\mathbb{C}$ de paires de réels munis des opérations suivantes.

On définit $x = (a, b)$ et $y = (c, d)$

- Addition:
$$x + y := (a + c, b + d)$$
- Multiplication:
$$x \cdot y := (ac - bd, ad + cb)$$

Avec ces opérations, $\mathbb{C}$ devient un **corps**.

<br>
<br>

## Propriétés des opérations

On définit (quelconques) $x, y, z \in \mathbb{C}$

1. $x + y = y + x$
2. $x + (y + z) = (x + y) + z$
3. **élément neutre pour l'addition**: $(0, 0)$ puis-ce que $x + (0, 0) = x$
4. $\forall x \in \mathbb{C}$, il existe un unique $-x \in \mathbb{C}$ tel que $x + (-x) = 0. \quad -x = (-1, 0) \cdot x$
5. $x \cdot y = y \cdot x$
6. $x \cdot (y \cdot z) = (x \cdot y) \cdot z$
7. $x \cdot (y + z) = x \cdot y + x \cdot z$
8. **élément neutre pour la multiplication**: $(1, 0)$, puis-ce que $x \cdot (1, 0) = x$
9. Pour tout $x \in C, x \neq (0, 0), \exist !$ élément appelé **inverse**, noté $x^{-1}$, tel que:
   1.  $x * x^{-1} = (1, 0)$
   2.  $x = (a, b) \space$ alors $\space x^{-1} = \big( \frac{a}{a^2 + b^2}, \frac{-b}{a^2 + b^2} \big)$

Il n'y a pas d'ordre total sur $\mathbb{C}$.

Les nombres complexes de forme $(x, 0)$ se comportent comme des nombres réels.

<br>
<br>

## Nombre i

$i := (0, 1)$

On remarque

$(-i)^2 = i^2 = (0, 1) \cdot (0, 1) = (-1, 0) = -1 \in \R$

Donc i et -i sont solutions de $x^2 + 1 = 0$. Dans $\mathbb{C}$, ce polynôme peut être factorisé ($(z-i)(z+i)$), ce qui n'est pas le cas dans $\R$.

I étant un complexe dont le carré vaut -1, on peut (abusamment) noter:

$i \equiv \sqrt{-1}$

### Partie réelle, partie imaginaire

$z = (x, y) = (x, 0) + (0, y) = (x, 0) + (0, 1)y = x + iy$.

- $Re(z) := x$, partie **réelle**
- $Im(z) := y$, partie **imaginaire**

On a:

- $Re(x) + Re(y) = Re(x + y)$
- $Im(x) + Im(y) = Im(x + y)$

### Conjuqué, module

Soit $x = a + bi$

- Complexe conjugué: $\overline x = a - bi$
- Module: $|x| = \sqrt{a^2 + b^2}$

D'où:

1. $\overline{\overline{x}}=x$
2. $x=\overline{x}$ si et seulement si $x\in \mathbb{R}$
3. $\overline{x+y}=\overline{x}+\overline{y}$
4. $\overline{xy}=\overline{x}\overline{y}$
5. $x\overline{x}=|x|^{2}$
6. $|\overline{x}|=|x|$
7. $\overline{(\frac{x}{y})}=\frac{\overline{x}}{\overline{y}}$
8. $\frac{x+\overline{x}}{2}=\operatorname{Re}{x}$
9. $\frac{x-\overline{x}}{2\mathsf{i}}=\operatorname{Im}{x}$

Pour aider dans une division, on peut multiplier et diviser par le conjuqué, ce qui aide souvent à isoler les parties réelles et imaginaires.

### Inverse

$z^{-1}= \frac{\overline z}{|z|^2}$

### Résoudre une équation simple

Exemple d'equation: $z-3\mathsf{i}z -3+6\mathsf{i}=0$

- Isoler z, faire la division à l'aide du conjuqué
- Poser $z = a + bi$, et injecter. On a donc un systeme de deux équations (une réelle, une imaginaire)

<br>
<br>

## Plan Complexe

On représente un nombre complexe dans un **plan complexe**,
- $O_x$ axe **réel**
- $O_y$ axe **imaginaire**

### Représentation polaire

- $r$: $|z|$
- $\theta$: angle par rapport à $O_x$

Pour $z = x + iy$

- $x = Re(z) = r \cdot cos \theta$
- $y = Im(z) = r \cdot sin \theta$

D'où **forme polaire**: $z = r(cos \theta + i \cdot sin \theta)$

$\theta$ est **l'argument** de $z$, noté $Arg(z)$. $tan \theta = \frac{y}{x}$. L'argument est $2 \pi$ périodique.

- $Arg(\overline a) = - Arg(a)$
- $Arg(ab) = Arg(a) + Arg(b)$
- $Arg(\frac{a}{b}) = Arg(a) - Arg(b)$
- $Arg(a^n) = n \cdot Arg(a)$

Soient $w, z \in \mathbb{C}$

- Pour $w \cdot z$
  - module $= |z| * |w|$
  - argument $= Arg(z) + Arg(w)$

Do'ou on obtient la

### Formule de Moivre

$z^n = r^n (cos(n \theta) + i \cdot sin (n \theta))$

<br>
<br>

## Exponentielle

$e^z = e^{Re(z)} \cdot (cos[Im(z)] + i \cdot cos[Im(z)])$

- $e^a \cdot e^b= e^{a + b}$
- $|e^a| = e^{Re(a)}$
- $Arg(e^z)= Im(z)$
- $e^z = e^{ z + i \cdot 2k \pi }$

Pour $yi$ (nombre purement imaginaire):

- $e^{iy} =cos (y) + i \cdot sin (y)$

On a:

- $|e^{iy}| = 1$
- $\overline{e^{iy}}=e^{i(-y)}$
- $e^{ia} \cdot e^{ib} = e^{i(a+b)}$
- $\frac{e^{ia}}{e^{ib}} = e^{i(a - b)}$
- $sin(y) = \frac{e^{iy} - e^{-iy}}{2i}$
- $cos(y) = \frac{e^{iy} + e^{-iy}}{2}$

On a particulièrement:

- $e^{i \frac{\pi}{2}} = i$
- $e^{i \cdot 2k \pi}= 1$
- **Formule d'Euler**: $e^{i \pi} = -1$

<br>
<br>

## Représentation Polaire (exponentielle)

$z = r e^{i \theta} \quad = |z|e^{i \cdot Arg(z)}$

Formule de Moivre:

$z^n = r^n e^{i \cdot n \theta}$

<br>
<br>

## Racines

Racines d'un complexe: $\set{\sqrt[n]{r} \cdot e^{i \frac{\theta + 2k \pi}{n}} | k = 0, 1, 2, ..., n-1}$

<br>
<br>

## Theorème Fondamental de l'Algèbre

Soit un polynôme de degré n:

$P(z) = a_0 z^0 + a_1 z^1 + ... + a_n z ^n$

Dans $\mathbb{C}$, tout polynôme de degré > 0 possède **au moins une racine**. ($P($racine$) = 0$).

### Conséquences

Soit $P$ de degré n > 0 et $z_0$ un complexe fixé. Alors $\exists !$ Q de degré $n-1$ | 

$P(z) = (z - z_0) \cdot Q(z) + P(z_0)$

Si $z_0$ est une racine, on trouve:

$P(z) = (z - z_0) Q(z)$

## Factorisation (de Polynômes)

Soit un polynôme de degré n:

$P(z) = a_0 z^0 + a_1 z^1 + ... + a_n z ^n$

Il possède $n$ racines, et peut se factoriser: $P(z) = (z - z_0)(z-z_1)...(z-z_n)$.

### Cas d'une equiation de 2nd degré

Equation de la forme: $az^2 + bz + c = 0$ avec $a, b, c \in \mathbb{C}, a \not = 0$

- $z = \frac{-b \plusmn \sqrt{b^2 - 4ac}}{2a}$
- Insérer $a + bi$, trouver les zeros.

###  Plusieures racines identiques

Si un complexe a plusieures racines identiques, cette racine est dite de multiplicité $n$. Aurement dit:

Si $n_*$ est le plus grand entier tel que $(z-z_*)^{n_*}$ divise $P$, $z_*$ est une racine de multiplicité $n_*$

On peut réecrire: $P(z)=a_{n}(z-z_{i_1})^{n_1}(z-z_{i_2})^{n_2}\cdots(z-z_{i_k})^{n_k}$, ainsi nos racines sont distinctes.

### Polynôme Réel

Soit $P(z)$ un polynôme dont tous les coefficients sont réels. Si $z_*$ est une racine...

- $P(\overline{z_*}) = 0$

D'où:

Si $P$ est de degré impair, ill possède au moins une racine réelle.

### Factorisation Polynôme Réel

Tout polynôme à coefficients réels $P(x)$ peut se factoriser en un produit de polynômes irréductibles de degré $1$ ou $2$, à coefficients réels eux aussi.

### Méthode Générale de Factorisation

- Trouver une première racine
- Faire la division euclidienne par cette racine
- Repeat