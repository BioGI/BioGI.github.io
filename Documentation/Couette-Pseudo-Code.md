# Main.f90
	Setup [MPI, LBM, Geometry, Scalar, Output]

	CALL ICs                

	CALL OpenOutputFiles    
	CALL PrintParams        
	CALL PrintFields        
	CALL PrintStatus        

	CALL IniParticles
	CALL Particle_Setup

	DO iter = iter0, nt
  	   CALL AdvanceGeometry                 
	   CALL Collision                      
	   CALL MPI_Transfer                   
	   CALL Stream   
	   CALL Particle_Track
	   CALL Scalar 		
	   Writing History file
	   Print [Fields, Particles,  Scalar,  Mass, Volume]
	   Print [PeriodicRestart, Status]
	   MPI_BARRIER 
	END

 	CALL PrintTime
	CALL PrintFinalRestart
	Closing


#SetParticle.f90
	CALL RANDOM_SEED (size --> get --> put)
	Defining Monodisperse Collection: 
			Same size, random location
	Defining Polydisperse Collection:
			Different sizes, random locations

#Geometry Module Contains:
	Geometry_Setup
	AdvanceGeometry
	BoundaryPosition
	SurfaceArea
	VilliPosition
	VilliBase
	VilliMove
	VilliTip
	BoundaryVelocity
	SetNodes
	SetNodesVilli
	CalcC
	NeighborVelocity
	SetProperties	
	

 	






#ICBC Module Contains:

	ICs           
	IniParticles 
	IniParticles_Old        
	ScalarDistribution 
	BounceBackL       
	BounceBack2  
	BounceBack2New 
	qCalc         
	BounceBackVL 
	BounceBackV2 
	VilliVelocity
	qCalcV 
	PrintFieldsTEST 
	SymmetryBC 
	SymmetryBC_NODE 
	ScalarBC 
	ScalarBC2
	GetPhiWallNew
	InterpolateProp
	GetPhiWall
	GetPerturbedVector
	RotateVector
	RotateVectorAboutAxis
	IntersectSurface
	Gauss
	ScalarBCV
	Equilibrium_LOCAL 


# ICs (inside ICBC.f90):
	IF (restart) --> Get node locations and fields form restart files
	ELSE         --> set u=1,v=0, w=w(z)

# AdvanceGeometry

	CALL BoundaryPosition
	CALL VilliPosition
	CALL BoundaryVelocity
	CALL SetNodes







