---
title: My understanding of the Lattice Boltzmann Method
author: Ganesh Vijayakumar
date: 09 Oct 2015
bibliography: /work2/guv106/CurrentProjects/Bio/References/references.bib
---

# Basic Boltzmann Gas concepts

The first concept to understand is that the gas is described as number of molecules interacting with one another only through collisions. A number density function [@Gombosi1994] is defined as the number of molecules $\Delta^3 N$ in a volume $\Delta^3 x$ around $\vec{x}$ at a given time $t$.

~~~math
n(\vec{x},t) = \lim_{\Delta^3 x \to 0} \frac{\Delta^3 N(\vec{x},t)}{\Delta^3 x}
~~~

This is probably related to the density through a scaling factor

~~~math
\rho(\vec{x},t) = n(\vec{x},t) \times \frac{MolecularWeight}{AvogradoNumber}
~~~

The Boltzmann theory further splits the number density into a distribution function in a phase space that includes the velocity of the molecules. So $f(\vec{x}, \vec{v}, t)$ is distribution function of the number of molecules $\Delta^3 N$ in a volume $\Delta^3 x$ around $\vec{x}$ and in a certain "velocity-volume" $\Delta^3 v$ around a velocity $\vec{v}$ at a given time $t$

~~~math
f(\vec{x},\vec{v},t) = \lim_{\Delta^3 x, \Delta^3 v \to 0} \frac{\Delta^3 N(\vec{x},\vec{v},t)}{\Delta^3 x \; \Delta^3 v}
~~~

$f(\vec{x}, \vec{v}, t)$ is connected to $n(\vec{x}, t)$ through integration over all possible velocity magnitudes and directions at the same location $\vec{x}$

~~~math
n(\vec{x},t) = \iiint_{\infty} f(\vec{x},\vec{v},t) d^3v
~~~

I borrow the rest of this material from Sukop and Thorne [@Sukop2006]. Let's say there's an external force acting on the molecules \vec{F} $(\vec{F} \ll \textrm{Intermolecular forces})$. If there are no collision, The molecules at $(\vec{x},\vec{v},t)$ will get moved to a new position in the phase space $(\vec{x} + \vec{dx}, \vec{v} + \vec{dv},t \; + \;dt)$ such that $\vec{dv} = (\vec{F}/\rho)dt$ and $\vec{dx} = \vec{v} \; dt$. Through the **streaming process**, the particle distribution function $f$ also gets streamed to the new location such that

~~~math
f(\vec{x} + \vec{dx}, \vec{v} + \vec{dv},t \; + \;dt) \; \vec{dx} \; \vec{dv} = f(\vec{x}, \vec{v},t) \; \vec{dx} \; \vec{dv}
~~~

I have a **big** question here. Can't particles arrive at $(\vec{x} + \vec{dx}, \vec{v} + \vec{dv},t \; + \;dt)$ from somewhere else in the phase space? I'm pretty sure it's not impossible. According to everything I've read so far, they just write this for the case of no collisions. I say that even with no collisions and well.. even no forces, it's possible for molecules from two different positions to come to one place. May be they'll collide there, but no collision until then. Got to figure out the reasoning behind this.

Moving on, there are collisions that result in some phase points starting at $(\vec{x},\vec{v},t)$ and not arriving at $(\vec{x} + \vec{dx}, \vec{v} + \vec{dv},t \; + \;dt)$ and some not starting at $(\vec{x},\vec{v},t)$ and arriving there (this probably answers the question above).

~~~math
\textrm{Number of molecules that do not arrive at } (\vec{x} + \vec{dx}, \vec{v} + \vec{dv},t \; + \;dt) \textrm{ due to collision } & \longrightarrow \Gamma^- \vec{dx} \; \vec{dv} \; dt \\

\textrm{Number of molecules that do arrive at } (\vec{x} + \vec{dx}, \vec{v} + \vec{dv},t \; + \;dt) \textrm{ from somewhere else } & \longrightarrow \Gamma^+ \vec{dx} \; \vec{dv} \; dt \\
~~~

Combining the streaming process and the model for collisions, we get the Boltzmann equation

