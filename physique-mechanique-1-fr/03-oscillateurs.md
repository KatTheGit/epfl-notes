# Oscillateurs

## Loi de Hooke (ressorts)

$\vec F_{rappel} = -k \vec{\Delta x}$

- k: constante elastique [N/m]

## Resolution $m \ddot x = -kx$

$F = ma \iff ma = -kx \iff m \ddot x = -kx$

$m \ddot x = -kx \iff \ddot x + {\omega_0}^2 x = 0$, avec $\omega = \sqrt \frac{k}{m}$ (pulsation propre oscillateur libre)
- $v(t) = -x_0 \omega_0 sin(\omega_0 t)$
- $a(t) = -x_0 {\omega_0}^2 cos(\omega_0 t)$

### Solution générale????

$x(t) = Acos(\omega_0t) + B sin(\omega_0 t)$
- $A = x_0$
- $B = \frac{v_0}{\omega_0}$
- $\omega_0 = \sqrt \frac{k}{m}$ (pulsation, $\not = \dot \phi$)

$x(t) = Csin(\omega_0𝑡 + \phi)$
- $C = {x_0}^2 + \frac{v_0}{\omega_0}^2$
- $tan(\phi) = \frac{\omega_0 x_0}{v_0}$

## Avec friction $m \ddot x = -kx -b \dot x$

On a posé une nouvelle force, $F_f = bv$
- $b$ coeff de frottement

### Solution

$\ddot x + 2 \gamma \dot x + {\omega_0}^2 x = 0$

- $\gamma = \frac{b}{2m}$
- $\omega_0 = \sqrt \frac{k}{m}$

IDK

- $\gamma < \omega_0$
- $\gamma = \omega_0$
- $\gamma > \omega_0$