---
title: My attempt at implementing a multi-block method in the intestine code
author: Ganesh Vijayakumar
date: 21-26 Oct 2015
bibliography: ../References/references.bib
---

I'll document my attempts at implementing a multi-block method in the intestine code.

The main reason for implemeting a multi-block method in the intestine code is to be able to simulate fasting states, where the occlusion ratio for intestinal motility can go really small. The occlusion ratio is not quite the ratio of the occluded diameter to the total diameter of the domain. 

```math
a &= \frac{0.5 \; D}{ 2 - (\epsilon/a)} \\
\rightarrow \frac{a}{0.5 D} &= \frac{1}{ 2 - (\epsilon/a)} \\
\rightarrow \frac{\epsilon}{0.5 D} &= \frac{\epsilon}{a} \frac{a}{0.5 D} =  \frac{\epsilon}{a} \frac{1}{ 2 - (\epsilon/a)}
```
When $\epsilon/a \ll 2$, $\epsilon/(0.5D)$ will become half of $(\epsilon/a)$.

A rule of thumb is that the the occluded region should be resolved with about $\sim 10$ cells. The estimate of the maximum gut diameter we've been using so far is $D = 0.005m$. Lets say this is resolved with a 100 cells in the $x$ and $y$ directions. The resolution will be $\Delta x = 0.005/100 = 5 \times 10^{-5}m$. Table (#table:resolutionRequirements) shows that the resolution requirements increase severely as the occlusion ratio is dropped. It may not be feasible to acheive a reduction of the grid spacing of $\sim O(20-200)$ times with just two grids. I suspect that we will need atleast 3 grids with a reduction ratio of $m-5$ to simulate the occlusion ratio of 0.01 and may be 4 grids with a similar reduction ratio to simulate the occlusion ratio of 0.001.

#### Table:  {#table:resolutionRequirements}

| $\epsilon/a$ |  $\epsilon/R$ | $\Delta x_f$ | Ratio $\Delta x_c / \Delta x_f$ | $nx_f,  $ny_f = 0.1 D / \Delta x_f$ | $nz_f = L/\Delta x_f$ | $nx_f \times ny_f \times nz_f$ |
|--------------|---------------|--------------|-------------------------------|-------------------------------------|-----------------------|--------------------------------|
|   0.5        |     0.32      | $1.667 \times 10^{-4}$m |  0.3  |    -  |   -    |   -     |
|   0.1        |     0.0527    | $2.631 \times 10^{-5}$m |  1.9  |  19   |   380  |  137k   |
|   0.01       |     0.005     | $2.512 \times 10^{-6}$m |  20   |  200  |  4000  |  157M   |
|   0.001      |     0.0005    | $2.501 \times 10^{-7}$m |  200  |  2000 | 40000  |  159B   |

Caption: Demonstration of resolution requirement in the occluded region as the occlusion ratio $\epsilon/a$ is reduced.


## How to design the extent of the fine mesh

Let's say that we require only two grids. Figure (#multiblockDomainDecomposition) shows the proposed design of a slice of ($x=0$ plane) a cylindrical computational domain and the fine mesh within.


#### Figure: {#multiblockDomainDecomposition}

![](./multiblockDomainDecomposition.png)

Caption: Proposed design of the computational domain and the fine mesh and it's domain decomposition.

