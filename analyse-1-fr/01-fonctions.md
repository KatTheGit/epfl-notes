## Fonction

```
f A -> B
```
Une fonction de A dans B est une régle qui associe à chaque élément appartenant à A, un (et un seul) élément appartenant à B.

$y$ est l'image de $x$ par $f$. l'ensemble image de $f$ est $Im(f)$, et est défini ainsi:
$Im(f) = \{y\in B : \exist x \in a : f(x) = y\}$ C'est lensemble des $y \in B$ qui possèdent au moins une préimage.

Pour trouver $Im(f)$, on cherche la "réciproque". En faisant ainsi, on trouve son ensemble et on démontre que chaque image a une préimage dans $Im(f)$.

## Surjectivité

Une fonction $f: A \to B$ est **surjective** si $Im(f) = B$.
Autrement dit, $\forall y \in B, \exist x \in A : f(x) = y$.
Autrement autrement dit, si chaque élément dans $B$ a au moins une préimage.

Pour démonter qu'une fonction est surjective, on veut démontrer que $Im(f) = B$. On cherche $Im(f)$ en cherchant la "réciproque".

## Injectivité

Une fonction $f:A \to B$ est **injective** si $x \not = x' => f(x) \not = f(x')$

Autrement dit si chaque élément dans $B$ a au plus une préimage.

Pour démontrer qu'une fonction est injective, on pose $f(x) = f(x')$, et on cherche à obtenir $x = x'$

## Bijectivité

Une fonction est **bijective** si elle est à la fois injective et surjective.

Une fonction bijective peut avoir une fonction réciproque, notée $f^{-1}$.

