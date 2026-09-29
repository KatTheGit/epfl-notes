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

Soit $L \in \R$. On dit qu'une suite $(a_n)$ tend vers $L$ (lorsque $n \to \infin$) si pour tout $b > 0$ il existe $N \in \N$ (qui dépend de $b$) $: |a_n - L| \le b$ pour tout $n \ge N$.

Autrement dit $a_n \in [L -b, L+b], \forall n \ge \N$.


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

## Indéterminations

Une limite représente une indétermination si elle fait parvenir une combinaison de grandeurs qui ne peut être déterminée. Une telle limite apparait si une suite est composée d'autres suites, ayant elle-memes des limites de type "vers l'infini" ou "vers 0".
| $x_n$ | indétermination
|---|---|
$a_n - b_n$ | "$\infin - \infin$" |
$a_n * b_n$ | "$0 * \infin$" |
$a_n / b_n$ | "$\infin / \infin$" |
$a_n / b_n$ | "$0 / 0$" |
${a_n}^{b_n}$ | "$1^\infin$" |
${a_n}^{b_n}$ | "$\infin^0$" |
${a_n}^{b_n}$ | "$0^0$" |

### type $\infin / \infin$

Essayer d'écrire en tant que produit, simplifier, etc.

### type $\infin - \infin$

Essayer de mettre en evidence un produit. Identités elémentaire, remarquables tres utiles.

### type $0 / 0$

### type $\infin / \infin$

## Série géométrique

$s_n := 1 + r + r^2 + ... + r^n = \displaystyle \sum_{n=0}^{\infin}  r^n$ (somme infinie)

- Si $r \ge 0$: $\space \space s_n \to \infin$
- Si $|r| < 1$: $\space \space s_n \to \frac{1}{1-r}$
- Si $r \le -1$: $\space \space s_n$ diverge.

Pour étudier des sommes infinie de nature semblable, il est souvent utile de les exprimer en tant que la série géométrique.

$e_{n}:=\Bigl(1+\frac{1}{n}\Bigr)^{n}$

- $(e_{n})$ est strictement croissante
- $(e_{n})$ est bornée: $2\le e_{n}<3$ pour tout $n\ge 1$

Par conséquent, il existe $e\in [2,3]$ tel que $\displaystyle \lim_{n\to\infty}e_{n}=e\,.$

## Critère d'Alembert

Soit $(a_n)$ une suite telle que la limite suivante existe:

$$p := \displaystyle \lim_{n \to \infin}|\frac{a_{n + 1}}{a_n}|$$

- Si $0 \le p < 1$ alors $a_n$ converge et $a_n \to 0$ 
- Si $p > 1$ alors $a_n$ diverge. Si $a_n > 0$ pour tout $n$ suffisament grand, $a_n \to \infin$ 

## Limite supérieure et inférieure

Une suite peut être bornée sans converger. (i.e. $(-1)^n$)

Soit $(a_n)$ une suite bornée. On définit:
- $M_n := \sup\{a_n, a_{n+1}, ...\}$
- $m_n := \inf\{a_n, a_{n+1}, ...\}$

De plus:

- $M_n$ majore $\{a_n, a_{n+1}, ...\}$, d'où $a_n \le M_n$
- $m_n$ minore $\{a_n, a_{n+1}, ...\}$, d'où $a_n \ge M_n$

D'où $m_n \le a_n \le M_n$.

- ($M_n$) est décroissante et minorée.
- ($m_n$) est croissante et majorée.

Elles sont convergentes.

- Limite supérieure: $\space \displaystyle \limsup_{n \to \infin} a_n:= \lim_{n \to \infin} M_n$
- Limite inférieure: $\space \displaystyle \liminf_{n \to \infin} a_n:= \lim_{n \to \infin} m_n$

<br>

Theorème:

$\displaystyle \lim_{n\to\infty}a_{n}=L \quad \Leftrightarrow \quad \liminf_{n\to\infty}a_{n}=\limsup_{n\to\infty}a_{n}=L\,.$

## Sous-suites



## Théorème de Bolzano-Weierstrass

De toute suite bornée $(x_n)_n$ on peut extraire une sous-suite convergente.

Si $x_n \in [a, b] \space \forall n \implies \exist L \in [a, b]$ et une sous-suite $(x_{n_k})_k$ telle que $x_{n_k} \to L$

## Suites de Cauchy

Si une suite $(a_n)_n$ converge, la distance entre deux éléments consécutifs tend vers 0.

$∣a_{n+1} ​− a_n​∣ \to 0$ lorsque $n \to \infin$.

Mais c'est aussi vrai pour tout éléments quelconques:

$∣a_m ​− a_n​∣ \to 0$ lorsque $n \to \infin$.

$(a_n)$ Est une **suite de Cauchy** si $\forall b > 0$ il existe $N$, tel que $|a_n - a_m| \le b \space \space \forall m, n \ge N$

Dans $\R$, une suite $(a_n)$ est convergente $\iff$ c'est une suite de Cauchy.

# Suites définies par récurrence

Une suite par récurrence est définie ainsi:

- Premier terme (condition initiale) $x_0 := qqch$
- $x_{n+1} := g(x_n) \space \forall n \ge 0$, $\space g$ étant une fonction $\R \to \R$.

Ces suites sont très compliqées.

## Méthodes de conclusion de comportement

Il est souvent utile de regarder $x_n - x_{n-1}$

### Observer, démontrer.

On peut conjecturer des comportements (monotonité, croissance) à base de quelques valeurs connues, et essayer de démontrer ce comportement.

Une fois qu'on sait que la limite converge vers $L$, $\displaystyle \lim_{n \to \infin} x_{n+1} = \lim_{n \to \infin} x_{n} = L$, d'où: $L = g(L)$

### Expression explicite

On essaye de conjecturer une expression en fonction de n utilisant quelques valeurs connues, et on essaye de démontrer ceci par récurrence.

### Chercher une suite de Cauchy

On cherche à démontrer que $(x_n)$ est une suite de Cauchy.

## Point fixe

Dans le cas de $x_{n+1} := g(x_n)$

Un nombre $\R$éel est **point fixe** de g si $g(x_*) = x_*$

Si $x_0 = x_*$, alors la suite est constante.

### Théorème

Si une suite définie par ($x_{n+1} = g(x_n)$) est convergente, et si $g: \R \to \R$ est continue, alors la limite de $x_n$ (vers l'infini) est un point fixe de $g$. Autrement dit ce nombre doit vérifier $g(L) = L$.

Autrement dit, si g est continue mais ne possède pas de point fixe, la série n'a pas de limite.

Si g possère plusieurs point fixes, [???] (étude détaillée)

