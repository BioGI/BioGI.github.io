---
title:Compiling the codes and running simulations on Summit
author: Farhad Behafarid
date: 17 June 2016
---

# webpages:	

* [Main Webpage:](https://www.rc.colorado.edu/support/getting-started.html)

* [Summit info](https://www.rc.colorado.edu/support/getting-started.html)

* [Webpage for Compiling:](https://www.rc.colorado.edu/support/user-guide/software-compilation.html)

* [Webpage for Running:](https://www.rc.colorado.edu/support/user-guide/batch-queueing.html)

* [Compiling:](https://www.rc.colorado.edu/support/user-guide/software-compilation.html)

* [Submitting Jobs](https://www.rc.colorado.edu/support/user-guide/batch-queueing.html)

# Allocations:
To find out how much CPU-hour remained in your allocation :

  sreport -n -t hours -P cluster AccountUtilizationByUser start=2016-01-01 tree user=fabe134

# Login:	
	ssh fabe1343@login.rc.colorado.edu 

#Password:
	4 digit pin + 6 digit OTP

#Spaces:
	2GB:       /home/user1234 

	250GB:     /projects/user1234
  
	Unlimited (will be purged every 90 days): /scratch/summit/user1234

# Compiling: 	
All softwares compiled on JAnus should be re-compiled on Summit

login to one of the compiling nodes (form a login node):	

	ssh scompile

Load proper modules:

	. /curc/tools/utils/switch_lmod.sh
	. /etc/profile.d/modules.sh
	module load gcc
	module load openmpi/2.0.1

Compile the code:
      
	make

#Used Allocation Report
	sreport cluster AccountUtilizationByUser -t hours user=fabe1343

#Running:

Exit from compiling node and Load slurm module:

	module load slurm/summit
	module load gcc
	module load openmpi/1.8.5
	module load slurm/summit


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

# Installing tmux in Janus
	mkdir local
	mkdir tmp
	mv tmux-1.4 tmp
	mv ncurses-5.7 tmp
	mv libevent-2.0.10-stable tmp
	cd tmp

	cd libevent-2.0.10-stable
	./configure --prefix=$HOME/local
	make
	make install

	cd ../ncureses-5.7
	./configure --prefix=$HOME/local
	make
	make install

	cd ../tmux-1.4
	./configure CPPFLAGS="-I$HOME/local/include -I$HOME/local/include/ncurses" LDFLAGS="-static -L$HOME/local/include -L$HOME/local/include/ncurses -L$HOME/local/lib" make
	cp tmux ~/local/bin
	export PATH=$HOME/local/bin:$PATH	


