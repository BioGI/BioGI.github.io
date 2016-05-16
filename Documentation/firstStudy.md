---
title: First computational study
author: Ganesh Vijayakumar, Farhad Behafarid, Yanxing Wang and James Brasseur
date: 13 May 2016
bibliography: ../References/references.bib
---

The first study is to test the influence of hydrodynamic and shear effects on the dissolution and absorption of drug releasing from a distribution of particles in the fed state of a human intestine. The four experiments that will be run are

1. Intestine without shear or hydrodynamic effects.
2. Intestine with shear but no hydrodynamic effects.
3. Intestine with hydrodynamic but no shear effects.
4. Intestine with hydrodynamic and shear effects.

The input parameters that need to be specified for the different experiments fall into different categories, viz., geometry and motility, drug and fluid properties, particle information, boundary conditions and the correlations for shear and hydrodynamic effects. 

# Geometry and Motility

   Diameter, Length and occlusion ratio, motility mode (peristalsis/segmentation) and wave speed.

Review Gino's thesis for in vivo human data - we need ranges of physiologically realistic parameters in the middle of which will be "typical". We need peristaltic and segmental motility geometry models:

* Need to estimate "bolus" volume as well as $R_{max}$, $\lambda$ (wavelength)  and $\epsilon/R_{max}$ (occlusion ratio - use 0.4).
* Need to estimate wave speed (peristalsis) and collapse speed (segmental)

Table (#table:study1GeomMotilityParams) describes the geometry and motility parameters of the first computational study.

#### Table:  {#table:study1GeomMotilityParams}

| Name             |       Symbol        | Value       |  Units    |  
|------------------|---------------------|-------------|-----------|
| Max diameter     | $D_{max}$           | 30          | $mm$      |
| Wavelength       | $\lambda$           | 40-60       | $mm$      |
| Number of waves  | -                   | 1           | -         |
| Occlusion ratio  | $\epsilon/R_{avg}$  | 0.5         | -         |
| Motility mode    | -                   | peristalsis | -         |
| Wave speed       | $s_1$               | 4           | $mm/s$    |


Caption: Geometry and motility properties for the first computational study.



# Drug and Fluid properties

Choose water with neutral $pH=7$ at $20^{\circ}C$ (to determine viscosity).

Choose ibuprofen with $C_S$ fixed according to the neutral pH.


Table (#table:study1DrugFluidParams) shows the drug and fluid properties for the first computational study.

#### Table:  {#table:study1DrugFluidParams}

| Name                 |          Symbol     | Value                  |  Units     |  
|----------------------|---------------------|------------------------|------------|
| Density              | $\rho_{water}$      |   998.2                | $kg/m^3$   |
| Kinematic Viscosity  | $\nu_{water}$       | $1.004\times 10^{-2}$  | $cm^2/s$   |
| Schmidt number       | $Sc$                | 10                     | -          |
| Molar volume         | $\nu_m$             | 268                    | $cm^3/mol$ |
| Diffusivity of drug  | $D_m$               |  $7.5 \times 10^{-6}$  | $m^2/s$    |
| Saturation conc.     | $C_S$               |  $3.3 \times 10^{-7}$  | $mol/cm^3$ |

Caption: Drug and fluid properties for the first computational study.


# Particles

Total dose and particle size distribution: Choice of shape (log normal), average size and width, number of bins, bin size.

Total dose: Choose $C_{tot}/C_S \sim 0.1$ to be such that we are in sink conditions and far from the singularity near $C_{tot}/C_s = 1$. We choose this even though that singularity is only for the case without absorption and we do have absorption in the intestine case.

"BOLUS DOSE": mass or moles of drug in a bolus segment. To estimate we will collect data from the literature and from UM on concentration of extracted fluids -- statistics. From MRI (Nottingham) we will estimate bolus volume. These two will give us dose in moles from which bolus CT can be estimated. To this end, we need to estimate solid content along with fluid concentration in the extracted segments. Once we have ranges of CT we can estimate ranges of CT/CS -- our critical parameter.

We need to estimate for time = 0 the ranges of average particle sizes (R* ~ 50 - 100 micron diameter seem reasonable), mathematical distribution function  shape (log normal seems reasonable), width of the distribution, number of particles, and the number of the bins discretizing the distribution. I must put together information from previous attempts to address this issue. There will have to be a strong balance with practicality -- computational load, grid resolution, etc.

Choice of where to locate the particles at the initial condition.

# Boundary conditions

 Immediate uptake. $\phi = 0$ at the wall.

# Correlations for shear and hydrodynamic effects.



