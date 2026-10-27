# Propriétés des fonctions

## Monotonie

Une fonction, sur un intervalle I, est:

- croissante si $f(x_1) \le f(x_2) \quad \forall \space x_1, x_2 \space \space | \space \space x_1 < x_2$
- strictement croissante si $f(x_1) > f(x_2) \quad \forall \space x_1, x_2 \space \space | \space \space x_1 < x_2$
- décroissante si $f(x_1) \ge f(x_2) \quad \forall \space x_1, x_2 \space \space | \space \space x_1 > x_2$
- strictement décroissante si $f(x_1) > f(x_2) \quad \forall \space x_1, x_2 \space \space | \space \space x_1 > x_2$

### Variation

L'étude de la variation c'est trouver les intervalles de croissance et décroissance.

## Parité

### Paire

$f(x) = -f(x)$

Symmétrique par rapport à l'axe Y

### Impaire

$f(-x) = -f(x)$

Symmétrique radialement par rapport à l'origine

### Propriétés

Toute fonctions (dans un domaine symmétrique) peut être écrite comme la somme d'une fonction paire et d'une fonction impaire.

## Périodicité

$f(x + t) = f(x)$. Si $\exists t > 0$, on apelle $t$ la période de $f$, et one note $T = t$

### Propriétés

Si $f$ de période $T_f$ et $g$ de période $T_g$, alors $f \plusmn g$ sont périodiques si $\frac{T_f}{T_g} \in \mathbb{Q}$. (rationnels).

## Maximum, Minimum

### Maximum

$f(x) \le f(M) \quad \forall x \in D_f$

$max \space f(x) = f(M)$

### Minimum

$f(x) \ge f(m) \quad \forall x \in D_f$


$min \space f(x) = f(m)$

### Majorant

$f(x) \le M \quad \forall x \in D_f$

pas nécéssairement $f(M)$.

### Minorant

pareil mais à l'envers.

### Bornée

Si les deux existent.

## Majorant et minorant.

Si $f$ est majorée $D_f$, sont majorant plus petit est **la borne supérieure de $f$**, notée $\displaystyle \sup_{D_f} \space f$

Si $f$ n'est pas majorée, $\displaystyle \sup_{D_f} f := +\infin$

pareil mais $ l'envers pour le minorant, noté $\inf$.

### Proprétés

Dans un intervalle $\sub D_f$

- $\sup -f = - \inf f$
- $\sup (f + g) = \sup f + \sup g$
- $\sup (\alpha f + \beta) = \alpha \sup f + \beta$
- si $A \sub B  \sub D_f$, alors $\displaystyle \sup_A f \le \sup_B f$, et $\displaystyle \inf_A f \ge \inf_B f$


## Convexité

### Convexe

$f((1-\lambda)x_{1}+\lambda x_{2})\le(1-\lambda) f(x_{1})+\lambda f(x_{2})$

Toute droite crée par deux points quelconques est **au dessus** du graphe.

### Concave

$f((1-\lambda)x_{1}+\lambda x_{2})\ge(1-\lambda) f(x_{1})+\lambda f(x_{2})$

Toute droite crée par deux points quelconques est **au dessous** du graphe.
