## Coordonnées Cylindriques

$p$ <br>
$\phi$ <br>
$z$ <br>

$x = p \space cos \phi$ <br>
$y = p \space sin \phi$ <br>
$z = z$ <br>

$\vec r = p * \hat e_p + z * \hat e_z$ <br>
$\vec v = \dot p * \hat e_p + p \dot \phi * \hat e_\phi + \dot z * \hat e_z$ <br>
$(\ddot p - p \dot \phi ^2) * \hat e_p + (p \ddot \phi + 2 \dot p \dot \phi) * \hat e_\phi + (\ddot z) * \hat e_z$ <br>

## Coordonnées Spériques

$r$ <br>
$\theta$ <br>
$\phi$ <br>

$x = r * sin (\theta) cos (\phi)$ <br>
$y = r * sin(\theta) sin (\phi)$ <br>
$z = r * cos(\theta)$ <br>


$\vec r = r * \hat e_r$ <br>
$\vec v = \dot r \hat e_r + r \dot \theta * \hat e_\theta + r \dot \phi sin \theta * \hat e_\phi$ <br>
$\vec a = (\ddot r - r \dot \theta^2- r \dot \phi^2sin^2 \theta) * \hat e_r$ <br>
$\space \space \space \space+ (r \ddot \theta + 2 \dot r \dot \theta - r \dot \phi^2 sin \theta \space cos \theta) * \hat e_\theta$ <br>
$\space \space \space \space+ (r \ddot \phi sin \theta + 2 \dot r \dot \phi sin \theta + 2r \dot \phi \dot \theta cos \theta) * \hat e_\phi$