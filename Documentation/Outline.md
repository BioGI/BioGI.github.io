---
title: Outline of the Projects
author: Farhad Behafarid
date: 27 June, 2016
---

# Outlines of the Project (Fed)

* **HPC**:
	* Fixing the issue causing drug conservation difference between Serial and Parallel (Not related to particle tracking or drug release)
	* Verifying parallel communications for Negative-$\phi$ monitoring, Mass-Fix and drug monitoring (release,abosrbed,remained,loss) toolsi, directional particle drug release.
	* MPI_Transfer after streaming since $u, v, w, \rho$ are needed in scalar subroutine.
	* Improving HPC scaling (Do-Nothing when particle is dissolved. Remove unnecessary communications)
        * In IC_Drug_Distribution, Blob coordinate are local (for current partition)  which causes problem in case of defining a  blub using global coordinates for parallel simulations.
	* Computational cost and scaling factor studies:
		* 1,2,4 partitions in X/Y 
		* 2,4,8,16 partitions in Z

&nbsp;


* **Finalizing the "restart" option:**
	* Geometry
	* All LBM fields ($u, v, w, P, \rho, \phi$,  all distribution functions)
	* All particle data (26 parameters)
	* All monitoring tools (drug released, drug absorbed, drung remained in domain, drug conservation errors)
	* Serial/Parallel (one file for particles, multiple fiels for other parameters)
	* Writing out at user-defined periodic intervals (not just the final)
	* No Particle restart file if particle tracking is off or if all particles are completely dissolved
	* Verify that the drug conservation monitoring parameters are identical after restart.

&nbsp;

* **Oversaturaion:**
	* Remove ad-hoc drug release in case of  $\delta R > R$ (which ignores the modeling equations and simply reduces the radius to half).
	* Add Fractional-Time-Stepping feature to the latest version of the git repo with flag and $N_f$ in the input file ($N_f$ is the number of fractional time steps inside each LBM time steps).
	* Test Fractional-Time-Stepping by analyzing the extra computational cost vs strength of supressing over-saturation for:
		* $N_f$ = 1
		* $N_f$ = 2
		* $N_f$ = 10
	* Last fix: in directional drug release, when using ($\frac{C_s-C}{C_s}$) as a weighting function, use the new C (after release) instead fo the old C (before release)

&nbsp;

* **Mass-Fix:**
	* Fixing Mass-Fix non-physical effects on scalar (very small and only the first time step)
	* Improving Mass-Fix option by adding the correction term proportional to the magnitude of f in different directions (instead of $f_m = f_m + \frac{Correction}{15}$ for all directions)

&nbsp;

* **Boundary Condition:** 
	* Finalize/verify the book-keeping routines
	* Introducing Permeability Boundary Condition intestine geometry

&nbsp;

* **Hydrodynamic effects:**
	* Introducing the 3D strain rate computation to be used in  hierarchic Sherwood number calculation.
	* Introducing the slip velocity calculations to be used in hierarchic Sherwood number calculation and in particle trackinig.

&nbsp;

* **Others:**

	* Fix the non-zero drug releas after all particles had completely dissolved (it is close to machine precision at each time step, but after tens of thousands of iterations, it becomes detectable).
	* Print out the scalar as non-dimensional ($C/C_s$) for visualizations.
	* Add a feature for plotting the particle distribution PDF as a function of time.


&nbsp;



# Real fed experiments before the FDA meeting deadline (July 24, 2016)

#### Table:  {#table: ExperimentsBeforeDeadline}

| Experiment No.                | Motility                                      | OC                            |Shear Effects                  |$C_{tot}/C_S$  |
|-------------------------------|-----------------------------------------------|-------------------------------|-------------------------------|---------------|
| 1                             |                        Fed,    Peristalsis    | 0.5                           | No                            |0.2            |
| 2                             |                        Fed,    Segmental      | 0.5                           | No                            |0.2            |
| 3                             |                        Fed,    Pristalsis     | 0.5                           | Yes                           |0.2            |
| 4                             |                        Fed,    Segmental      | 0.5                           | Yes                           |0.2            |

Caption: Fed Experiments before the FDA meeting in July 24, 2016
























# Outline of the Project (Fasted)

* Fix the particle tracking issue which lets some particles to get trapped in the solid phase:
	* Use new velocity instead of velocity from previous time step (Move particle-tracking from before to after stream/macro).
	* Add particle location warning tools. 
	* Run the exact simulation that caused the problem using interval-restart-option and let it run to reach the time that particles move out of the domain.
	* Go back to the closest restart file and run the simulation again with printing out all the particle tracking parameters.

* Run fasted simulation (OC= 0.1) using coarse mesh.

* Computational cost analysis (estimating the CPU hour with one processor)

* Dscussion on:
	* Need to reduce the occlusion ratio from 0.1 to 0.05
	* Need to increase the resolution


&nbsp;


# Real fasted experiments before the FDA meeting deadline (July 24, 2016)

Hopefully we can push to perform the corresponding Fasted simulations too:

#### Table:  {#table: FastedExperimentsBeforeDeadline}

| Experiment No.                | Motility                                      | OC                            |Shear Effects                  |$C_{tot}/C_S$  		|
|-------------------------------|-----------------------------------------------|-------------------------------|-------------------------------|-------------------------------|
|<span style="color:red"> 5     |<span style="color:red">Fasted, Pristalsis     |<span style="color:red"> 0.1   |<span style="color:red"> No    |<span style="color:red"> 0.644 |
|<span style="color:red"> 6     |<span style="color:red">Fasted, Segmental      |<span style="color:red"> 0.1   |<span style="color:red"> No    |<span style="color:red"> 0.644 |
|<span style="color:red"> 7     |<span style="color:red">Fasted, Pristalsis     |<span style="color:red"> 0.1   |<span style="color:red"> Yes   |<span style="color:red"> 0.644 |
|<span style="color:red"> 8     |<span style="color:red">Fasted, Segmental      |<span style="color:red"> 0.1   |<span style="color:red"> Yes   |<span style="color:red"> 0.644 |

Caption: Fasted Experiments before the FDA meeting in July 24, 2016

