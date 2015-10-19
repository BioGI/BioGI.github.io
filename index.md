---
title: Wiki for the Bio GI project
author: James Brasseur (PI), Farhad Behafarid and Ganesh Vijayakumar
bibliography: references.bib
---

This page is intended to be a home page for the documentation of the Bio-GI project. This will be expanded in the future.

To generate a new page or modify the contents, please follow the instructions [(How to contribute)](Documentation/HowToModifyWiki.html)


# Summary of previous work done on the Bio project

This is our current understanding of the previous work done on the Bio-project.

## Lattice Boltzmann method applied to an intestine model

Anupam Pal wrote the first Lattice Boltzmann code in Dr. Brasseur's group and applied it to analyze the motility of the Pharynx [@Pal2000]. Gino and Yang Xing developed a Lattice Boltzmann model of the intestine [@Wang2010b]. The nutrients are modeled as a single passive scalar using the Moment-propagation method of Merks et. al. [@Merks2002563]. They also incorporated various existing techniques like 2nd order moving boundary conditions from Lallemand and Luo [@Lallemand2003] and a multiple-grid strategy from Yu, Mei and Shyy [@Yu2002] and extended them to scalars. While the initial development was in 3D, they also wrote a 3D code that was designed to run in parallel [@Banco2010]. 

## Effect of intestinal motility on the nutrient absorption through a Micro-Macro mixing layer

Gino and Yang Xing studied this through the NSF grant. They argued using 2D simulations initially [@Wang2010, @Banco2010] and 3D simulations later [@Wang2015] that the motion of the villi along with the intestinal motility creates a micro-macro mixing layer that enhances the delivery of drug to the intestinal surface .

## Modeling tablet dissolution in a fluid medium

Gordon Amidon et. al. [@Amidon1995] and Horter and Dressman [@Horter200175] show that for poorly soluble substances the ability to go into solution is a more important limitation of absorption than its ability to permeate the intestinal mucosa [@Emilie2009]. Thus it is important to model the in-vivo dissolution of tablets. Former dissolution models have assumed a constant diffusion layer from the particle surface and a monodisperse models of dissolution. Yang Xing and Brasseur studied this through the NSF grant and then in collaboration with Bertol Abrahamson and Lennat Lindfors at Astrazeneca Pharmaceuticals. They created engineering models from first principles for dissolution from a single particle in [@Wang2012] and extended it to a polydisperse model in [@JPS:JPS24472]. They also studied the effect of shear on tablet dissolution through Lattice Boltzmann calculations past a dissolving sphere using very fine meshes and created correlations between the Sherwood number and the shear rate. 

## Modeling tablet dissolution in the gut

Yang Xing and Brasseur tried to combine the previous two capabilities to model this. However, Balaji did most of the coding to track the drug particles in the code in parallel. Yet, he was only able to barely finish the implementation in-vitro in a Couette device. Balaji also noticed problems with conservation of mass in the solver. This is apparently a well known issue with Lattice Boltzmann methods. 

# Lattice Boltmann Method 

## LBM Method References

These are the references we got from Brasseur and Balaji. I have also added some references I found from the web that have been useful. 

* Sukop and Thorne - Lattice Boltzmann Modeling - An Introduction for Geoscientists and Engineers [@Sukop2006]
* Chen and Doolen - Lattice Boltzmann Method for Fluid Flows [@Chen1998]
* Lallemand and Luo - Theory of the lattice Boltzmann method: Dispersion, dissipation, isotropy, Galilean invariance, and stability [@Lallemand2000]
* Mohammad - Lattice Boltzmann Method - Fundamentals and Engineering Applications with Computer Codes [@Mohammad2011]
* Gilberto M Kremer - An Introduction to the Boltzmann Equation and Transport Processes in Gases [@Kremer2010]
* Alexander J Wagner - A Practical Introduction to the Lattice Boltzmann Method [@Wagner2008]
* Ladd [@Ladd1994], [@Ladd1994a] - First order moving boundary conditions
* Lallemand and Luo [@Lallemand2003] - Second order moving boundary conditions
* Merks et. al. [@Merks2002563] - Moment propagation method for scalars
* Yu, Mei and Shyy [@Yu2002] - Multiple grid method for LBM

Please see [Basics of Lattice Boltzmann Method](Documentation/lbmBasics.html) for our current understanding of the Lattice Boltzmann Method

## LBM codes from Balaji, Yang Xing and Gino

We have two codes in our possession. We got both from Balaji.

* 3D Intestine code

    * Based off Gino and Yang Xing's 3D codes
    * Models intestinal motility using combination of Peristalsis and Segmentation
    * Can model villi motion
    * Not sure if it contains multi-grid capability
    * Models scalar advection/diffusion using "Moment Propagation Method"
    * Contains elementary particle dissolution and tracking implmentation (in serial)

* Couette flow device code

    * Based off Gino and Yang Xing's 3D codes
    * Contains most advanced dissolution model for particles in Couette flow device
    * Has parallel particle tracking capability 

We have been able to run both codes and visualize their output.

## Dissolution Physics

Please see [Understanding of Mono vs. Polydisperse dissolution models](Documentation/monoVsPolydisperse.html) for our current understanding of the dissolution models.

We are working on the implementation of the dissolution model in the numerical code [see Implementation of dissolution model](Documentation/Dissolution-Model-Implementation.html) for the physics/mathematical model and [Particle Tracking and Drug Release](Documentation/ParticleTrackingDrugRelease.html) for the implementation in the Couette flow code.

## Attempts to reproduce Gino's 3D results

Please see [Attempts to reproduce Gino's results](Documentation/ginoReproduce.html) for our attempts to reproduce a few of Gino's results.

# References
