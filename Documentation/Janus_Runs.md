---
title:Compiling the codes and running simulations on Janus
author: Farhad Behafarid, Ganesh Vijayakumar
date: 17 June 2016
---

# webpages:	

* [Main Webpage:](https://www.rc.colorado.edu/support/user-guide/batch-queueing.html#interactive_jobs)

* [Webpage for Compiling:](https://www.rc.colorado.edu/support/user-guide/software-compilation.html)

* [Webpage for Running:](https://www.rc.colorado.edu/support/user-guide/batch-queueing.html)


# Login:	
	ssh username@login.rc.colorado.edu 

#Password:
	4 digit pin + 6 digit OTP


# Compiling: 	

login to one of the compiling nodes:	

	ssh janus-compile1


Load proper modules:

	. /curc/tools/utils/switch_lmod.sh
	. /etc/profile.d/modules.sh
	module load gcc
	module load openmpi

Compile the code:
      
	make


#Running:

Exit from compiling node and Load slurm module:

	module load slurm


Create the JobScript.sh following the example below:

	#!/bin/bash                                                               
	#SBATCH -J testJob                      # Job name                                     
	#SBATCH --output myjob.%j.out           # stdout; %j expands to jobid                 
	#SBATCH --qos janus-debug               # queue (you can ask for Janus, janus-debug or janus-long
	#SBATCH --nodes 1                                                             
	#SBATCH --ntasks-per-node 8             # Requesting 8 processors 
	#SBATCH -t 00:30:00                     # max time (half an hour) 
	. /curc/tools/utils/switch_lmod.sh
	. /etc/profile.d/modules.sh
	module load gcc                         # Loading modules
	module load openmpi
	srun ./Intestine.exe                    # Intestine.exe is the executable



# Submitting the job to the queue:

	sbatch JobScript.sh

