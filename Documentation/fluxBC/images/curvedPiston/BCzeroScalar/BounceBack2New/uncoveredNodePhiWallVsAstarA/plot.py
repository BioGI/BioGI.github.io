import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import commands
from matplotlib.patches import Ellipse, Polygon
import numpy as np
from matplotlib import rc_file
from pylab import loadtxt
import pickle, sys, os

cases = ['uncoveredNodePhiWall','AstarA']

os.chdir('../../uncoveredNodePhiWall/run/')
import uncoveredNodePhiWall as case0
os.chdir('../../AstarA/run/')
import AstarA as case1
os.chdir('../../plots/uncoveredNodePhiWallVsAstarA')

fig = plt.figure()
plt.axes([0.13,0.18,0.97-0.13,0.92-0.18])

plt.plot(case0.time, (case0.phiOUTleft-case0.phiINleft)*1e6,'-', color= 'red', label=cases[0])
plt.plot(case1.time, (case1.phiOUTleft-case1.phiINleft)*1e6,'-', color= 'black', label=cases[1])
plt.grid(b=True, which='major',  axis='y', linewidth=1)
#plt.xlim(0,750)
plt.xlabel('Time (s)')
plt.ylabel('phi Absorbed Left ($\mu$ mol)')
plt.legend(loc=0)
plt.savefig('phiAbsleft.png')

fig = plt.figure()
plt.axes([0.13,0.18,0.97-0.13,0.92-0.18])
plt.plot(case0.time, (case0.phiOUTright-case0.phiINright)*1e6,'-', color= 'red', label=cases[0])
plt.plot(case1.time, (case1.phiOUTright-case1.phiINright)*1e6,'-', color= 'black', label=cases[1])
plt.grid(b=True, which='major',  axis='y', linewidth=1)
#plt.xlim(0,750)
plt.xlabel('Time(s)')
plt.ylabel('phi Absorbed Right ($\mu$ mol)')
plt.legend(loc=0)
plt.savefig('phiAbsright.png')

fig = plt.figure()
plt.axes([0.13,0.18,0.97-0.13,0.92-0.18])
plt.plot(case0.time, (case0.phiOUTright-case0.phiINright)*1e6-(case0.phiOUTleft-case0.phiINleft)*1e6,'-', color= 'red', label=cases[0])
plt.plot(case1.time, (case1.phiOUTright-case1.phiINright)*1e6-(case1.phiOUTleft-case1.phiINleft)*1e6 ,'-', color= 'black', label=cases[1])
plt.grid(b=True, which='major',  axis='y', linewidth=1)
#plt.xlim(0,750)
plt.xlabel('Time (s)')
plt.ylabel('phi Absorbed (Right-Left) ($\mu$ mol)')
plt.legend(loc=0)
plt.savefig('phiAbsDiff.png')


fig = plt.figure()
plt.axes([0.13,0.18,0.97-0.13,0.92-0.18])
plt.plot(case0.time, case0.scalarAbsorbed,'-', color= 'red', label=cases[0])
plt.plot(case1.time, case1.scalarAbsorbed,'-', color= 'black', label=cases[1])
plt.grid(b=True, which='major',  axis='y', linewidth=1)
#plt.xlim(0,2.3)
plt.xlabel('Time (s)')
plt.ylabel('Drug Absorbed ($\mu$ mol)')
plt.legend(loc=0)
plt.savefig('DrugAbsorbed.png')

fig = plt.figure()
plt.axes([0.13,0.18,0.97-0.13,0.92-0.18])
plt.plot(case0.time, case0.scalarRemained,'-', color= 'red', label=cases[0])
plt.plot(case1.time, case1.scalarRemained,'-', color= 'black', label=cases[1])
plt.grid(b=True, which='major',  axis='y', linewidth=1)
#plt.xlim(0,2.3)
plt.xlabel('Time (s)')
plt.ylabel('Drug Remained in Domain ($\mu$ mol)')
plt.legend(loc=0)
plt.savefig('DrugRemained.png')


fig = plt.figure()
plt.axes([0.13,0.18,0.97-0.13,0.92-0.18])
plt.plot(case0.time, case0.scalarError,'-', color= 'red', label=cases[0])
plt.plot(case1.time, case1.scalarError,'-', color= 'black', label=cases[1])
plt.grid(b=True, which='major',  axis='y', linewidth=1)
#plt.xlim(0,2.3)
plt.xlabel('Time (s)')
plt.ylabel('Drug loss (%)')
plt.legend(loc=0)
plt.savefig('DrugLoss.png')

#commands.getoutput("convert -border 2x2 -append phiAbsleft.png  phiAbsright.png phiAbsDiff.png DrugAbsorbed.png DrugRemained.png DrugLoss.png Drug.png")

#commands.getoutput("chromium Drug.png")

