# Séries

Une somme infinite d'une suite.

## Definition

On définit $(s_n)_{n \ge 0}$, la suite des sommes partielles associée à $(a_n)_{n \ge 0}$

### Limite

Si $\displaystyle s:= \lim_{n \to \infin} s_n$ existe, on dit que la série **converge**, et que sa **somme vaut s**.

Si la somme tend vers l'infini, on dit que la série diverge.

## Propriétés

Si $\sum_n a_n$ converge, alors $a_n \to 0$

Soient $\displaystyle \sum_n a_n$ et $\displaystyle \sum_n b_n$ convergentes.

- $\displaystyle \sum_n a_n + \sum_n b_n = \sum_n (a_n + b_n)$ est convergente.
- $\displaystyle \lambda \sum_n a_n = \sum_n \lambda a_n$ est convergente.
- $\displaystyle \sum_n (\alpha a_n + \beta b_n) = \alpha \sum_n a_n + \beta \sum_n b_n$

## Critère de Comparaison

Si $0 \le a_n \le b_n$

1. Si $s_b$ converge, alors $s_a$ converge aussi.
2. Si $s_a = + \infin$ alors $s_b = + \infin$

## Le Critère de Leibniz

Voiyons ce que veut nous dire le Dr. Pangloss...

Soit $a_n = (-1)^n \cdot (x_n)_{n \ge 0}$
- $x_n$ décroissante, tend vers 0.

Alors 
$\displaystyle \sum_{n \ge 0} a_n$ converge.

## Série Téléscopique

Une série dans laquelle le terme général est une différence.

$a_n = x_n - x_{n-1}$

## Séries $\frac{1}{n^p}$

$\displaystyle \sum_ {n \ge 1} \frac{1}{n^p}$
- converge si $p > 1$
- $= + \infin$ si $p \le 1$

## Critère de la Limite du Quotient

Si:
- $a_n > 0$
- $b_n > 0$ pour $n$ suffisamment grand
- $\displaystyle \lim_{n \to \infin} \frac{a_n}{b_n} > 0$ existe

Alors soit $s_a$ et $s_b$ convergent toutes les deux, soit elles divergent toutes les deux.

## Convergence Absolue

Si $\displaystyle \sum_n |a_n|$ converge, on dit que $\displaystyle \sum_n a_n$ est absolument convergente.

Si une somme converge absolument, alors elle converge.

## Critère de d'Alembert

Soit $(a_n)$ pour laquelle $\displaystyle p := \lim_{n \to \infin} |\frac{a_{n+1}}{a_n}|$ exite ou est $+ \infin$

1. Si $p < 1$ alors $s_a$ converge absolument
2. Si $p > 1$ alors $s_a$ diverge

## Critère de Cauchy

Soit $(a_n)$ pour laquelle $\displaystyle p := \lim_{n \to \infin} \sqrt[n]{|a_n}$ exite ou est $+ \infin$

1. Si $p < 1$ alors $s_a$ converge absolument
2. Si $p > 1$ alors $s_a$ diverge

