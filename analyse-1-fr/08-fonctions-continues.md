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


# Limites de Fonctions

Soit $x_0 \in \R$ et $f$ une fonction.

$f$ tend vers $L \in \R$ lorsque $x$ tend vers $x_0$

si pour tout $a > 0$ il existe $b > 0$ tel que

$|f(x)-L| \le a$ dès que $0 < |x - x_0| < b$

## Lemmes

la limite est unique.

## Théorème des Gendarmes

Si:
- $g(x) \le f(x) \le h(x) \quad \forall x$
- $\lim g(x) = \lim h(x) = L$

Alors:

- $\lim f(x) = L$

## Limite Latérale

si pour tout $a > 0$ il existe $b > 0$ tel que

- $f$ tend vers $L$ lorsque $x$ tend vers $x_0$ **par la droite**:
  - $|f(x)-L| \le a$ dès que $0 < x - x_0 < b$
- $f$ tend vers $L$ lorsque $x$ tend vers $x_0$ **par la gauche**:
  - $|f(x)-L| \le a$ dès que $-b < x - x_0 < 0$

On note $\displaystyle \lim_{x \to {x_0}^\plusmn}f(x) = L$

### Theorème

$\displaystyle \lim_{x \to x_0} f(x) = L \iff \lim_{x \to {x_0}^+} f(x) = \lim_{x \to {x_0}^-} f(x) = L$

## Propriétés

Valables pour $\displaystyle \lim_{x \to x_0}$, $\displaystyle \lim_{x \to {x_0}^+}$ et $\displaystyle \lim_{x \to {x_0}^-}$.

- $\lim (f + g) = \lim f + \lim g$
- $\lim (f \cdot g) = (\lim f) \cdot (\lim g)$
- Si $\lim g \neq 0$, $\lim \frac{f}{g} = \frac{\lim f}{\lim g}$
- Si $f(x) \le g(x)$ dans un voisinage de $x_0$, alors $\lim f \le \lim g$

## Cas spécifiques

### Indéterminations "$\frac{0}{0}$"

Une division de polynômes peut se factoriser.

On peut multiplier par le conjuqué. $\frac{a -b}{c} = \frac{a -b}{c} \cdot \frac{a + b}{a + b}$

### Trigo

- $\lim \frac{\sin x}{x} = 1$
- $\lim \frac{1 - \cos x}{x^2} = \frac{1}{2}$

### Exp Log

- $\lim \frac{\log(1 + x)}{x} = 1$
- $\lim \frac{e^x -1}{x} = 1$

## Limite Infinie (en un point)

- $\displaystyle \lim_{x \to {x_0}} f(x) = + \infin \space \space \iff \space \space \forall \space (M > 0) \space \space \exists \space (a > 0) \space \space | \space (f(x) \ge M$ dès que $0 \le |x - x_0 | < a)$
  - Pour $\displaystyle \lim_{x \to {x_0}^+}$: dès que $x_0 < x \le x_0 + a$ 
  - Pour $\displaystyle \lim_{x \to {x_0}^-}$: dès que $-b \le x < x_0$ 
- $\displaystyle \lim_{x \to {x_0}} f(x) = - \infin \space \space \iff \space \space \forall \space (m < 0) \space \space \exists \space (a > 0) \space \space | \space (f(x) \le m$ dès que $0 \le |x - x_0 | < a)$

### Propriétés

pour limites $x \to x_0$

- $g(x)$: bornée
- $g^*(x)$: bornée, nonzero
- $i(x)$: tend vers l'infini

alors

- $\lim \frac{1}{f(x)} = 0$
- $\lim (f + i) = +\infin$
- $\lim (f \cdot i) = +\infin$
- $\lim (f + g) = +\infin$
- $\lim \frac{g}{f} = 0$
- $\lim (f \cdot g) = +\infin$ (si $\lim g > 0$) et $= -\infin$ (si $\lim g < 0$)
- si $g \ge f$ dans un voisinage épointé de $x_0$, $\lim g = +\infin$

## Limites x Vers l'Infini

- $\displaystyle \lim_{x \to + \infin} f(x) = L \quad \forall \space (a > 0) \quad \exist \space (N > 0) \quad : \space |f - L| \le a$ dès que $x \ge N$
  - dès que $x \le N$ pour $\displaystyle \lim_{x \to - \infin}$
- $\displaystyle \lim_{x \to + \infin} f(x) = + \infin \quad \forall \space (M > 0) \quad \exist \space (N > 0) \quad | \space f(x) \ge M$ dès que $x \ge N$
  - t.q. $f(x) \le M$ pour $\displaystyle \lim_{x \to + \infin} = -\infin$
  - dès que $x \le N$ avec $N < 0$ pour $\displaystyle \lim_{x \to - \infin}$
