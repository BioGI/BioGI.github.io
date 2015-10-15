---
title: How to implement the dissolution model in GI code - Dissolution from small particles in numerical simulation
author: Farhad Behafarid and Ganesh Vijayakumar
date: 15 Oct 2015
bibliography: ../References/references.bib
---


Dissolution from small particles in numerical simulation

# Magnitude ranges for particle and lattice cell sizes

~~~math
\forall_{\Delta}= \Delta^3=cell \hskip {0.1in} volume \\
\Delta \sim (100-1000) \mu m \\
R_j \sim (10-50) \mu m \\
\dfrac{R_j}{\Delta} \sim (0.01-0.5) < 1 \\
~~~

--------------------------------------------------------------------------------------------------

# Basic LBM equations

~~~math
\phi_i = concentration\\
~~~

~~~math
#Equtaion1
\dfrac{dN_{b_j}}{dt}=q''_{s_j} A_{s_j} \\
~~~

Where:

~~~math
#Equation2
Sh_j = {\dfrac{R}{\delta}}_j = \dfrac{q''_s}{D_m \big( \dfrac{C_s-C_b}{R}\big)}=1+\Delta_{con} + \Delta_{hyd} 
~~~

And,

~~~math
#Equation3
r_j = | \vec{x}- \vec{x}_j | \\
~~~

~~~math
#Equation4
C(r_j)= ( C_s - C_{{\infty}_j} ) \dfrac{R_j}{r_j} + C_{{\infty}_j} \\
~~~

~~~math
#Equation5
C_{{\infty}_j} = \dfrac{{C_b}_j-\gamma {C_s}_j}{1-\gamma_j} \\
~~~

~~~math
#Equation6
\gamma_j=f(\forall/\forall_C)_j \\
~~~

Therefore for $\gamma=0$, we get $C_{{\infty}_j}=C_b$.

The basic LBM is as follows:

~~~ math
#Equation7
\dfrac{\partial \phi(\vec{x},t)}{\partial{t}} +\nabla . (\vec{u} \phi) = \nabla . \vec{q}''_m
~~~ 

Where $\vec{q}''_m = - D_m \nabla \phi=$ local mole flux.

--------------------------------------------------------------------------------------------------

#Continuum Point Particle Model

Models release of molecules $dN_b/dt$ from points at location of particles: 

~~~ math
#Equation8
\dfrac{\partial \phi(\vec{x},t)}{\partial{t}} +\nabla . (\vec{u} \phi) = S(\vec{x},t) + \nabla . \vec{q}''_m
~~~

Where, 

~~~math
#Equation9
S(\vec{x},t)=\dfrac{d \phi_s(\vec{x},t)}{dt},
~~~

is the rate of change in local concentration field due to release of the molecules from particle j, or in other words, "source" to $\phi(\vec{x},t)$ in local volume $\delta \forall_j$

--------------------------------------------------------------------------------------------------

#Simulations Evolve Filtered Concentration Field $\tilde{\phi} (\vec{x},t)$

At the grid scale $\forall_{\Delta}$:

~~~math
#Equation10
\tilde{\phi} (\vec{x},t)=\dfrac{1}{\forall_{\Delta}} \int \phi (\vec{x},t) f(\vec{x}_i - \vec{x} ) dx
~~~

Where $f(\vec{x})$ has support $\forall_{\Delta} = \Delta^3$ and $\int f(\vec{x}) d \vec{x} = \forall_{\Delta}$

Combining these equations


















-------------------------------------------------------------------------------------------------

#Evaluating the SGS terms

At a grid point `i`, this is the filtered advection/diffusion equation for the scalar concentration that we're trying to solve.

~~~math 
#eqFilteredScalar
\underbrace{ \frac{\partial \tilde{\phi}_i}{\partial t} + \nabla \cdot ( \tilde{\vec{u}}_i \tilde{\phi}_i ) = \nabla \cdot \tilde{\vec{q}}_{m_i} }_{LBM, Moment propagation method} + \tilde{S_i} + \nabla \cdot \vec{\tau}_i
~~~