The rule of thumb reg. 10 grid points in the occluded region need to be applied uniformly across the entire gut. Thus, if the max diameter of the gut is resolved with 100 points, the inner 10% of the domain needs to be refined at all times as it would have less than 10 cells by definition. If the fine mesh has been designed according to the rule of thumb, the resolution requirements would start to become astronomical very quickly as shown in the last column in Table (#table:resolutionRequirements).

# Actual design of the multi-block/grid algorithm

All these issues , not withstanding, I'm still going ahead with designing the multi-grid algorithm. I had to print out and study the Intestine code in detail. I'll branch off the Intestine code and not the COuette code as I'm not sure of the readiness of this code to simulate intestinal motility. When Farhad makes the merge between the two codes, my mods to the Intestine code should transfer straight away to the merged code.

## Diagrams that help understanding the basics of the intestine 3D code

This will probably belong in it's own section. But I'll just make a brief description of the Intestine 3D code here.

Most of the LBM algorithm is fairly straight forward. The complicated parts involve the communication between processors to exchange information. This is first done by creating local arrays that are padded on the boundaries in each direction like so in `Setup.f90`

```fortran
! Distribution Functions
ALLOCATE(f(0:NumDistDirs,0:nxSub+1,0:nySub+1,0:nzSub+1),                        &
fplus(0:NumDistDirs,0:nxSub+1,0:nySub+1,0:nzSub+1))
! Velocity, Density
ALLOCATE(u(0:nxSub+1,0:nySub+1,0:nzSub+1),                                                      &
v(0:nxSub+1,0:nySub+1,0:nzSub+1),                                                      &
w(0:nxSub+1,0:nySub+1,0:nzSub+1))
ALLOCATE(rho(0:nxSub+1,0:nySub+1,0:nzSub+1))
```

The numbering scheme for the density distribution function and the lattice velocity vectors are shown in Figure (#densityDistribution).

#### Figure: {#densityDistribution}

![](./densityDistribution.png)

Caption: Numbering scheme of the density distribution directions and lattice velocity vectors in the Intestine 3D code.


Now for the complicated second part. The nodes on the boundaries of each processor could potentially interact with another processor in a variety of directions. To understand this, simply think of the information that a node on the faces, edges and corners of the processor boundaries. This is controlled by the temporary arrays `CDx, CDy and CDz` in the subroutine `SubDomainSetup` inside `Setup.f90`. Figure (#commDirs) shows the communication direction vector numbering scheme. 


#### Figure: {#commDirs}

![](./commDirs.png)

Caption: Numbering scheme of the communication direction vectors in the Intestine 3D code.

This is then used to setup the array `SubID` that contains the neighboring processor in each communication direction through the subroutine `SetSubID`.

All of this information is then used to carefully setup the main arrays `msgSend` and `msgRecv` that is transferred across processors. There are a whole host of supporting arrays and variables that describe the structure of the the two main arrays and how to pack it before sending and unpack it after receiving. The optimization of this array is done pretty well and only information that is absolutely required is transferred. For instance, only certain components of the density distribution function is transferred depending upon the communication direction.

* `OppCommDir`
* `f_Comps`
* `fSize`
* `dsSize`
* `uvwSize`
* `YZ_FaceSize`
* `ZX_FaceSize`
* `XY_FaceSize`
* `msgSize`
* `f_SendSize`
* `ds_SendSize`
* `uvw_SendSize`
* `total_SendSize`
* `XY_SendIndex`
* `YZ_SendIndex`
* `XZ_SendIndex`
* `X_SendIndex`
* `Y_SendIndex`
* `Z_SendIndex`
* `Corner_SendIndex`
* `XY_RecvIndex`
* `YZ_RecvIndex`
* `XZ_RecvIndex`
* `X_RecvIndex`
* `Y_RecvIndex`
* `Z_RecvIndex`
* `Corner_RecvIndex`
* `CommDataStart_f`
* `CommDataStart_rho`
* `CommDataStart_phi`
* `CommDataStart_u`
* `CommDataStart_v`
* `CommDataStart_w`


## Current plan to modify the Intestine code

This is the current list of steps to modify the Intestine code to a multigrid code.


1. Copy `Setup, LBM, Geometry, ICBC, Parallel.f90` files into corresponding `_fine` files.
2. Change the variable names in these files to `_fine`
3. In the mani `Geometry.f90` file, introduce a new type of node called `REFINEMESH`. Identify/Flag the required nodes as `REFINEMESH`.
4. Set the geometry parameters for the fine mesh in `Geometry_fine.f90` and the identify the outer nodes as `COARSEMESH`.
5. In the `Main.f90`, change the algorithm to include the sub-iterations for the fine mesh.
6. Introduce interpolation subroutines to transfer density distribution and other stuff between coarse and fine meshes.

The progress on this can be tracked on the [attemptedMultiGrid](https://github.com/BioGI/Codes/commits/attemptedMultigrid) branch of the Github repository.

##Psuedo-code for multigrid implementation in the Main algorithm

The current outline of the time-stepping in Main.f90 looks like this

```fortran
DO iter = iter0-0_lng,nt

      CALL AdvanceGeometry            ! advance the geometry to the next time step [MODULE: Geometry]
      CALL Collision                  ! collision step [MODULE: Algorithm]
      CALL MPI_Transfer               ! transfer the data (distribution functions, density, scalar) [MODULE: Parallel]

      CALL Stream                     ! perform the streaming operation (with Lallemand 2nd order BB) [MODULE: Algorithm]

      CALL Macro                      ! calcuate the macroscopic quantities [MODULE: Algorithm]

      IF(iter .GE. phiStart) THEN
          CALL Scalar             ! calcuate the evolution of scalar in the domain [MODULE: Algorithm]
      END IF

      CALL PrintFields                   ! output the velocity, density, and scalar fields [MODULE: Output]
      CALL PrintScalar                   ! print the total absorbed/entering/leaving scalar as a function of time [MODULE: Output]
      CALL PrintMass                     ! print the total mass in the system (TEST)
      CALL PrintVolume                   ! print the volume in the system (TEST)

      !   CALL PrintPeriodicRestart     ! print periodic restart files (SAFE GUARD) [MODULE: Output]

      CALL PrintStatus              ! print current status [MODULE: Output]

      CALL MPI_BARRIER(MPI_COMM_WORLD,mpierr)       ! synchronize all processing units before next loop [Intrinsic]

END DO
```

This should become

```fortran90
DO iter = iter0-0_lng,nt

      CALL AdvanceGeometry            ! advance the geometry to the next time step [MODULE: Geometry]
      CALL Collision                  ! collision step [MODULE: Algorithm]
      CALL MPI_Transfer               ! transfer the data (distribution functions, density, scalar) [MODULE: Parallel]

      CALL InterpolateToFineGrid      ! Interpolate required variables to fine grid
      DO subIter=1,ratio
          CALL AdvanceGeometry_Fine   ! Advance the geometry on the fine grid
     	  IF (subIter .gt. 1) THEN
     		  CALL Collision_Fine     ! Collision step on the fine grid
	          CALL MPI_Transfer_Fine  ! Transfer the data across processor boundaries on the fine grid
          END IF
     	  IF (subIter .lt. ratio) THEN
         	  CALL Stream_Fine            ! Stream fine grid
	     	  CALL Macro_Fine             ! Calculate Macro properties on fine grid
			  !    CALL Scalar_Fine       ! Calculate Scalar stuff on fine grid
		  END IF
      END DO
	  CALL InterpolateToCoarseGrid    ! Interpolate required variable to coarse grid
	  
      CALL Stream                     ! perform the streaming operation (with Lallemand 2nd order BB) [MODULE: Algorithm]

      CALL Macro                      ! calcuate the macroscopic quantities [MODULE: Algorithm]

      IF(iter .GE. phiStart) THEN
          CALL Scalar             ! calcuate the evolution of scalar in the domain [MODULE: Algorithm]
      END IF

      CALL PrintFields                   ! output the velocity, density, and scalar fields [MODULE: Output]
      CALL PrintScalar                   ! print the total absorbed/entering/leaving scalar as a function of time [MODULE: Output]
      CALL PrintMass                     ! print the total mass in the system (TEST)
      CALL PrintVolume                   ! print the volume in the system (TEST)

      !   CALL PrintPeriodicRestart     ! print periodic restart files (SAFE GUARD) [MODULE: Output]

      CALL PrintStatus              ! print current status [MODULE: Output]

      CALL MPI_BARRIER(MPI_COMM_WORLD,mpierr)       ! synchronize all processing units before next loop [Intrinsic]

END DO
```

## Design of Interpolation from coarse mesh to fine mesh

In this section, I will describe the interface between a coarse and a fine mesh using an example. The coarse mesh has a 101 points in the x and y directions. Points 46-56 in both x and y directions are to be resolved by the fine mesh. The fraction of the total diameter resolved by the fine mesh will be $0.1D$. Figure (#designFineCoarseInterface) shows the interface between the coarse and the fine meshes.


####Figure: {#designFineCoarseInterface}

![x-y plane](./multigridPlan_xy.png){width=75%} \
![x-z plane](./multigridPlan_xz.png){width=49%}
![y-z plane](./multigridPlan_yz.png){width=49%}

Caption: Design of the interface between the fine and coarse meshes for the multigrid algorithm.


### Fine to coarse mesh

The pseudo-code for the interpolation from the fine to coarse mesh should roughly look like this.

```fortran
    do k=1,nzSub
      do j=46,56,10
         do i=46,56
            f(i,j,k) = f_fine(closestFineIindex(x_fine(i)), closestFineJindex(y_fine(j)), closestFineKindex(z_fine(k)))
         end do
      end do
    end do

    do k=1,nzSub
      do j=47,55
         do i=46,56,10
            f(i,j,k) = f_fine(closestFineIindex(x_fine(i)), closestFineJindex(y_fine(j)), closestFineKindex(z_fine(k)))
         end do
      end do
    end do
```

But this doesn't include the directional densities or the temporal interpolation. For temporal interpolation we need 3 time points. Hence, I will need new array(s) to store the spatial interpolation at the 3 time levels. I will use and allocate four arrays, the first two for the bottom and the top x-z planes and then the second two for the remaining points on the front and the back y-z planes. Hence this step will become $\ldots$

```fortran
    real, allocatable, dimension(:,:,:,:) :: fFtoC_topXZ
    real, allocatable, dimension(:,:,:,:) :: fFtoC_bottomXZ
    real, allocatable, dimension(:,:,:,:) :: fFtoC_frontYZ
    real, allocatable, dimension(:,:,:,:) :: fFtoC_backYZ

    allocate(fFtoC_topXZ(m,1:14,3,46:56,nzSub)     !Includes the ends - Indices are directionalDensity, timeLevel, x Index, z Index
    allocate(fFtoC_bottomXZ(m,1:14,3,46:56,nzSub)  !Includes the ends - Indices are directionalDensity, timeLevel, x Index, z Index
    allocate(fFtoC_frontYZ(m,1:14,3,47:55,nzSub)     !Does not include the ends - Indices are directionalDensity, timeLevel, y Index, z Index
    allocate(fFtoC_backYZ(m,1:14,3,47:55,nzSub)      !Does not include the ends - Indices are directionalDensity, timeLevel, y Index, z Index

    !Initialization
    !Do the bottom and top x-z planes first
    do m=1,14
      do k=1,nzSub
         do i=46,56
            fFtoC_bottomXZ(m,3,i,k) = f_fine(m,closestFineIindex(x(i)), closestFineJindex(y(46)), closestFineKindex(z(k))) !Add the latest value to the last(third) time step.
            fFtoC_bottomXZ(m,1,i,k) = fFtoC_bottomXZ(m,2,i,k) !Cycle the second time step to the first time step
			fFtoC_bottomXZ(m,2,i,k) = fFtoC_bottomXZ(m,3,i,k) !Cycle the last time step to the second time step
            fFtoC_topXZ(m,3,i,k) = f_fine(m,closestFineIindex(x(i)), closestFineJindex(y(56)), closestFineKindex(z(k))) !Add the latest value to the last(third) time step.
            fFtoC_topXZ(m,1,i,k) = fFtoC_topXZ(m,2,i,k) !Cycle the second time step to the first time step
			fFtoC_topXZ(m,2,i,k) = fFtoC_topXZ(m,3,i,k) !Cycle the last time step to the second time step
		end do
      end do			
    end do

    !Fill out the remaining points on the front and back y-z planes
    do m=1,14
      do k=1,nzSub
         do j=47,55
            fFtoC_frontYZ(m,3,j,k) = f_fine(m,closestFineIindex(x(46)), closestFineJindex(y(j)), closestFineKindex(z(k))) !Add the latest value to the last(third) time step.
            fFtoC_frontYZ(m,1,j,k) = fFtoC_frontYZ(m,2,j,k) !Cycle the second time step to the first time step
			fFtoC_frontYZ(m,2,j,k) = fFtoC_frontYZ(m,3,j,k) !Cycle the last time step to the second time step
            fFtoC_backYZ(m,3,j,k) = f_fine(m,closestFineIindex(x(56)), closestFineJindex(y(j)), closestFineKindex(z(k))) !Add the latest value to the last(third) time step.
            fFtoC_backYZ(m,1,j,k) = fFtoC_backYZ(m,2,j,k) !Cycle the second time step to the first time step
			fFtoC_backYZ(m,2,j,k) = fFtoC_backYZ(m,3,j,k) !Cycle the last time step to the second time step
		end do
      end do			
    end do

    !Do this every time step
    !Do the bottom and top x-z planes first
    do m=1,14
      do k=1,nzSub
         do i=46,56
            fFtoC_bottomXZ(m,1,i,k) = fFtoC_bottomXZ(m,2,i,k) !Cycle the second time step to the first time step
			fFtoC_bottomXZ(m,2,i,k) = fFtoC_bottomXZ(m,3,i,k) !Cycle the last time step to the second time step
            fFtoC_bottomXZ(m,3,i,k) = f_fine(m,closestFineIindex(x(i)), closestFineJindex(y(46)), closestFineKindex(z(k))) !Add the latest value to the last(third) time step.
			f(m,i,46,k) = temporalInterpolate(fFtoC_bottomXZ(1,i,k),fFtoC_bottomXZ(2,i,k), fFtoC_bottomXZ(3,i,k), desiredTime)			
            fFtoC_topXZ(m,1,i,k) = fFtoC_topXZ(m,2,i,k) !Cycle the second time step to the first time step
			fFtoC_topXZ(m,2,i,k) = fFtoC_topXZ(m,3,i,k) !Cycle the last time step to the second time step
            fFtoC_topXZ(m,3,i,k) = f_fine(m,closestFineIindex(x(i)), closestFineJindex(y(56)), closestFineKindex(z(k))) !Add the latest value to the last(third) time step.
			f(m,i,56,k) = temporalInterpolate(fFtoC_topXZ(1,i,k),fFtoC_topXZ(2,i,k), fFtoC_topXZ(3,i,k), desiredTime)
		end do
      end do			
    end do

    !Fill out the remaining points on the front and back y-z planes
    do m=1,14
      do k=1,nzSub
         do j=47,55
            fFtoC_frontYZ(m,1,j,k) = fFtoC_frontYZ(m,2,j,k) !Cycle the second time step to the first time step
			fFtoC_frontYZ(m,2,j,k) = fFtoC_frontYZ(m,3,j,k) !Cycle the last time step to the second time step
            fFtoC_frontYZ(m,3,j,k) = f_fine(m,closestFineIindex(x(46)), closestFineJindex(y(j)), closestFineKindex(z(k))) !Add the latest value to the last(third) time step.
			f(46,j,k) = temporalInterpolate(fFtoC_frontYZ(1,j,k),fFtoC_frontYZ(2,j,k), fFtoC_frontYZ(3,j,k), desiredTime)
            fFtoC_backYZ(m,1,j,k) = fFtoC_backYZ(m,2,j,k) !Cycle the second time step to the first time step
			fFtoC_backYZ(m,2,j,k) = fFtoC_backYZ(m,3,j,k) !Cycle the last time step to the second time step
            fFtoC_backYZ(m,3,j,k) = f_fine(m,closestFineIindex(x(56)), closestFineJindex(y(j)), closestFineKindex(z(k))) !Add the latest value to the last(third) time step.
			f(m,56,j,k) = temporalInterpolate(fFtoC_backYZ(1,j,k),fFtoC_backYZ(2,j,k), fFtoC_backYZ(3,j,k), desiredTime)			
		end do
      end do			
    end do
```

### Coarse to Fine mesh


As before, temporal interpolation is required. However, this time, spatial interpolation is required as well.

```fortran
    real, allocatable, dimension(:,:,:,:) :: fCtoF_topXZ
    real, allocatable, dimension(:,:,:,:) :: fCtoF_bottomXZ
    real, allocatable, dimension(:,:,:,:) :: fCtoF_frontYZ
    real, allocatable, dimension(:,:,:,:) :: fCtoF_backYZ

    allocate(fCtoF_topXZ(1:14,3,nxSub_fine,nzSub_fine)     !Includes the ends - Indices are directionalDensity, timeLevel, x Index, z Index
    allocate(fCtoF_bottomXZ(1:14,3,nxSub_fine,nzSub_fine)  !Includes the ends - Indices are directionalDensity, timeLevel, x Index, z Index
    allocate(fCtoF_frontYZ(1:14,3,1:nySub_fine-1,nzSub_fine)   !Does not include the ends - Indices are directionalDensity, timeLevel, y Index, z Index
    allocate(fCtoF_backYZ(1:14,3,1:nySub_fine-1,nzSub_fine)    !Does not include the ends - Indices are directionalDensity, timeLevel, y Index, z Index

    !Initialization
    !Do the bottom and top x-z planes first
    do m=1,14
      !x - interpolation first
      do k=1,nzSub_fine, gridRatio
         do i=1,nxSub_fine
	  
            lCxIndex = lowerCoarseXindex(x_fine(i))  ! Lower Coarse x Index
			lCzIndex = lowerCoarseZindex(z_fine(i))  ! Lower Coarse z Index - No interpolation in z

            f1 = f(m,lCxIndex-1,46,k)
            f2 = f(m,lCxIndex,46,k)
            f3 = f(m,lCxIndex+1,46,k)
            f4 = f(m,lCxIndex+2,46,k)
			xInterp = dble( (i-1) % gridRatio) / dble(gridRatio)
			aHat = (-f1 + 3*(f2 - f3) + f4)/6.0
			bHat = 0.5 * (f1 + f3) - f2
			dHat = f2
			cHat = f3 - aHat - bHat - dHat

            fCtoF_bottomXZ(m,3,i,k) = dHat + xInterp * (cHat +  xInterp * (bHat + xInterp * aHat)) !Interpolate the latest value to the last(third) time step            fCtoF_bottomXZ(m,1,i,k) = fCtoF_bottomXZ(m,2,i,k) !Cycle the second time step to the first time step
			fCtoF_bottomXZ(m,2,i,k) = fCtoF_bottomXZ(m,3,i,k) !Cycle the last time step to the second time step

            f1 = f(m,lCxIndex-1,56,k)
            f2 = f(m,lCxIndex,56,k)
            f3 = f(m,lCxIndex+1,56,k)
            f4 = f(m,lCxIndex+2,56,k)
			xInterp = dble(i % gridRatio - 1) / dble(gridRatio)
			aHat = (-f1 + 3*(f2 - f3) + f4)/6.0
			bHat = 0.5 * (f1 + f3) - f2
			dHat = f2
			cHat = f3 - aHat - bHat - dHat

            fCtoF_topXZ(m,3,i,k) = dHat + xInterp * (cHat +  xInterp * (bHat + xInterp * aHat)) !Interpolate the latest value to the last(third) time step               fCtoF_topXZ(m,1,i,k) = fCtoF_topXZ(m,2,i,k) !Cycle the second time step to the first time step
			fCtoF_topXZ(m,2,i,k) = fCtoF_topXZ(m,3,i,k) !Cycle the last time step to the second time step

         end do
      end do			

      !Now z - interpolation
      do k=1,nzSub_fine
         do i=1,nxSub_fine
	        IF ( (k-1) % gridRatio ) THEN
			lCzIndex = k - ((k-1) % gridRatio)  ! Lower Coarse z Index - No interpolation in z

            f1 = fCtoF_bottomXZ(m,lCxIndex-1,46,k)
            f2 = f(m,lCxIndex,46,k)
            f3 = f(m,lCxIndex+1,46,k)
            f4 = f(m,lCxIndex+2,46,k)
			xInterp = dble(i % gridRatio) / dble(gridRatio)
			aHat = (-f1 + 3*(f2 - f3) + f4)/6.0
			bHat = 0.5 * (f1 + f3) - f2
			dHat = f2
			cHat = f3 - aHat - bHat - dHat

            fCtoF_bottomXZ(m,3,i,k) = dHat + xInterp * (cHat +  xInterp * (bHat + xInterp * aHat)) !Interpolate the latest value to the last(third) time step            fCtoF_bottomXZ(m,1,i,k) = fCtoF_bottomXZ(m,2,i,k) !Cycle the second time step to the first time step
			fCtoF_bottomXZ(m,2,i,k) = fCtoF_bottomXZ(m,3,i,k) !Cycle the last time step to the second time step

            f1 = f(m,lCxIndex-1,56,k)
            f2 = f(m,lCxIndex,56,k)
            f3 = f(m,lCxIndex+1,56,k)
            f4 = f(m,lCxIndex+2,56,k)
			xInterp = dble(i % gridRatio) / dble(gridRatio)
			aHat = (-f1 + 3*(f2 - f3) + f4)/6.0
			bHat = 0.5 * (f1 + f3) - f2
			dHat = f2
			cHat = f3 - aHat - bHat - dHat

            fCtoF_topXZ(m,3,i,k) = dHat + xInterp * (cHat +  xInterp * (bHat + xInterp * aHat)) !Interpolate the latest value to the last(third) time step               fCtoF_topXZ(m,1,i,k) = fCtoF_topXZ(m,2,i,k) !Cycle the second time step to the first time step
			fCtoF_topXZ(m,2,i,k) = fCtoF_topXZ(m,3,i,k) !Cycle the last time step to the second time step
			END IF
         end do
      end do			


    end do

    !Fill out the remaining points on the front and back y-z planes
    do m=1,14
      do k=1,nzSub
         do j=47,55
            fCtoF_frontYZ(m,3,j,k) = f_fine(m,closestFineIindex(x_fine(46)), closestFineJindex(y_fine(j)), closestFineKindex(z_fine(k))) !Add the latest value to the last(third) time step.
            fCtoF_frontYZ(m,1,j,k) = fCtoF_frontYZ(m,2,j,k) !Cycle the second time step to the first time step
			fCtoF_frontYZ(m,2,j,k) = fCtoF_frontYZ(m,3,j,k) !Cycle the last time step to the second time step
            fCtoF_backYZ(m,3,j,k) = f_fine(m,closestFineIindex(x_fine(56)), closestFineJindex(y_fine(j)), closestFineKindex(z_fine(k))) !Add the latest value to the last(third) time step.
            fCtoF_backYZ(m,1,j,k) = fCtoF_backYZ(m,2,j,k) !Cycle the second time step to the first time step
			fCtoF_backYZ(m,2,j,k) = fCtoF_backYZ(m,3,j,k) !Cycle the last time step to the second time step
		end do
      end do			
    end do
    



```

