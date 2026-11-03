# Fonctions Continues

## Continuité

$f$ est dite **continue** en $x_0$ si $\displaystyle \lim_{x \to x_0} f(x) = f(x_0)$.
- Si la limite n'éxiste pas ou n'est pas = à $f(x_0)$, $f$ est **discontinue**.

Autrement dit, $\forall \space (a>0) \quad \exists \space (b > 0) \quad : (|x-x_0| \le b \implies |f(x) - f(x_0)| \le a)$

## Fonctions élémentaires

- Polynomes sont continus
- fonctions trigo sont continues, et tan est continue sur $\R \setminus \set{\frac{\pi}{2} + \pi k, k \in \Z}$
- base a > 0, toute exponentielle continue.
- base a > 0, tout logarithme continue sur $\R^*_+$

## Continuité Latérale

- $f$ continue à **gauche** en $x_0$ si $\displaystyle \lim_{x \to {x_0}^-} f(x) = f(x_0)$.
- $f$ continue à **droite** en $x_0$ si $\displaystyle \lim_{x \to {x_0}^+} f(x) = f(x_0)$.

Si $f$ est continue à gauche et à droite en $x_0$ alors elle est continue en $x_0$.

## Prolongée

Si une fonction part d'un domaine qui exclut $x_0$, elle est discontinue, mais on peut la rendre continue en définissant $f(x_0)$ en utilisant une valeur semblable que dans le voisinage. $\displaystyle f(x_0) := \lim_{x \to x_0} f(x)$. Cette nouvelle fonction s'apelle la **prolongée par continuité**.

## Continuité sur un Intervalle Compact

$f: [a, b] \to \R$ est **continue** si:
- continue $\forall \space x_0 \in ]a, b[$
- continue à droite en $x_0$ = a
- continue à gauche en $x_0$ = b

$f: [a, b] \to \R$ continue alors $f$ est bornée.

## Maximum, Minimum

$f: [a, b] \to \R$ continue alors elle atteint:
- $\displaystyle \min_{x \in [a, b]} f(x) = f(x_*)$
- $\displaystyle \max_{x \in [a, b]} f(x) = f(x^*)$

## Théorème des Valeurs Intermédiaires.

Soit $f: [a, b] \to \R$ continue.

Si $f(a) < f(b)$, pour toute valeur $h$, $f(a) < h < f(b)$ alors $\exists \space c \in ]a, b[ \quad | f(c) = h$.

## Image de Fonction Bornée

Soit $f: [a, b] \to \R$ continue.

Alors $\displaystyle Im(f) = [\min_{x \in [a, b]} f(x), \max_{x \in [a, b]} f(x)]$

## Theorème 2

Pour un $x_0$ qui peut être $\infin$,

Si $\displaystyle \lim_{x \to x_0} g(x) = y_0$

Alors $\displaystyle \lim_{x \to x_0} f(g(x)) = f(y_0)$