where $\vec{\tau}_i = \tilde{\vec{u}}_i \tilde{\phi}_i - \widetilde{\vec{u}_i \phi_i}$ and $\tilde{\vec{q}}_{m_i} = -D_m \nabla \tilde{\phi}_i$. The SFS term in Equation (#eqFilteredScalar) is $\nabla \cdot \vec{\tau}_i$. Balaji developed an analysis of this term on 11/15/2014 as

~~~math
#eqBalajiSFSterm
\nabla \cdot \vec{\tau}_i = \tilde{F}_sfs = \frac{1}{V_i} \sum_{CGF} \left ( \underbrace{\sum_{\textrm{SGF in CGF}} \vec{q}_{bf} A_{bf}}_{\widetilde{\vec{u}_i \phi_i}}  - \underbrace{\vec{q}^{CGC} A_F}_{\tilde{\vec{u}}_i \tilde{\phi}_i}  \right ) \cdot \hat{n}_b
~~~

While I don't understand this completely, here's what I do. Balaji's formulation is based on converting the volume integral to a surface integral and using the fluxes to compute it. According to Dr. Brasseur, Balaji's formulation includes both the diffusive and the advective flux. The diffusive flux from the molecule surface is already modeled through $\tilde{S}_i$. Instead Dr. Brasseur claims to evaluate $\widetilde{\vec{u}_i \phi_i}$ by integrating it around the particles. According to Dr. Brasseur,

~~~math
\widetilde{\vec{u}_i \phi_i} &= \widetilde{\sum_{\textrm{particles j in } V_i } \vec{u}_i C_j(r)} \\
~~~

where $C_j(r)$ is the concentration profile around the particle derived from the QSM model as

~~~math
#eqQSMconcProfile
 C_j(r) = \left ( \frac{C_{b_j} - \gamma_j C_s}{ 1 - \gamma_j} \right ) \left [ 1 + \left ( \frac{C_s - C_{b_j}}{ C_{b_j} - \gamma_j C_s} \right ) \frac{R_j}{r}  \right ]
~~~

$r$ is defined from the center of the particle $j$ of radius $R_j$. This is further simplified as (**I don't seem to quite understand this.**)

~~~math
#eqComputeTauModel
\widetilde{ \sum_{\textrm{particles j in } V_i } \vec{u}_i C_j(r) } = \sum_{j \in V_i} \vec{u}_j \tilde{C}_j
~~~

where $\vec{u}_j$ is the local velocity predicted by the LBM interpolated to the particle location and \tilde{C}_j is the local concentration surrounding particle $j$. 

~~~math
 \tilde{C}_j = \frac{1}{V_i} \int_{V_i} C_j(r) dV
~~~

Further the term inside the integral is
~~~math
\int_{V_i} C_j(r) dV = N_{b_j} = \textrm{ Number of moles surrouding particle j}
~~~

Dr. Brasseur aims to approximate this integral using an effective volume $V_{eff}$ around the particles as 

~~~math
N_{b_j} \int_{V_{eff}} C_j(r) dV =  \int_{R_j}^{R_{eff_j}} C_j(r) 4 \pi r^2 dr 
~~~

The estimate for $V_{eff}$ and hence $R_{eff}$ is based on the central model estimate for ** $C_{b_j}$ as the coarse-grained LBM prediction for concentration at the position of the point particle**. i.e.

~~~math
C_{b_j} = \tilde{\phi}(\vec{x}_j,t) = \frac{N_{b_j}}{V_{eff_j}}
~~~

In other words, adjust the volume of integration around the particle such that the average concentration inside that is the same as that predicted by the LBM. While the full expression for $C_j(r)$ is given in Equation (#eqQSMconcProfile), it is restated as 

~~~math
C_j(r) &= A \left [ 1 + B \left( \frac{R_j}{r} \right) \right ] \\
\textrm{where } A &= \frac{C_{b_j} - \gamma_j C_s}{ 1 - \gamma_j} \\
\textrm{and } B &= \frac{C_s - C_{b_j}}{ C_{b_j} - \gamma_j C_s} 
~~~

Thus the integral for $N_{b_j}$ becomes 

~~~math 
C_{b_j} \frac{4}{3} \pi R_{eff_j}^3 =  N_{b_j} = \int_{R_j}^{R_{eff_j}}  A \left [ 1 + B \left( \frac{R_j}{r} \right) \right ]  4 \pi r^2 dr
~~~

It's only important to know that A and B are functions of $C_{b_j}$.

~~~math #eqRefCb
C_{b_j} = A + 3 B \left [ \left ( \frac{R_j}{R_{eff_j}} \right ) - \left ( \frac{R_j}{R_{eff_j}} \right )^3 \right ]
~~~

Thus the algorithm used to determine $V_{eff}$ and $N_{b_j}$ is 

* From LBM at time $t$, determine $C_{b_j} = \tilde{\phi}_j = \tilde{\phi}(\vec{x}_j,t)$ for all particles j
* Compute $A$ and $B$ for each particle
* Use Newton-Raphson to solve Equation (#eqRefCb) for $R_{eff}$
* Determine $N_b$ as $C_{b_j} (4/3) \pi R_{eff_j}^3$
* Compute $\tau_i$ using Equation (#eqComputeTauModel)


# Ganesh thoughts on modeling dissolution from particles in the intestine

The Reynolds number of these flows is in general fairly small. If we model the drug particles as finite particles, there would be a difference between the local flow velocity and the velocity of the particle. If you consider the relative velocity between the drug particle and the flow, then the reynolds number w.r.t the particle diameter is definitely $\sim O(1)$ or smaller. At such Reynolds numbers, we can apply the Stokes flow approximation to the flow around the particle. The Stokes flow around spheres has an analytical solution for both the velocity and the scalar distribution. Dennis, Walker and Hudson reported on the heat transfer from an isothermal sphere at low Reynolds numbers in 1973 [@FLM:372733]. Kim and Karrila [@Kim2005], Happel and Brenner [@Happel1983] and [@Guazzelli2011] seem to report analytical solutions even for a Stokes flow past a sphere under a constant shear rate. May be this can be used to implement a sub-filter scale model for the interaction between the drug particle and the flow. We may be able to develop a correlation for $\widetilde{\vec{u}_i \phi_i}$ analytically using some approximations.


# References
