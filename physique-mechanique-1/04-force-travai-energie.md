# Forces

## Forces de Frottement

- S'oppose au mouvement

$F_{frot} = -f(v) \hat v$ pour $f(v) > 0$


Lois de Coulomb:

- $v = 0$: $\vec F_{frot} \leq F^{max}_{frot} = \mu_s N$
- $v \not = 0$: $\vec F_{frot} = -\mu_c N \hat v$

### Force de Frottement Sec

- ne depend pas de la norme de la vitesse
- dépend de la nature du corps (+etat surface, temperature)

### Force de Frottement dans Fluide

Poussée d'Archimède: $\vec F_{arc} = -M \vec g = -V \rho \vec g$

Dans un fluide:

- laminaire: $F_frot = -b \vec v$
- turbulent (haute vitesse): $F_frot = -b v^2 \hat v$

# Impulsion et Quantité de Mouvement

On définit la **Quantité de Mouvement**: $\vec p = m \vec v$ [$kg \cdot m/s$]

On définit **l'Impulsion de la Force $\vec F$**: $I_{12} = \int_1^2 \vec F \space dt = \vec p_2 - \vec p_1$


## Energie Cinétique

$E_k = \frac{1}{2}mv^2$ [$J$]

## Travail

$dW = \vec F \cdot d \vec r \implies W_{12} = \int_1^2 dW = \int_1^2 \vec F d \vec r$

$W = K_2 - K_1$ 

Remarques:

$\vec F \cdot \vec r$: projection de $\vec F$ sur $\vec r$.

### Cas force de pesanteur

$W = \int_1^2 m \vec g \cdot d \vec r = mgz_1 - mgz_2$

## Puissance d'une force

$P = \frac{dW}{dt}= \vec F \cdot \vec v$

$K_2 - K_1 = W_{12} \iff \frac{dK}{dt}$ Taux de variation Ekin = puissance de la resultate des forces

## Force Conservative, Energie Potentielle

- Son travail ne dépend pas du chemin suivi. (uniquement $\Delta$pos)
- $\vec F(x) = -\vec \nabla V(\vec r)\quad$ ($V(\vec r)$ = energie potentielle)
  - $\nabla = (d/dr)$ pour chaque composante x, y, z
    - En gros on dérive V(r) sur chaque composante
- $E = E_k + V(\vec r)\quad$ (energie mécanique est conservée (que pour les forces conservatives))