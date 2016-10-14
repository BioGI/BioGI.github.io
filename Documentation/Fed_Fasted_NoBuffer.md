---
title: Fed Experiments
author: Farhad Behafarid
date: 30 June 2016
---

The 4 experiments are summerized in Table (#table:FedExperiments):

#### Table:  {#table:FedExperiments}

|Exp. No.|State/Motility      |Shear Effects |Buffer |
|--------|--------------------|--------------|-------|
|1       |Peristalsis, Fed    |Yes           |0 mM   |
|2       |Peristalsis, Fasted |Yes           |0 mM   |
|3       |Peristalsis, Fed    |Yes           |10.5 mM|
|4       |Peristalsis, Fasted |Yes           |10.5 mM|

Caption: Experiments

The input parameters that need to be specified for the different experiments fall into different categories, viz., geometry and motility, drug and fluid properties, particle information, boundary conditions and the correlations for shear and hydrodynamic effects. 


<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
# Geometry and Motility

Table (#table:study1GeomMotilityParams) describes the geometry and motility parameters of the first computational study.

#### Table:  {#table:study1GeomMotilityParams}

|Name            |Symbol            | Fed        | Fasted     | Unit |  
|----------------|------------------|------------|------------|------|
|Motility type   |-                 |Peristalsis |Peristalsis |      |
|Max diameter    |$D_{max}$         |22.4        |20          |$mm$  |
|Wavelength      |$\lambda$         |60	         |30	        |$mm$  |
|Volume of bolus |$V_C$		          |11.82       |3.67        |$cm^3$|
|Occlusion ratio |$\epsilon/R_{max}$|0.5         |0.1         |-     |
|Number of waves |-                 |1           |1           |-     |

Caption: Geometry and motility properties for the first computational study.






<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
# Drug and Fluid properties

Table (#table:study1DrugFluidParams) shows the drug and fluid properties for the first computational study.

#### Table:  {#table:study1DrugFluidParams}

| Name                 	             |Symbol   |Choice           	           |Unit    	     |  
|------------------------------------|---------|-----------------------------|---------------|
| Fluid                		           |         |Water                        |               |
| Fluid's temperature                |$T_w$    |20                           |$^{\circ}C$    |
| Fluid's PH                         |$pH_{,b}$|6.5					                 |               |
| Fluid's density                    |$\rho_w$ |1000	                       |$kg/m^3$       |
| Fluid's dynamic viscosity          |$\mu_w$  |$1$                          |$cp$   	       |
| Fluid's kinematic viscosity        |$\nu_w$  |$1.0e-6$                     |$m^2/s$   	   |
| Drug                 		           |	       |Ibuprofen	   			           | 	     	       |
| Drug's molar volume                |$\nu_d$  |268                          |$cm^3/mol$     |
| Drug's molecular wight             |$M_d$    |206.285                      |$g/mol$        |  
| Drug's diffusivity                                         |$D_d$    |$7.5 \times 10^{-6}$         |$cm^2/s$       |
| Drug's  density                                            |$\rho_d$ |<span style="color:red">1.03 |$g/cm^3$       |
| Interinsic solubility                                      |$S_o$    | $0.33$                      |$\mu mol/cm^3$ |
| Interinsic Solubility                                      |$S_o$    | $68$                        |$\mu g/cm^3$   |
| Bulk solubility over interinsic solubility ($pH_{,b}$=6.5) |$S_b/S_o$| 126.893                     | -             |
| Bulk solubility ($pH_{,b}$=6.5)                            |$S_b$    | 41.87                       |$\mu mol/cm^3$ |
| Bulk solubility ($pH_{,b}$=6.5)                            |$S_b$    | 8628.7                      |$\mu g/cm^3$   |

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

| Name                        	|    Symbol     | Choice                                   | Units        |
|-------------------------------|---------------|------------------------------------------|--------------|
|Toal drug in the domain      	|               |1.0                 	                     |$mg$          |
|Toal drug in the domain      	|               |4.848                                     |$\mu mol$     |
|Total volume of the particles  |$V^{tot}_d$    |$1.299 \times 10^{-3}$                    |$cm^3$        | 
|Maximum particle diameter    	|$D_P^{max}$  	|195	 		 		                             |$\mu m$       |
|Average particle diameter      |$D_P^{ave}$    |100                			                 |$\mu m$       |
|Minimum particle diameter      |$D_P^{min}$    |5      	   	 			                       |$\mu m$       |
|Number of particles	         	|$N_P$			    |? (Figure [#fig:Particle_Distribution_16])|-	            |
|Distribution function shape	  |-	           	|Normal	        			                     |-	            |
|Standard deviation	 	          |$\sigma$	      |25						                             |$\mu m$       |		
|Number of the bins		          |$N_{bins}$   	|20				                                 |-	            |
|Initial particle locations	    |-		          |Randomly distributed in a sphere 				 |-	            |	
|Total concentration            |$C_{tot}$      |Fed:84.6, Fasted:272.5                    |$\mu g/cm^3$  | 
|Total concentration            |$C_{tot}$      |Fed:0.41, Fasted:1.32                     |$\mu mol/cm^3$| 
|Total concentration            |$C_{tot}/C_o$  |Fed:0.01, Fasted:0.03                     |$\mu mol/cm^3$| 


Caption: Drug particle properties for the first computational study.



## Particle Distributions

For $\sigma$= 25$\mu m$:

#### Figure: {#fig:Particle_Distribution_16}

![](./Figures/Particle_Distribution_16.png){width=99%}

Caption: $\frac{C_{tot}}{C_s}$=0.2 ,  $D_{min}$=5$\mu m$ ,   $D_{max}$=195$\mu m$ ,  $N_{bin}$=20  , $\sigma$=25$\mu m$ ,   $N_P$= 1175 



<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
# Boundary conditions
Table (#table:study1BC) shows the boundary condition choices: 

#### Table:  {#table:study1BC}

| Name                     			| Symbol                | Choice                   |  Units      |
|-------------------------------|-----------------------|--------------------------|-------------|
| Momentum Boundary Condition	  | BounceBack2           | Second order Bounce Back | -           |
| Scalar  Boundary Condition   	| $\phi_{BC} = 0.0$    	| Immidiate uptake 			   | -           |

Caption: Boundary Conditions






<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
# Modeling Parameters
Table (#table:study1ModelingParameters) shows the modeling and computational parameters 

#### Table:  {#table:study1ModelingParameters}

| Name                              		|Symbol | Choice                												               			|
|---------------------------------------|-------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Partitioning modeling parameter       |$n_d$	| <span style="color:black"> 3 															|
| Bulk concentration modeling parameter	|$n_b$  | <span style="color:black"> 2 															|     
| Schmidt number       	            		|$Sc$   | <span style="color:black"> 20    														|             		           
| LBM Relaxation parameter	           	|$\tau$	| <span style="color:black"> 1 															| 
| Mass conservation fix                 |       | <span style="color:black"> in BC:$\rho$=1, $\rho_{uncov}=\rho_{ave}$, Fix [$\rho, f, f^+$]  							|  
| Directional drug release partitioning |     	| <span style="color:black"> $\Delta \phi_{(i,j,k)} = Overlap_{(i,j,k)} \Big[ \frac{C_s-C_{i,j,k}}{C_s} \Big] \frac{\Delta N_b}{ (\Delta x) ^3}$  |

Caption: Modeling and computational parameters for the first computational study.





<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
#Computational Cost Estimation
#### Table:  {#table:ComputationalCost}

| Name                                  	   |Symbol          |Choice          | Units |
|--------------------------------------------|----------------|----------------|-------|
| Mesh resolution		        	               |$\Delta x$      |0.2		         | mm    |
| Total number of nodes		        	         |$N_{nodes}$     |3 000 000	     |       |
| Number of Particles                   	   |$N_{particles}$ |?               |       |
| Time steps		               	           	 |$\Delta t$      |6.66 e-3	       | s     |
| Total number of waves simulated       	   |	              |Fed:20/Fasted:40|       |
| Wave's charactristice time scale      	   |$t_{wave}$      |Fed:30/Fasted:15| s     |
| Total physical time		                     |$t_{tot}$       |600             | s     |
| Total number of iterations           		   |$N_{iter}$      |?               |       |
| Computational time for 1 iteration (8 CPU) |		            |?		           | s     |
| Total computational time		               |		            |?               | hour  |

Caption: Computational cost estimation


# Results: Case 1

Using 8 processors on Janus.

#### Figure: {#fig:Results_Case1}

![](./Figures/Drug_Case_0mM_Buffer.png){width=70%}

Caption: Results of the case 1 experiment

