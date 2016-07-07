---
title: Outline of the Projects
author: Farhad Behafarid
date: 27 June, 2016
---

# Outlines of the Project (Fed)

* **HPC**:
	* <span style="color:blue"> Fixing the issue causing drug conservation difference between Serial and Parallel.
	* <span style="color:blue"> Verifying parallel communications for Negative-$\phi$ monitoring, Mass-Fix and drug monitoring (release,abosrbed,remained,loss) tools, directional particle drug release.
	* <span style="color:blue"> MPI_Transfer after streaming since $u, v, w, \rho$ are needed in scalar subroutine.
	* In IC_Drug_Distribution, Blob coordinate are local (for current partition)  which causes problem in case of defining a  blub using global coordinates for parallel simulations.
	* Computational cost and scaling factor studies for (Serial, 2,4 partitions in X/Y,* 2,4 partitions in Z)

&nbsp;


* **Finalizing the "restart" option:**
	* <span style="color:blue"> Geometry
	* <span style="color:blue"> All LBM fields ($u, v, w, P, \rho, \phi$ and all distribution functions)
	* <span style="color:blue"> All particle data (26 parameters)
	* <span style="color:blue"> All monitoring tools (drug released, drug absorbed, drung remained in domain, drug conservation errors)
	* <span style="color:blue"> Writing out at user-defined periodic intervals (not just the final)
	* <span style="color:blue"> No Particle restart file if particle tracking is off or if all particles are completely dissolved
	* <span style="color:blue"> Write out only one particle data file even in parallel simulations
	* <span style="color:blue"> Verify that the all fields are identical after restart.
	* <span style="color:blue"> Verify that the drug conservation monitoring parameters are identical after restart.
	* <span style="color:blue"> Modifyying hte particle numbers in the Restart-Particles*.dat based on the current remaining particles

&nbsp;

* **Oversaturaion:**
	* Compute the average over-saturaion (using only the oversaturated nodes)
	* Add fractionall-time-stepping flag to the input.dat
	* Add $N_f$ value to the input.dat
	* Add fractional-time-step interval to the input.dat (probably only a few hundred initial time steps)	
	* Remove ad-hoc drug release in case of  $\delta R > R$ (which ignores the modeling equations and simply reduces the radius to half).
	* Add Fractional-Time-Stepping feature to the latest version of the git repo with ON/OFF flag and $N_f$ defined in the input file ($N_f$ is the number of fractional time steps inside each LBM time step).
	* Test Fractional-Time-Stepping by analyzing the extra computational cost vs benefits for $N_f$ = 1, 2, 10
	* Last fix: in directional drug release, when using ($\frac{C_s-C}{C_s}$) as a weighting function, use the new C (after release) instead fo the old C (before release)

&nbsp;

* **Mass-Fix:**
	* <span style="color:blue"> Fixing Mass-Fix non-physical effects on scalar (very small and only the first time step)
	* <span style="color:blue"> Improving Mass-Fix option by adding the correction term proportional to the magnitude of f in different directions (instead of $f_m = f_m + \frac{Correction}{15}$ for all directions)

&nbsp;

* **Boundary Condition:** 
	* <span style="color:blue">  Finalize/verify the book-keeping routines
	* Introducing Permeability Boundary Condition in intestine geometry

&nbsp;

* **Hydrodynamic effects:**
	* Introducing the 3D strain rate computation to be used in hierarchic Sherwood number calculationi.
	* Introducing the slip velocity calculations to be used in hierarchic Sherwood number calculation and in particle trackinig.

&nbsp;

* **Improve computational efficiency:**
	* <span style="color:blue"> Write out particle data in output files only if the particle is not fully dissolved
	* <span style="color:blue"> Write out only one particle data file even in parallel simulations
        * <span style="color:blue"> Write out particle data in restart files only if the particle is not fully dissolved
        * <span style="color:blue"> Write out only one particle restart file even in parallel simulations
        * <span style="color:blue"> Remove the particles from the particle list when it is completely dissolved.
        * <span style="color:blue"> Write out only one particle data file even in parallel simulations.
	* Improving HPC scaling (Do-Nothing when particle is dissolved. Remove unnecessary MPI communications. All processors do the job and remove the MPI communications if otherwise they need to wait for the master)
	* Turn off the particle tracking when all particles are dissolved

&nbsp;

* **Computational Resources**
	* Estimate how long it takes to use all 15000 CPU.hours.
	* Figure out if new assignments are free or not.
	* Write a proposal for more CPU allocations
	* Request larger HD allocations.
	* Explore the possibility of the access to the Penn-State's high priority 80 CPU 
	


&nbsp;


* **Others:**
	* <span style="color:blue"> Introduce a user defined input parameter to set the intervals between the output files (instead of defining approximate number of output files)
	* <span style="color:blue"> Chaning Segmental geometry so that at the initial time step, the highest radius is at the center (consistent with Pristalsis) 
	* <span style="color:blue">  Make sure the values for $C_s$, $\nu_m$ and $D_m$ are correct
	* <span style="color:blue"> Design fed experiments and create a wiki page for it
	* <span style="color:blue"> Remove $C_s$, $\nu_m$ and $D_m$ from Setup.f90 and add them to input.dat
	* <span style="color:blue"> Finalize the computational cost estimation subroutines. 
	* <span style="color:blue"> Fix the non-zero drug releas after all particles are completely dissolved (it is close to machine precision at each time step, but after tens of thousands of iterations, it becomes detectable).
	* <span style="color:blue"> Print out the scalar as non-dimensional ($C/C_s$) for visualizations.
	* Design fasted experiments and create a wiki page for them
	* Add a feature for plotting the particle distribution (PDF) as a function of time.
	* Add the feature to track particles/release drug, only after (at least) one full period of flow simulation (using restart option).
	* Litrature review for a reasonable fed state bolus volume.
	* Feature to plot shear PDf and strain-rate contribution to Sherwood number (at least at each 0.1 of a period)
	* Calculate Strain rate at each node and visualize it.
	* Add the effects of PH on solubility

&nbsp;














# Outline of the Project (Fasted)

* Fix the particle tracking issue which lets some particles to go and get trapped in the solid phase:
	* Use the new velocity instead of velocity from previous time step (Move particle-tracking from before to after stream/macro).
	* Add particle location warning tools (based on both analytical and real geometry). 
	* Find the  particle ID of one of teh particles which is trapped in Solid  phase.
	* Run the exact simulation that caused the problem with only one particle and using Interval-Restart-Option and let it run to reach the time that particles move out of the domain.
	* Go back to the closest restart file and run the simulation again with printing out all the particle tracking parameters for that specific particle.

* Run fasted simulation (OC= 0.1) using coarse mesh.

* Computational cost analysis (estimating the CPU hour with one processor)

* Dscussion on:
	* Need to reduce the occlusion ratio from 0.1 to 0.05
	* Need to increase the resolution


&nbsp;

<!---

# Parallel Communication Issue:

* Fixing the issue causing drug conservation difference between Serial and Parallel (Only happens when Mass-Fix is on)
	* The issue is not related to particle traking or drug release
	* The issue is related to LBM boundary condition:
	* An extreme case for debugging was created (super-Coarse mesh. uniform saturated scalar at IC)
#### Table:  {#table: ExperimentsBeforeDeadline}

| LBM BC order |Error % (1 CPU) | Error % (8 CPU)|
|--------------|----------------|----------------|
| 1            | 4.15           | 4.15           |
| 2            | 0.15           | 0.45           |

Caption: Errors in Serial/Parallel simulations with 1st and 2nd order LBM BC
-->
