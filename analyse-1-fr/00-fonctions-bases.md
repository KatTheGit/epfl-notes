# Fonctions (Réelles)

```
f A -> B
```
Une fonction de A dans B est une régle qui associe à chaque élément appartenant à A, un (et un seul) élément appartenant à B.

$y$ est l'image de $x$ par $f$. l'ensemble image de $f$ est $Im(f)$, et est défini ainsi:
$Im(f) = \{y\in B : \exist x \in a : f(x) = y\}$ C'est lensemble des $y \in B$ qui possèdent au moins une préimage.

Pour trouver $Im(f)$, on cherche la "réciproque". En faisant ainsi, on trouve son ensemble et on démontre que chaque image a une préimage dans $Im(f)$.

Pour retrouver l'ensemble Im(f) on met la "réciproque" trouvée dans l'ensemble (A). i.e. $[1, 5] -> 1 \leq 2y + 3 \leq 5$, on manipule, et ou retrouve le nouvel ensemble (B)

## Surjectivité

Une fonction $f: A \to B$ est **surjective** si $Im(f) = B$.
Autrement dit, $\forall y \in B, \exist x \in A : f(x) = y$.
Autrement autrement dit, si chaque élément dans $B$ a au moins une préimage.

Pour démonter qu'une fonction est surjective, on veut démontrer que $Im(f) = B$. On cherche $Im(f)$ en cherchant la "réciproque".

Graphiquement, cela signifie que toute droite horizontale d'equation $y=b, b\in B$, coupe le graphe de $f$ en au moins un point.

## Injectivité

Une fonction $f:A \to B$ est **injective** si $x \not = x' => f(x) \not = f(x')$

Autrement dit si chaque élément dans $B$ a au plus une préimage.

Pour démontrer qu'une fonction est injective, on pose $f(x) = f(x')$, et on cherche à obtenir $x = x'$

Graphiquement, cela signifie que toute droite horizontale d'equation $y=b, b\in B$, coupe le graphe de $f$ en au plus un point.

## Bijectivité

Une fonction est **bijective** si elle est à la fois injective et surjective.

Une fonction bijective peut avoir une fonction réciproque, notée $f^{-1}$.

$f^{-1}: B \to A$ <br>
$y \mapsto f(y)^{-1}$

Graphiquement, la réciproque est une réflexion par rapport à la diagonale du premier quadrant ($y = x$).

# Trigonométrie

## Angles

Les angles peuvent être mesurés en radians, une unité qui exprime la longeur d'un arc de cercle.

La circomférence d'un cercle est de $2\pi$, ce qui corréspond à $360 \degree$ en radians.

Formules de conversion:

$a [deg] = \frac{180}{\pi} a [rad]$

## Fonctions trigo.

Posons un triangle rectangle, dont les cotés prennent le nom de leur relation apr rapport à l'angle $\theta$:
- a: adjacente
- h: hypoténuse
- o: opposée

$cos(\theta) = \frac{a}{h}$ "CAH" <br>
$sin(\theta) = \frac{o}{h}$ "SOH" <br>
$tan(\theta) = \frac{o}{a}$ "TOA" <br>

De plus, $tan = sin/cos$

Les fonctions trigonométriques représentent en réalité, un triangle d'hypoténuse 1, avec l'angle $\theta$ placé à l'rogine. Le cosinus représente la position du point P, de l'autre coté de l'hipoténuse, horizonzale. le sinus représente la position verticale, et la tangente, l'intersection entre (Ox, P) et la ligne tangente au cercle trigonométrique à x = 1.

### Propriétés

$sin(\theta) = sin(\theta + 2k\pi), k \in \N$ (périodique 2pi) <br>
$cos(\theta) = cos(\theta + 2k\pi), k \in \N$ <br>
$tan(\theta) = tan(\theta + k\pi), k \in \N$ (périodique pi) <br>

$-sin(\theta) = sin(\theta + (2k+1)\pi), k \in \N$ (périodique 2pi) <br>
$-cos(\theta) = cos(\theta + (2k+1)\pi), k \in \N$ <br>

## Identités trigonométriques

Identité fondamentale: (obtenue par Théorème de Pythagore)

$sin^2 + cos^2 = 1$

Pour tous $a, b \in \R$

$sin(a+b)=sin(a)cos(b)+sin(b)cos(a)$ <br>
$cos(a+b)=cos(a)cos(b)-sin(b)sin(a)$ <br>
$tan(a+b) = \frac{tan(a) + tab(b)}{1 - tab(a)tab(b)}$ <br>

Pour tout $a \in \R$

$sin(2a) = 2sin(a)cos(a)$ <br>
$cos(2a) = cos^2(a) - sin^2(a) = 2cos^2(a) -1 = 1- 2sin^2(a)$ <br>
$tan(2a) = \frac{2tan(a)}{1-tan^2(a)}$ <br>

# Exponentielles et logarithmes

## Exponentielle

$a^n, n \in \N*$, aussi noté $exp_a(n)$

$a^{b+c} = a^b a^c$

$a^0 = 1$

$a^{-n} = \frac{1}{a^n}$


On apelle $a$ la **base** et $n$ l'**exponent**.

La fonction exponentielle étant bijective, on apelle sa réciproque **logarithme**.

## Logarithme

Le **logarithme de base $a$** se note $log_a(x)$

$log_a(exp_a(x)) = x$ <br>
$exp_a(log_a(x)) = x, \forall x \in R_+^*$

$log_a(xy) = log_a(x) + log_a(y)$

$log_a(1) = 0$

si $a > 1$, $log_a$ est croissante <br>
si $0 < a < 1$, elle est décroissante <br>

$log_a(x) = \frac{log_b(x)}{log_b(a)}$

## la base $e$

e = 2.718

$exp_e(x) = exp(x) = e^x$ <br>
$log_e(x) = log(x) = ln(x)$ <br>

# Dérivation et integration

### Derivation

| $F$ | $F'$ |
|--|--|
| $k$ | $0$ |
| $x$ | $1$ |
| $x^n$ | $nx^{n+1}$ |
| $\frac{1}{x^n}$ | $\frac{-n}{x^n+1}$ |
| $\sqrt x$ | $\frac{1}{2\sqrt x}$ |
| $ln(x)$ | $\frac{1}{x}$ |
| $e^x$ | $e^x$ |
| $cos(x)$ | $-sin(x)$ |
| $sin(x)$ | $cos(x)$ |
| $tan(x)$ | $\frac{x'}{cos^2(x)}$ |
| $tan(x)$ | $x'*(1+tan^2(x))$ |
| $k^x$ | $k^xln(x)$ |
| $u * v$ | $u' * v + u * v'$ |
| $\frac{u}{v}$ | $\frac{u' * v - u * v'}{v^2}$ |
| $v(u(x))$ | $v'(u(x)) *u'(x)$ |

### Integration

Always add the integration constant.

with known x and y, we can find this constant.

| $F$ | $\int F dx$ |
|--|--|
| $x^n$ | $\frac{x^{n+1}}{n+1} + c$
| $k \in \R$ | $kx + c$
| $\frac{1}{\sqrt x}$ | $2 \sqrt x + c$
| $\frac{1}{x^n}, n\in \N \backslash \{0, 1\}$ | $\frac{-1}{(n-1)x^{n-1}} + c$
| $cos(x)$ | $sin(x) + c$
| $sin(x)$ | $-cos(x)+c$
| $e^x$ | $e^x + c$
| $e^{ax}$ | $\frac{1}{a} e^x$