~~~math
f(\vec{x} + \vec{dx}, \vec{v} + \vec{dv},t \; + \;dt) \; \vec{dx} \; \vec{dv} &= f(\vec{x}, \vec{v},t) \; \vec{dx} \; \vec{dv} + (\Gamma^+ - \Gamma^-) \vec{dx} \; \vec{dv} \; dt \\
\left ( f(\vec{x}, \vec{v},t) + \vec{dx} \cdot \nabla_x f + \vec{dv} \cdot \nabla_v f + \frac{\partial f}{\partial t} dt \right ) \; \vec{dx} \; \vec{dv} &= f(\vec{x}, \vec{v},t) \; \vec{dx} \; \vec{dv} + (\Gamma^+ - \Gamma^-) \vec{dx} \; \vec{dv} \; dt \\
\frac{\partial f}{\partial t} + \vec{v} \cdot \nabla_x f + \frac{\vec{F}}{\rho} \cdot \nabla_v f &= (\Gamma^+ - \Gamma^-)
~~~

The term $(\Gamma^+ - \Gamma^-)$ is usually modeled as a return to equilibrium using the Bhatnagar-Grossman-Krook (BGK) collision operator with a single relaxation time scale $\tau$.

# Application to the Lattice Boltzmann Method

The first thing that nobody seems to mention regarding the Lattice Boltzmann Method is that they go ahead and assume that $f$ already contains the scaling factor such that

~~~math
\rho(\vec{x},t) = \iiint_{\infty} f(\vec{x},\vec{v},t) d^3v
~~~

