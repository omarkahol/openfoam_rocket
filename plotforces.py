import math
from numpy import *
import matplotlib.pyplot as plt
from pylab import *
import os.path
import inspect
import io
import os
curwordir=os.getcwd()


#input from torque file
timeX = loadtxt('output/forcesWS.txt', unpack=True, usecols=[0])
Fxp = loadtxt('output/forcesWS.txt', unpack=True, usecols=[1])
Fyp = loadtxt('output/forcesWS.txt', unpack=True, usecols=[2])
Fzp = loadtxt('output/forcesWS.txt', unpack=True, usecols=[3])
Fxv = loadtxt('output/forcesWS.txt', unpack=True, usecols=[4])
Fyv = loadtxt('output/forcesWS.txt', unpack=True, usecols=[5])
Fzv = loadtxt('output/forcesWS.txt', unpack=True, usecols=[6])
Txp = loadtxt('output/forcesWS.txt', unpack=True, usecols=[10])
Typ = loadtxt('output/forcesWS.txt', unpack=True, usecols=[11])
Tzp = loadtxt('output/forcesWS.txt', unpack=True, usecols=[12])
Txv = loadtxt('output/forcesWS.txt', unpack=True, usecols=[13])
Tyv = loadtxt('output/forcesWS.txt', unpack=True, usecols=[14])
Tzv = loadtxt('output/forcesWS.txt', unpack=True, usecols=[15])

#calculate forces and torques on x,y,z
ro=1
Fx = (Fxp + Fxv)*ro
Fy = (Fyp + Fyv)*ro
Fz = (Fzp + Fzv)*ro

Tx = (Txp + Txv)*ro
Ty = (Typ + Tyv)*ro
Tz = (Tzp + Tzv)*ro


#plot forces
#Fx
FxPlot = plt.plot(timeX, Fx, '*')
plt.title('Variazione di Fx')
plt.xlabel('iterazione')
plt.ylabel('Fx (N)')
plt.savefig('output/Fx.png')
plt.close()

#Fy
FyPlot = plt.plot(timeX, Fy, '*')
plt.title('Variazione di Fy')
plt.xlabel('iterazione')
plt.ylabel('Fy (N)')
plt.savefig('output/Fy.png')
plt.close()

#Fz
FzPlot = plt.plot(timeX, Fz, '*')
plt.title('Variazione di Fz')
plt.xlabel('iterazione')
plt.ylabel('Fz (N)')
plt.savefig('output/Fz.png')
plt.close()

#plot torque
#Tx
TxPlot = plt.plot(timeX, Tx, '*')
plt.title('Variazione di Tx')
plt.xlabel('iterazione')
plt.ylabel('Tx (Nm)')
plt.savefig('output/Tx.png')
plt.close()

#Ty
TyPlot = plt.plot(timeX, Ty, '*')
plt.title('Variazione di Ty')
plt.xlabel('iterazione')
plt.ylabel('Ty (Nm)')
plt.savefig('output/Ty.png')
plt.close()

#Tz
TzPlot = plt.plot(timeX, Tz, '*')
plt.title('Variazione di Tz')
plt.xlabel('iterazione')
plt.ylabel('Tz (Nm)')
plt.savefig('output/Tz.png')
plt.close()

#plot all forces
plt.plot(timeX, Fx, '*')
plt.plot(timeX, Fy, '*')
plt.plot(timeX, Fz, '*')
plt.legend(['Fx', 'Fy', 'Fz'], loc='upper right')
plt.title('Variazione delle forze')
plt.xlabel('iterazione')
plt.ylabel('F (N)')
plt.savefig('output/F.png')
plt.close()

#plot all torques
plt.plot(timeX, Tx, '*')
plt.plot(timeX, Ty, '*')
plt.plot(timeX, Tz, '*')
plt.legend(['Tx', 'Ty', 'Tz'], loc='upper right')
plt.title('Variazione delle coppie')
plt.xlabel('iterazione')
plt.ylabel('T (Nm)')
plt.savefig('output/T.png')
plt.close()
