# How to implement the dissolution model in GI code

Dissolution from small particles in numerical simulation

## Mmagnitude ranges for particle and lattice cell sizes

~~~math
\forall_{\Delta}= \Delta^3=cell \hskip {0.1in} volume \\
\Delta \sim (100-1000) \mu m \\
R_j \sim (10-50) \mu m \\
\dfrac{R_j}{\Delta} \sim (0.01-0.5) < 1 \\
~~~

## Basic LBM equations

~~~math
\phi_i = concentration \\
\dfrac{dN_{b_j}}{dt}=q''_{s_j} A_{s_j} \\
~~~

Where:

~~~math
Sh_j = {\dfrac{R}{\delta}}_j = \dfrac{q''_s}{D_m \big( \dfrac{C_s-C_b}{R}\big)}=1+\Delta_{con} + \Delta_{hyd} 
~~~

And,
~~~math
r_j = | \vec{x}- \vec{x}_j | \\
C(r_j)= ( C_s - C_{{\infty}_j} ) \dfrac{R_j}{r_j} + C_{{\infty}_j} \\
C_{{\infty}_j} = \dfrac{{C_b}_j-\gamma {C_s}_j}{1-\gamma_j} \\
\gamma_j=f(\forall/\forall)_j \\
~~~

Therefore for $\gamma=0$, we get $C_{{\infty}_j}=C_b$.

The basci LBM is as follows:

~~~ math
\dfrac{\partial \phi(\vec{x},t)}{\partial{t}} +\nabla . (\vec{u} \phi) = \nabla . \vec{q}''_m
~~~ 

Where $\vec{q}''_m = - D_m \nabla \phi=$ local mole flux.

##Continuum Point Particle Model

Models release of molecules $dN_b/dt$ from points at location of particles: 

~~~ math
\dfrac{\partial \phi(\vec{x},t)}{\partial{t}} +\nabla . (\vec{u} \phi) = S(\vec{x},t) + \nabla . \vec{q}''_m
~~~

Where, $S(\vec{x},t)=\dfrac{d \phi_s(\vec{x},t)}{dt}$ is the rate of change in local concentration field due to release of the molecules from particle j, or in other words, "source" to $\phi(\vec{x},t)$ in local volume $\delta \forall_j$

