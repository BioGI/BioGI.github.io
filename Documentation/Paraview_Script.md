---
title: Creating paraview scripts for movies
author: Farhad Behafarid, Ganesh Vijayakumar
date: 20 June 2016
---



# Save state:

Save Paraview state as "state.py" 




# Add at top of the state.py :
	import sys, glob, commands 




# Flexible input files:

Change inoput file names (both output files and particle files) so they can be defined as an  argument:
	
	out0001000__dat = TecplotReader( guiName="out-0001000-..dat", DataArrayStatus=['u', 'v', 'w', 'P', 'phi', 'node'], FileNames=['/home/farhad/RUNS/Intestine/8-first-Experiment/2-1st-Experiment-for-Abstract/Case-2-B/out-{}-00001.dat'.format(sys.argv[1])] )
	pardat0001000__csv = CSVReader( guiName="pardat-0001000-..csv", FileName=['/home/farhad/RUNS/Intestine/8-first-Experiment/2-1st-Experiment-for-Abstract/Case-2-B/pardat-{}-00001.csv'.format(sys.argv[1])] )


Or using "Replace" option in vim (state.py saved at time step 500 for 2 processors):

	:%s/out\-0000500\-00001\.dat'\])/out\-{}\-00001\.dat'\.format(sys\.argv\[1\])\])/g
	:%s/out\-0000500\-00002\.dat'\])/out\-{}\-00002\.dat'\.format(sys\.argv\[1\])\])/g

	:%s/pardat\-0000600\-00001\.csv'\])/pardat\-{}\-00001\.csv'\.format(sys\.argv\[1\])\])/g



# Add at the Bottom of the state.py: 
	viewLayout = GetLayout()
	WriteImage('tmp1.png', view=RenderView1)
	WriteImage('tmp2.png', view=RenderView2)
	WriteImage('tmp3.png', view=RenderView3)
	WriteImage('tmp4.png', view=RenderView4)
	commands.getoutput("convert -border 1x1 +append tmp*.png T{}.jpg".format(sys.argv[1]))

Note: if one bolus is visualized and for example 4 consecutive sections are desired:

    viewLayout = GetLayout()
    WriteImage('tmp1.jpg', view=RenderView1)
    WriteImage('tmp2.jpg', view=RenderView3)
    commands.getoutput("convert -border 1x1 +append tmp1.jpg tmp1.jpg tmp1.jpg tmp1.jpg TEMP1.jpg".format(sys.argv[1]))
    commands.getoutput("convert -border 1x1 +append tmp2.jpg tmp2.jpg tmp2.jpg tmp2.jpg TEMP2.jpg".format(sys.argv[1]))
    commands.getoutput("convert -border 1x1 -append TEMP* T{}.jpg".format(sys.argv[1]))



# Define the desired time steps:

Create a file called TimeSteps with all desired  steps in one line, separated by "Tab" or "Space".




# Create snapshots:

#### Figure: {#fig:Bash_Loop_pvpython}

![](./Figures/Bash_Loop_pvpython.png){width=40%}

# Make a movie out of the snapshots:
    ffmpeg -framerate 10 -pattern_type glob -i "*.jpg" -vf "fps=25,format=yuv420p" Movie.mp4

# Scaling the movie size:
    ffmpeg -i Movie.mp4 -s 524x440 -c:a copy Movie_mall.mp4

# ADVANCED: Creating Plot snapshots with a moving time indicator line
in creating the plots, "axvline" option should be used. 

An example file called Plot.py can be found below: 

	import numpy as np
    import matplotlib as mpl
    mpl.use('TkAgg')
    import matplotlib.pyplot as plt
    import commands
    from matplotlib.patches import Ellipse, Polygon
    from matplotlib import rc_file
    from pylab import loadtxt
    from pylab import rcParams
    import pickle, sys, os
    os.chdir('../Fasted')
    import Fasted as Case1
    os.chdir('../Plots')
    rcParams['figure.figsize'] = 12.86, 5
    axis_font  = {'fontname':'Arial', 'size':'16'}
  
    tcf = 2.6041666666666665E-003 
    Cs_mol =0.33000
    Cs_gram= 68
    alfa= Cs_gram/Cs_mol
    IC_solid_drug= alfa * 0.78734  
    IT = Case1.IterationNo
  
    for i in IT:
        fig = plt.figure()
        plt.axes([0.13,0.18,0.97-0.13,0.92-0.18])
        plt.plot(Case1.time, Case1.scalarAbsorbtionRate,'-', color= 'blue', label='') 
        plt.grid(b=True, which='major',  axis='y', linewidth=1)
        plt.ylim(0,6)
        plt.xlim(0,160)
        plt.xlabel('Time (s)',**axis_font)
        plt.ylabel('Drug Absorbtion Rate ($\mu g/s$)',**axis_font)
        plt.axvline(linewidth=2, color='red', x=i*tcf)
        plt.legend(loc=0)
        plt.savefig('DrugAbsRate-{:07d}.jpg'.format(int(i)),dpi=300)

To create the plot snapshots using plot.py:

    for i in `cat Times`; do echo "import Plot" | python ; done

After creating the plot snapshots, use the below command to atttach the plot snapshots to the paraview snapshots:

    for i in `cat Times`; do convert ../../"T$i.jpg" "DrugAbsRate-$i.jpg" -append "Viz-Plot-$i.jpg" ; done

# Make a movie out of the snapshots:
    ffmpeg -framerate 10 -pattern_type glob -i "*.jpg" -vf "fps=25,format=yuv420p" Movie.mp4
    ffmpeg -framerate 6  -pattern_type glob -i "*.jpg" -vf "fps=5, format=yuv420p" Movie.mp4 
