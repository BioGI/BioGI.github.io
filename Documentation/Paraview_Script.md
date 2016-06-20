---
title: Creating paraview scripts for movies
author: Farhad Behafarid, Ganesh Vijayakumar
date: 20 June 2016
---



# Save state:

Save Paraview state as "state.py" (preferably at time step 0)




# Add at top of the state.py :
	import sys, glob, commands 




# Flexible input files:

Change inoput file names (both output files and particle files) so they can be defined as an  argument:
	
	out0001000__dat = TecplotReader( guiName="out-0001000-..dat", DataArrayStatus=['u', 'v', 'w', 'P', 'phi', 'node'], FileNames=['/home/farhad/RUNS/Intestine/8-first-Experiment/2-1st-Experiment-for-Abstract/Case-2-B/out-{}-00001.dat'.format(sys.argv[1])] )
	pardat0001000__csv = CSVReader( guiName="pardat-0001000-..csv", FileName=['/home/farhad/RUNS/Intestine/8-first-Experiment/2-1st-Experiment-for-Abstract/Case-2-B/pardat-{}-00001.csv'.format(sys.argv[1])] )


Or using "Replace" option in vim: 

	:%s/out\-0000000-00001\.dat'\] )/out\-{}\-00001\.dat'\.format(sys\.argv\[1\])\] ) /g
	:%s/pardat\-0000000\-00001\.csv'\] )/pardat\-{}\-00001\.csv'\.format(sys\.argv\[1\])\] ) /g




# Add at the Bottom of the state.py: 
	viewLayout = GetLayout()
	WriteImage('tmp1.png', view=RenderView1)
	WriteImage('tmp2.png', view=RenderView2)
	WriteImage('tmp3.png', view=RenderView3)
	WriteImage('tmp4.png', view=RenderView4)
	commands.getoutput("convert -border 1x1 +append tmp*.png T{}.jpg".format(sys.argv[1]))




# Define the desired time steps:

Create a file called TimeSteps with all desired  steps in one line, separated by "Tab" or "Space".




# Create snapshots:
	for i in `cat TimeSteps`; do pvpython state.py $i ; done	


# Make a movie out of the snapshots:
	ffmpeg -framerate 10 -pattern_type glob -i "*.jpg" -vf "fps=25,format=yuv420p" Movie.mp4

