#!/usr/bin/env python
# coding: utf-8

import numpy as np
from pint import UnitRegistry
ureg = UnitRegistry()


# This script convert the LJ parameters from the Grivet 2005 (NMR relaxation parameters of a Lennard-Jones fluid from molecular-dynamics simulations) paper into the real units system of LAMMPS

# From Grivet 2005
# 
# $\rho^* = 0.84$
# 
# $T^* \in [0.8, 3.0]$
# 
# $N_{part} = 16384$

T_star = 3.2

sigma = 3 * ureg.angstrom # A
epsilon = 0.1 * ureg.kcal / ureg.mol # kcal/mol
mass = 1.0 * ureg.g / ureg.mol # g/mol
kB = 1.987204259e-3 * ureg.kcal / ureg.mol / ureg.K # kcal/mol/K

# $t_{conv} = \sqrt{\epsilon / m \sigma^2}$
# 
# $d_{conv} = \sigma$
# 
# $T_{conv} = \epsilon / k_B$

tconv = np.sqrt(mass*sigma**2/epsilon)
dconv = sigma
tempconv = epsilon/kB
print("tvonc = "+str(tconv.to(ureg.femtos)))
print("dconv = "+str(dconv))
print("tempconv = "+str(tempconv))


# $\omega_0 =  0.07 \times 2 \pi$ [no unit]

omega0 = 2*np.pi*0.07 # no unit
f0 = 0.07 # no unit
f0 /= tconv
t0 = 1/f0
t0 = t0.to(ureg.fs)
dt = tconv*0.0025
dt = dt.to(ureg.fs)
n_step = 20000 # 4*np.int32(t0/dt) # factor 4 for safety

print("f_0 = "+str(f0.to(ureg.MHz)))
print("t_0 = "+str(t0.to(ureg.ps)))
print("dt = "+str(dt.to(ureg.fs)))
print("N_0 = "+str(n_step))

rho_star = 0.84
rho = rho_star * mass / sigma**3
print("rho = "+str(rho))
n_part = 1638
L = (n_part / (rho / mass))**(1/3)
print("L = "+str(L))
cut_off = 3.0*sigma

T = tempconv * T_star
print("temperature = "+str(T))

f = open("parameters.lammps", "w")
f.write("# LAMMPS parameters \n")
f.write("variable mass equal " + str(mass.magnitude) + " # " + str(mass.units) + "\n")
f.write("variable sigma equal " + str(sigma.magnitude) + " # " + str(sigma.units) + "\n")
f.write("variable epsilon equal " + str(epsilon.magnitude) + " # " + str(epsilon.units) + "\n")
f.write("variable dt equal " + str(dt.magnitude) + " # " + str(dt.units) + "\n")
f.write("variable n_step equal " + str(n_step) + "\n")
f.write("variable n_part equal " + str(n_part) + "\n")
f.write("variable L equal " + str(L.magnitude)  + " # " + str(L.units) + "\n")
f.write("variable cut_off equal " + str(cut_off.magnitude)  + " # " + str(cut_off.units) + "\n")
f.write("variable T equal " + str(T.magnitude)  + " # " + str(T.units) + "\n")
f.close()

