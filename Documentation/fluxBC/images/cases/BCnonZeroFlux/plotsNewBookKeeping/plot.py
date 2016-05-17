import matplotlib.pyplot as plt
import commands
from matplotlib.patches import Ellipse, Polygon
import numpy as np
from matplotlib import rc_file
from pylab import loadtxt
import pickle, sys, os


os.chdir('../Moving')
import moving as Moving
os.chdir('../Stationary')
import stationary as Stationary
os.chdir('../plots')

fig = plt.figure()
plt.axes([0.13,0.18,0.97-0.13,0.92-0.18])

plt.plot(Stationary.time, (Stationary.phiOUTleft-Stationary.phiINleft)*1e6,'-', color= 'red', label='Stationary')
plt.plot(Moving.time, (Moving.phiOUTleft-Moving.phiINleft)*1e6,'-', color= 'black', label='Moving')
plt.grid(b=True, which='major',  axis='y', linewidth=1)
#plt.xlim(0,750)
plt.xlabel('Time (s)')
plt.ylabel('phi Absorbed Left ($\mu$ mol)')
plt.legend(loc=0)
plt.savefig('phiAbsleft.png')

fig = plt.figure()
plt.axes([0.13,0.18,0.97-0.13,0.92-0.18])
plt.plot(Stationary.time, (Stationary.phiOUTright-Stationary.phiINright)*1e6,'-', color= 'red', label='Stationary')
plt.plot(Moving.time, (Moving.phiOUTright-Moving.phiINright)*1e6,'-', color= 'black', label='Moving')
plt.grid(b=True, which='major',  axis='y', linewidth=1)
#plt.xlim(0,750)
plt.xlabel('Time(s)')
plt.ylabel('phi Absorbed Right ($\mu$ mol)')
plt.legend(loc=0)
plt.savefig('phiAbsright.png')

fig = plt.figure()
plt.axes([0.13,0.18,0.97-0.13,0.92-0.18])
plt.plot(Stationary.time, (Stationary.phiOUTright-Stationary.phiINright)*1e6-(Stationary.phiOUTleft-Stationary.phiINleft)*1e6,'-', color= 'red', label='Stationary')
plt.plot(Moving.time, (Moving.phiOUTright-Moving.phiINright)*1e6-(Moving.phiOUTleft-Moving.phiINleft)*1e6 ,'-', color= 'black', label='Moving')
plt.grid(b=True, which='major',  axis='y', linewidth=1)
#plt.xlim(0,750)
plt.xlabel('Time (s)')
plt.ylabel('phi Absorbed (Right-Left) ($\mu$ mol)')
plt.legend(loc=0)
plt.savefig('phiAbsDiff.png')


fig = plt.figure()
plt.axes([0.13,0.18,0.97-0.13,0.92-0.18])
plt.plot(Stationary.time, Stationary.scalarAbsorbed,'-', color= 'red', label='Stationary')
plt.plot(Moving.time, Moving.scalarAbsorbed,'-', color= 'black', label='Moving')
plt.grid(b=True, which='major',  axis='y', linewidth=1)
#plt.xlim(0,2.3)
plt.xlabel('Time (s)')
plt.ylabel('Drug Absorbed ($\mu$ mol)')
plt.legend(loc=0)
plt.savefig('DrugAbsorbed.png')

fig = plt.figure()
plt.axes([0.13,0.18,0.97-0.13,0.92-0.18])
plt.plot(Stationary.time, Stationary.scalarRemained,'-', color= 'red', label='Stationary')
plt.plot(Moving.time, Moving.scalarRemained,'-', color= 'black', label='Moving')
plt.grid(b=True, which='major',  axis='y', linewidth=1)
#plt.xlim(0,2.3)
plt.xlabel('Time (s)')
plt.ylabel('Drug Remained in Domain ($\mu$ mol)')
plt.legend(loc=0)
plt.savefig('DrugRemained.png')


fig = plt.figure()
plt.axes([0.13,0.18,0.97-0.13,0.92-0.18])
plt.plot(Stationary.time, Stationary.scalarError,'-', color= 'red', label='Stationary')
plt.plot(Moving.time, Moving.scalarError,'-', color= 'black', label='Moving')
plt.grid(b=True, which='major',  axis='y', linewidth=1)
#plt.xlim(0,2.3)
plt.xlabel('Time (s)')
plt.ylabel('Drug loss (%)')
plt.legend(loc=0)
plt.savefig('DrugLoss.png')

commands.getoutput("convert -border 2x2 -append phiAbsleft.png  phiAbsright.png phiAbsDiff.png DrugAbsorbed.png DrugRemained.png DrugLoss.png Drug.png")

commands.getoutput("chromium Drug.png")