Instead of a continuum of possible positions and velocity for the molecules, the positions are limited to a set of points on a lattice and the velocities are restricted to a set of magnitudes and directions. The set of possible velocities are connected to the lattice and the time step. The D2Q9 and D3Q15 are very commonly used in 2D and 3D simulations respectively. The basic lattice distance $\delta x$ is set to 1 as is the time step $\delta t$. Thus, the _grid speed_ is $c = \delta x / \delta t = 1$. Of course, there conversion factors for each quantity like $\delta x, \delta t, c$ to their corresponding physical values. Figure [#latticeDiscretization2D3D] shows the two basic lattice models used are the D2Q9 version for 2D and D3Q15 for 3D. 

#### Figure: {#latticeDiscretization2D3D}

![](d2q9d3q15.png)

Caption: Illustrations of the lattice and directional densities on a D2Q9 (left) and D3Q15 (right) arrangement (from [@Nourgaliev2003117]).

I now explain how the choice of the discrete velocity vectors are tied to the grid and the time step. In Figure [#latticeDiscretization2D3D], the red vectors are of unit distance in lattice units in both D2Q9 and D3Q15 models. The corresponding velocity vectors are lattice unit per time step. The choice of the velocity vectors is done such that that any molecule with that velocity at that point will get _streamed_ to the first neighboring node along the velocity direction in one time step. Thus the green distance and velocity vectors are $\sqrt{2}$ lattice units in the D2Q9 model and $\sqrt{3}$ units in the D3Q15 model. Thus the continuous particle distribution $f(\vec{x}, \vec{v}, t)$ becomes the discrete _directional densities_ $f_{\alpha}(\vec{x},t), \, \alpha=1,b$ at each lattice point/node, where $b$ is the number of directions used in the lattice model (9 for the D2Q9 and 15 for the D3Q15 models). The macroscopic properties density ($\rho$) and velocity ($\vec{v}$) are recovered from the directional densities as

~~~math
\rho(\vec{x},t) &= \Sigma_{\alpha = 1}^b f_{\alpha} (\vec{x},t) \\
\rho(\vec{x},t) \; \vec{v}(\vec{x},t) &= \Sigma_{\alpha = 1}^b f_{\alpha} (\vec{x},t) \hat{e}_{\alpha}
~~~
The pressure is recovered through the equation of state, where

~~~math
P(\vec{x},t) = \rho(\vec{x},t) c_s^2 
~~~

where $c_s$ is the speed of sound in lattice units $c_s = \sqrt{RT} = \sqrt{1/3}$ in lattice units. I wonder why the ratio of specific heats $\gamma$ is missing from the expression for the speed of sound. In any case, this tells us that the LBM method is essentially a compressible method. 

The basic LBM method for the momentum and continuity equations thus becomes

~~~math
f_{\alpha}(\vec{x} + \hat{e}_{\alpha} \; \delta t,t + \delta t) = f_{\alpha} (\vec{x},t) - \frac{1}{\tau} \left [ f_{\alpha} (\vec{x},t) - f_{\alpha}^{eq} (\vec{x},t) \right ]
~~~

The time advance in the LBM method is carried out algorithmically in two steps, viz.,

1. Collision step

~~~math
\hat{f}_{\alpha}(\vec{x}, t) = f_{\alpha} (\vec{x},t) - \frac{1}{\tau} \left [ f_{\alpha} (\vec{x},t) - f_{\alpha}^{eq} (\vec{x},t) \right ]
~~~

2. Streaming step
~~~math
f_{\alpha}(\vec{x} + \hat{e}_{\alpha} \; \delta t,t + \delta t) = \hat{f}_{\alpha} (\vec{x},t) 
~~~

where $\hat{f}_{\alpha} (\vec{x},t)$ is the _post-collision pre-streamed_ directional densities. The boundary conditions are typically applied on $\hat{f}$.


## BGK collision operator

The rate of relaxation towards equilibrium is typically a measure of the rate of molecular mixing and is hence proportional to the kinematic viscosity. In lattice units

~~~math
\nu = (2 \tau - 1) \frac{c \; \delta x}{6}
~~~
The viscosity in physical units is matched to the viscosity in lattice units by matching the Reynolds numbers between the physical and lattice units. For numerical stability purposes, the choice of $\tau$ is designed to be such that the viscosity is positive and hence $\tau > 0.5$. The farther away it is from $0.5$, the more stable the simulation is expected to be.

In the low Mach number limit, the equilibrium distribution function $f^{eq}$ is written as

~~~math
f^{eq}_{\alpha} (\vec{x},t) = w_{\alpha} \rho(\vec{x},t) \left [ 1 + 3 \frac{\hat{e}_{\alpha} \cdot \vec{v}}{c^2} + \frac{9}{2} \frac{(\hat{e}_{\alpha} \cdot \vec{v})^2 }{c^4} - \frac{3}{2} \frac{(\vec{v} \cdot \vec{v})^2}{c^2}  \right ]
~~~

For the D2Q9 model,

~~~math
w_{\alpha} =  \left \{ \begin{aligned} 4/9 & \, \alpha = 0 \\ 1/9 & \, \alpha = 1,3,5,7 \\ 1/36 & \, \alpha = 2,4,6,8 \end{aligned} \right.
~~~

The rest of the stuff to be written up are

# Conversion of lattice units to physical units

The code converts the physical units to lattice units as follows in [Geometry.f90]()

```fortran
! Define the lattice <=> physical conversion factors
IF(domaintype .EQ. 0) THEN
xcf = (0.5_lng*D)/(nx-1_lng)   ! length conversion factor: x-direction
ycf = (0.5_lng*D)/(ny-1_lng)   ! length conversion factor: y-direction
ELSE
! begin Balaji added
xcf = (1.0_lng*D)/(nx-1_lng)   ! length conversion factor: x-direction
ycf = (1.0_lng*D)/(ny-1_lng)   ! length conversion factor: y-direction
! end Balaji added
ENDIF

zcf = L/nz                     ! length conversion factor: z-direction
tcf = nuL*((xcf*xcf)/nu)       ! time conversion factor
dcf = den/denL                 ! density conversion factor
vcf = xcf/tcf                  ! velocity conversion factor
pcf = cs*cs*vcf*vcf            ! pressure conversion factor

! Determine the number of time steps to run
nt = ANINT((nPers*Tmix)/tcf)
```

In human readable form, this becomes

~~~math
x_{cf} &= \frac{D}{n_x-1} \\
y_{cf} &= \frac{D}{n_y-1} \\
z_{cf} &= \frac{L}{nz} \\
t_{cf} &= \nu_L \frac{x_{cf} \; x_{cf}}{\nu} \\
\rho_{cf} &= \frac{\rho}{\rho_L} \\
v_{cf} &= \frac{x_{cf}}{t_{cf}}
~~~

The quantities with $f_L$ are in lattice units. For e.g $\rho_L = 1.0$ is the density in lattice units and $\nu_L$ is the viscosity in lattice units defined in `LBM.f90` as $\nu_L = (2 \tau - 1)/6$.

~~~fortran
nuL = (2.0_dbl*tau - 1.0_dbl)/6.0_dbl
~~~

# Boundary conditions

# Treatment of passive scalar

# Multi-grid scheme


# References


