---
title: Fed Experiments
author: Farhad Behafarid
date: 30 June 2016
---

The Fed experiments are desined to investigate  the influence ofmotility mode and shear effects on the dissolution and absorption of drug releasing from a distribution of particles in the fed state of a human intestine. 

The four Fed experiments are summerized in Table (#table:FedExperiments):

#### Table:  {#table:FedExperiments}

| Experiment No.| Motility    |Shear Effects|
|---------------|-------------|-------------|
| 1             | Peristalsis |No           |
| 2             | Segmental   |No           |
| 3             | Pristalsis  |Yes          |
| 4             | Segmental   |Yes          |

Caption: Fed Experiments

The input parameters that need to be specified for the different experiments fall into different categories, viz., geometry and motility, drug and fluid properties, particle information, boundary conditions and the correlations for shear and hydrodynamic effects. 


<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
# Geometry and Motility

Table (#table:study1GeomMotilityParams) describes the geometry and motility parameters of the first computational study.

#### Table:  {#table:study1GeomMotilityParams}

| Name             |       Symbol        | Choice     				|Unit	|  
|------------------|---------------------|--------------------------------------|-------|
| Max diameter     | $D_{max}$           | <span style="color:black">22.4|$mm$  	|
| Wavelength       | $\lambda$           | <span style="color:black">60	|$mm$  	|
| Volume of bolus  | $V_C$		 | <span style="color:red">11.82 |$cm^3$ |
| Wave speed       | $s_1$               | <span style="color:black">2	|$mm/s$ |
| Number of waves  | -                   | 1           				|-      |
| Occlusion ratio  | $\epsilon/R_{max}$  | 0.5         				|-      |

Caption: Geometry and motility properties for the first computational study.






<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
# Drug and Fluid properties

Table (#table:study1DrugFluidParams) shows the drug and fluid properties for the first computational study.

#### Table:  {#table:study1DrugFluidParams}

| Name                 		|    Symbol           	| Choice                				|  Unit      	|  
|-------------------------------|-----------------------|-------------------------------------------------------|---------------|
| Drug                 		| 		     	| Ibuprofen	   					| 	     	|
| Fluid                		|              		| Water                					|            	|
| Fluid's temperature  		| $T_w$		     	| 20                   					| $^{\circ}C$	|
| Fluid's PH			| $PH_w$		| 7							|            	|
| Fluid's density              	| $\rho_w$      	| <span style="color:black">1000			| $kg/m^3$   	|
| Fluid's dynamic viscosity  	| $\mu_w$       	| <span style="color:black">$1$ 			| $cp$   	|
| Fluid's kinematic viscosity  	| $\nu_w$       	| <span style="color:black">$1.0e-6$ 		| $m^2/s$   	|
| Drug's density		| $\rho_m$ 		| <span style="color:red">?			| $kg/m^3$	|	    	
| Drug's molar volume  		| $\nu_m$             	| 268                  					| $cm^3/mol$ 	|
| Drug's diffusivity   		| $D_m$               	| $7.5 \times 10^{-6}$ 					| $cm^2/s$    	|
| Saturation concentration	| $C_S$               	| $3.3 \times 10^{-7}$ 					| $mol/cm^3$ 	|

Caption: Drug and fluid properties for the first computational study.






<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
# Particles

Total dose: Choose $C_{tot}/C_s =0.2$ to be such that we are in sink conditions and far from the singularity near $C_{tot}/C_s = 1$. 
We choose this even though that singularity is only for the case without absorption and we do have absorption in the intestine case.

"BOLUS DOSE": mass or moles of drug in a bolus segment. To estimate we will collect data from the literature and from UM on concentration of extracted fluids -- statistics. From MRI (Nottingham) we will estimate bolus volume. These two will give us dose in moles from which bolus $C_{tot}$ can be estimated. To this end, we need to estimate solid content along with fluid concentration in the extracted segments. Once we have ranges of $C_{tot}$ we can estimate ranges of  $C_{tot}/C_s$ -- our critical parameter.

Choice of where to locate the particles at the initial condition.

Table (#table:study1ParticleParameters) shows the particles parameters for the first computational study.


####Table:  {#table:study1ParticleParameters}

| Name                  	|    Symbol          	| Choice                						|  Units     |
|-------------------------------|-----------------------|-----------------------------------------------------------------------|------------|
|	-			| $C_{tot}/C_s$        	| <span style="color:red"  >   0.20185		 			| -          |
|Total concentration   		| $C_{tot}$           	| <span style="color:red"  > $6.661   \times 10^{-8}$			| $mol/cm^3$ |
|Total volume of the particles  | $V_P$                 | <span style="color:red"  > $2.11007 \times 10^{-4}$ 			| $cm^3$     | 
|Toal drug in the domain 	|                       | <span style="color:red"  > $7.8734  \times 10^{-7}$                 	| $mol$      |
|Maximum particle diameter	| $D_P^{max}$          	| <span style="color:black"> 195	 		 		| $\mu m$    |
|Average particle diameter      | $D_P^{ave}$           | <span style="color:black"> 100                			| $\mu m$    |
|Minimum particle diameter      | $D_P^{min}$           | <span style="color:black"> 5      	   	 			| $\mu m$    |
|Number of particles		| $N_P$			| <span style="color:red"  > 1175 (Figure [#fig:Particle_Distribution_16])	| -	     |
|Distribution function shape	|	-		| <span style="color:black"> Normal	        			| -	     |
|Standard deviation	 	| $\sigma$		| <span style="color:red"  > 25						| $\mu m$    |		
|Number of the bins		| $N_{bins}$		| <span style="color:black"> 20						| -	     |
|Initial particle locations	|	-		| randomly distributed in a sphere 						| -	     |	

Caption: Drug particle properties for the first computational study.



## Particle Distributions

For $\sigma$= 25$\mu m$:

#### Figure: {#fig:Particle_Distribution_16}

![](./Particle_Distribution_16.png){width=99%}

Caption: $\frac{C_{tot}}{C_s}$=0.2 ,  $D_{min}$=5$\mu m$ ,   $D_{max}$=195$\mu m$ ,  $N_{bin}$=20  , $\sigma$=25$\mu m$ ,   $N_P$= 1175 



<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
# Boundary conditions
Table (#table:study1BC) shows the boundary condition choices: 

#### Table:  {#table:study1BC}

| Name      			| Symbol                | Choice                                |  Units      |
|-------------------------------|-----------------------|---------------------------------------|-------------|
| Momentum Boundary Condition	| BounceBack2           | Second order Bounce Back		| -           |
| Scalar  Boundary Condition   	| $\phi_{BC} = 0.0$    	| Immidiate uptake 			| -           |

Caption: Boundary Conditions






<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
# Modeling Parameters
Table (#table:study1ModelingParameters) shows the modeling and computational parameters 

#### Table:  {#table:study1ModelingParameters}

| Name                   		|Symbol | Choice                															|
|---------------------------------------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Partitioning modeling parameter       |$n_d$	| <span style="color:black"> 3 															|
| Bulk concentration modeling parameter	|$n_b$  | <span style="color:black"> 2 															|     
| Schmidt number       	 		|$Sc$   | <span style="color:black"> 20    														|             		           
| LBM Relaxation parameter		|$\tau$	| <span style="color:black"> 1 															| 
| Mass conservation fix                 |       | <span style="color:black"> in BC:$\rho$=1, $\rho_{uncov}=\rho_{ave}$, Fix [$\rho, f, f^+$]  							|  
| Directional drug release partitioning |     	| <span style="color:black"> $\Delta \phi_{(i,j,k)} = Overlap_{(i,j,k)} \Big[ \frac{C_s-C_{i,j,k}}{C_s} \Big] \frac{\Delta N_b}{ (\Delta x) ^3}$  |

Caption: Modeling and computational parameters for the first computational study.





<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
#Computational Cost Estimation
#### Table:  {#table:ComputationalCost}

| Name                                  | Symbol                | Choice                                |  Units     |
|---------------------------------------|-----------------------|---------------------------------------|------------|
| Mesh resolution		        | $\Delta x$            | 0.2					| mm         |
| Total number of nodes		        | $N_{nodes}$           | 3 000 000				|            |
| Number of Particles                   | $N_{particles}$       | 1175 	                                |            |
| Time steps		                | $\Delta t$            | 6.66 e-3				| s          |
| Total number of waves simulated       | 	             	| 20		                        |            |
| Wave's charactristice time scale      | $t_{wave}$            | 30					| s          |
| Total physical time		        | $t_{tot}$             | 600                                   | s          |
| Total number of iterations            | $N_{iter}$            | 90 000                                |            |
| Computational cost of each iteration  |			|  					| CPU.s      |
| Total computational Cost		|			|           				| CPU.hour   |
| Total computational Cost		|			| 					| CPU.days   |

Caption: Computational cost estimation



