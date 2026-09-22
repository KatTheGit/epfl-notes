# Suites (réelles)

Une famille ordonnée de réels, indexée par des entiers.

Notée $(a_n)_{n \geq n_0}$ pour une suite commençant par un indice $n_0$. Sans indice de départ, notée simplement $(a_n)$

Les suites peuvent etre représentées par le graphe d'une fonction.

$f: \N^* \to \R$ <br>
$\space \space \space \space n \mapsto f(n) := a_n$

## Expressions

Explicite: Exprime comment le $n$ème terme se calcule en fonction de $n$.

Par récurrence: Exprime comment le $n$ème terme se calcule en fonction du $(n-x)$ème terme.

## Bornes

Une fonction est
- majorée si il existe $M$ t.q. $a_n \leq M \forall n$
- minorée si il existe $M$ t.q. $a_n \geq M \forall n$
- bornée si les deux.

## Suites Monotones

Une suite est:
- **croissante** si $a_n \leq a_{n+1} \forall n$
- **strictement croissante** si $a_n < a_{n+1} \forall n$
- **décroissante** si $a_n \ge a_{n+1} \forall n$
- **strictement décroissante** si $a_n > a_{n+1} \forall n$

De plus, si une suite satisfait une de ces propretés, elle est dite **monotone**.

## Limite

Soit $L \in \R$. On dit qu'une suite $(A_n)$ tend vers $L$ (lorsque $n \to \infin$) si pour tout $a > 0$ il existe $N \in \N (qui dépend de $a$) $: |a_n - L| \le a$ pour tout $n \ge N$.

Autrement dit $a_n \in [L -a, L+a], \forall n \ge \N$.


$\displaystyle\lim_{n\to\infty}a_{n}=L$

Lorsque ce L existe, et $a_n$ tend vers L, on dit qu'elle converge, sinon qu'elle diverge.

## Propriétés des Limites

1. Si une suite est convergente, sa limite est unique.
2. Si une suite converge, alors elle est bornée.
3. Si $a_n \to L$ alors $|a_n| \to |L|$
4. $\displaystyle\lim_{n\to\infty}(a_n + b_n) = \displaystyle\lim_{n\to\infty}a_n + \displaystyle\lim_{n\to\infty}b_n$
5. $\displaystyle\lim_{n\to\infty}(a_n * b_n) = \displaystyle\lim_{n\to\infty}a_n * \displaystyle\lim_{n\to\infty}b_n$
6. $\displaystyle\lim_{n\to\infty}(a_n / b_n) = \displaystyle\lim_{n\to\infty}a_n / \displaystyle\lim_{n\to\infty}b_n$
7. Si $a_n \le b_n \space \forall n$ suffisament grand, $L_a \le L_b$

## Théorème des deux gendarmes

Soit $(x_n)$ une suite, et $(a_n), (b_n)$ deux suites telles que $(a_n) \le (x_n) \le (b_n) \space \forall n$ suffisamment grand, et que $\displaystyle\lim_{n\to\infty}a_n = \displaystyle\lim_{n\to\infty}b_n = L$, ALORS:

$(x_n)$ converge, et $\displaystyle\lim_{n\to\infty}x_n = L$.

En consquent si $(x_n)$ est bornée et $y_n \to 0$, $x_ny_n = 0$ 

## Monotone et bornée

Une suite convergente est forcément bornée.

Si une suite est bornée et monotone, alors elle converge. Autrement dit elle converge si:
- Croissante et majorée
- Décroissante et minorée

## Suite divergentes (vers l'infini)

1. $\displaystyle\lim_{n\to\infty}a_n = + \infin$ si $\forall M > 0$ il existe $N_0 \in \N$ (qui dépend de M) tel que $a \ge M \space \space \forall n \ge N_0$ 
1. $\displaystyle\lim_{n\to\infty}a_n = - \infin$ si $\forall M < 0$ il existe $N_0 \in \N$ (qui dépend de M) tel que $a \le M \space \space \forall n \ge N_0$ 

### Propriétés

Soient $(a_n), (b_n)$ deux suites avec $a_n \to + \infin$

1. $1/a_n \to 0$
2. $b \to \infin$ alors $a_n + b_n \to \infin$ et $a_n b_n \to \infin$
3. Si $b_n$ bornée, $a_n + b_n \to \infin$, et $b_n / a_n \to 0$
4. Si $\exist c : b_n \ge c \space \forall n$ suffisamment grand, alors $b_n a_n \to \infin$
5. Si $b_n \ge a_n \forall n$ suffisamment grand, $b_n \to \infin$

## Comportement de polynomiaux, logarithmes et exponentielles

$a, b > 0$ et $c, d > 1$

$\lim_{n\to\infty}\frac{n^{a}}{d^{n}}=0$


$\lim_{n\to\infty}\frac{\bigl(\log_{c} (n)\bigr)^{b}}{n^{a}}=0$