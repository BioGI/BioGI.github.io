---
title: Validation using in vitro experimental data
author: Farhad Behafarid
date: 18 Aug 2016
---

The Couette experiments were desined to investigate the influence of shear effects on drug release from a distribution of particles. 


<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
# Geometry and Flow 

Table (#table:CouetteGeometry) describes the geometry and the flow for the in vivo experiment.

#### Table:  {#table:CouetteGeometry}

|Parameter             |Symbol   | value     |Unit  |  
|----------------------|---------|-----------|------|
|Outer diameter        |R_1      | 13.81     |$mm$  |
|Inner diameter        |R_2      | 12.575    |$mm$  |
|Gap                   |$\delta$ | 1.235     |$mm$  |
|Total volume (Fluid)  |$V_f$    | 12        |$cm^3$|
|Rotational speed      |$\omega$ |0.5,10,100 |RPM   |

Caption: In vivo Geometry and flow.




<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
# Drug and Fluid properties

Table (#table:study1DrugFluidParams) shows the drug and fluid properties for the first computational study.

#### Table:  {#table:study1DrugFluidParams}

| Name                         | Symbol |Choice                        |  Unit         |  
|------------------------------|--------|------------------------------|---------------|
| Drug                         |        |Benzoic Acid                  |               |
| Fluid                        |        |Density Matched Solution (DMS)|               |
| Fluid's temperature          |$T_w$   |20                            | $^{\circ}C$   |
| Fluid's PH                   |$PH_w$	|7                             |               |
| Fluid's density              |$\rho_f$|1.29         			           | $g/cm^3$      |
| Fluid's dynamic viscosity    |$\mu_f$ |6.72                          | $cp$          |
| Fluid's dynamic viscosity    |$\mu_f$ |0.00672                       | $kg/m.s$      |
| Fluid's kinematic viscosity  |$\nu_w$ |$5.21 \times 10^{-6}$         | $m^2/s$       |
| Drug's molecular mass        |        |122.12                        | $g/mol$       |  
| Drug's density               |$\rho_m$|1.29		                       | $g/cm^3$	     |	    	
| Drug's molar volume          |$\nu_m$ |92.73                         | $cm^3/mol$    |
| Drug's diffusivity           |$D_m$   |$8.47 \times 10^{-7}$         | $cm^2/s$  	   |
| Solubility in DMS            |$C_S$   |0.368                         | $mg/cm^3$     |
| Solubility in DMS            |$C_S$   |3.149                         | $\mu mol/cm^3$|

Caption: Drug and fluid properties in the vivo experiment.






<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
<!----------------------------------------------------------------------------------------------------------------------------------------------------------->
# Particles

Total dose: Choose $C_{tot}/C_s =0.2$ to be such that we are in sink conditions and far from the singularity near $C_{tot}/C_s = 1$. 
We choose this even though that singularity is only for the case without absorption and we do have absorption in the intestine case.

"BOLUS DOSE": mass or moles of drug in a bolus segment. To estimate we will collect data from the literature and from UM on concentration of extracted fluids -- statistics. From MRI (Nottingham) we will estimate bolus volume. These two will give us dose in moles from which bolus $C_{tot}$ can be estimated. To this end, we need to estimate solid content along with fluid concentration in the extracted segments. Once we have ranges of $C_{tot}$ we can estimate ranges of  $C_{tot}/C_s$ -- our critical parameter.


Choice of where to locate the particles at the initial condition.

Table (#table:study1ParticleParameters) shows the particles parameters for the first computational study.


####Table:  {#table:study1ParticleParameters}

| Name                        	|    Symbol          	  | Choice                                       			                 			|  Units     |
|-------------------------------|-----------------------|-------------------------------------------------------------------------|------------|
|	-		                        	| $C_{tot}/C_s$        	| 1.08                                                                    | -          |
|Total volume of the particles  | $V_P$                 | <span style="color:black"  > $2.11   \times 10^{-4}$                  	| $cm^3$     | 
|Toal drug in the domain      	|                       | <span style="color:black"  > 0.78734                                  	| $\mu mol$  |
|Toal drug in the domain      	|                       | <span style="color:black"  > 162.2                	                    | $\mu g$    |
|Maximum particle diameter    	| $D_P^{max}$          	| <span style="color:black"> 195	 		 		                                | $\mu m$    |
|Average particle diameter      | $D_P^{ave}$           | <span style="color:black"> 100                			                    | $\mu m$    |
|Minimum particle diameter      | $D_P^{min}$           | <span style="color:black"> 5      	   	 			                          | $\mu m$    |
|Number of particles	         	| $N_P$			            | <span style="color:black"> 1175 (Figure [#fig:Particle_Distribution_16])| -	         |
|Distribution function shape	  |	-	                   	| <span style="color:black"> Normal	        			                        | -	         |
|Standard deviation	 	          | $\sigma$		          | <span style="color:black"  > 25						                              | $\mu m$    |		
|Number of the bins		          | $N_{bins}$        		| <span style="color:black"> 20				                                   	| -	         |
|Initial particle locations	    |	-		                  | randomly distributed in a sphere 						                            | -	         |	

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

| Name                                  	| Symbol          | Choice      | Units |
|-----------------------------------------------|-----------------|-------------|-------|
| Mesh resolution		        	| $\Delta x$      | 0.2		| mm    |
| Total number of nodes		        	| $N_{nodes}$     | 3 000 000	|       |
| Number of Particles                   	      | $N_{particles}$ | 1175        |       |
| Time steps		               	                | $\Delta t$      | 6.66 e-3	| s     |
| Total number of waves simulated             	| 	          | 20	        |       |
| Wave's charactristice time scale             	| $t_{wave}$      | 30		| s     |
| Total physical time		                      	| $t_{tot}$       | 600         | s     |
| Total number of iterations           		      | $N_{iter}$      | 90 000      |       |
| Computational time at each iteration (8 CPU)	|		  | 1		| s     |
| Total computational time			                |		  | 25         	| hour  |

Caption: Computational cost estimation



