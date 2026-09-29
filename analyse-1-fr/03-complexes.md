# Nombres complexes

Un ensemble noté $\mathbb{C}$ de paires de réels munis des opérations suivantes.

On définit $x = (a, b)$ et $y = (c, d)$

- Addition:
$$x + y := (a + c, b + d)$$
- Multiplication:
$$x \cdot y := (ac - bd, ad + cb)$$

Avec ces opérations, $\mathbb{C}$ devient un **corps**.

## Propriétés des opérations

Sans spécification additionelle, ces propriétés sont vraies pour tous $x, y, z \in \mathbb{C}$

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

## Nombre i

$i := (0, 1)$

On remarque

$(-i)^2 = i^2 = (0, 1) \cdot (0, 1) = (-1, 0) = -1 \in \R$

Donc i et -i sont solutions de $x^2 + 1 = 0$. Dans $\mathbb{C}$, ce polynôme peut être factorisé ($(z-i)(z+i)$), ce qui n'est pas le cas dans $\R$.

I étant un complexe dont le carré vaut -1, on peut (abusamment) noter:

$i \equiv \sqrt{-1}$

### Partie réelle, partie imaginaire

$z = (x, y) = (x, 0) + (0, y) = (x, 0) + (0, 1)y = x + iy$.

- $Re(z) := x$, aka partie **réelle**
- $Im(z) := y$, aka partie **imaginaire**

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

### Résoudre une équation simple

Exemple d'equation: $z-3\mathsf{i}z -3+6\mathsf{i}=0$

- Isoler z, faire la division à l'aide du conjuqué
- Poser $z = a + bi$, et injecter. On a donc un systeme de deux équations (une réelle, une imaginaire)