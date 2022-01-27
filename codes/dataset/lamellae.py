import hoomd
from hoomd import md
from hoomd import deprecated
import math
import numpy as np
import os.path
import sys
import time

hoomd.context.initialize()

system = deprecated.init.read_xml(filename="startConfig.xml")

#***** Force Field Setup *****#
harmonic = md.bond.harmonic()
harmonic.bond_coeff.set('polymer', k=4.0, r0=0.0) #Sets harmonic bond parameter with C = 4

nl = md.nlist.cell()
nl.reset_exclusions(exclusions=None)

#NOTE - manually check these all before running
aii = 25
aAB=3.0
aAC=2.0
aBC = 3.5

dpd = md.pair.dpd(r_cut=1.0,nlist=nl,kT=1.0,seed=24) #Can convert these to chi
dpd.pair_coeff.set('A', 'A', A=aii, gamma=4.5)
dpd.pair_coeff.set('B', 'B', A=aii, gamma=4.5)
dpd.pair_coeff.set('C', 'C', A=aii, gamma=4.5)

dpd.pair_coeff.set('A', 'B', A=aii+aAB, gamma=4.5)
dpd.pair_coeff.set('A', 'C', A=aii+aAC, gamma=4.5)
dpd.pair_coeff.set('B', 'C', A=aii+aBC, gamma=4.5)

# Start logging (every step)
logger = hoomd.analyze.log(filename=filename+".log", period=5000, phase=0,
        quantities=['time','potential_energy','bond_harmonic_energy','temperature','pressure', 'pressure_xx', 'pressure_xy', 'pressure_xz', 'pressure_yy', 'pressure_yz', 'pressure_zz','lx','lz'], header_prefix='#', overwrite=False)

#dump every 500k/200k steps
xml = deprecated.dump.xml(group=hoomd.group.all(), filename=filename+".xml", vis=True, velocity = True, restart=True, period=500000, phase=0)
hoomd.dump.dcd(filename=filename+".dcd", period=100000, phase=0)

# integrate NPT for a bunch of time steps
md.integrate.mode_standard(dt=0.01)
md.integrate.npt(group=hoomd.group.all(),kT=temperature,tau=1.0,P=20.0914,tauP=1.0,couple="xy")

hoomd.run(5e6)

xml.write_restart()

xml.write(filename="start_" + filename + ".xml", time_step=0)
#xml.write(filename="shear_start_" + filename + ".xml")
