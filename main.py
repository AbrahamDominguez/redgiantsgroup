#this is where we loop and iterate all the values and graph

import matplotlib.pyplot as plt
from numpy import array, log10
import const
import density, energy, kappa, luminosity, mass, mu, opacity, pressure, temperature

mass.init()
luminosity.init()
density.init()
temperature.init()
opacity.init()

loops = 0
#for i in xrange(loops):
try:
    while(True):
        loops += 1
        mass.iterate()
        luminosity.iterate()
        pressure.iterate()
        density.iterate()
        temperature.iterate()
        opacity.iterate()
        kappa.iterate()
        #print kappa.get()
        #print(luminosity.get())
        print( temperature.get())
        #print(temperature.dT_dr_conv(temperature.rk4.t,temperature.get()), temperature.dT_dr_rad(temperature.rk4.t,temperature.get()))
        #print(loops, temperature.get(), temperature.dT_dr_conv(temperature.rk4.t,temperature.get()), temperature.dT_dr_rad(temperature.rk4.t,temperature.get()),temperature.rk4.t/const.Rsun )
        if temperature.get() < const.step/6.0:
            break
        #print(i, temperature.get(), kappa.get())
except:
    pass

T_max = max(temperature.rk4.v_y)
L_max = max(luminosity.Solver.v_y)
M_max = max(mass.rk4_mass.v_y)
Rho_max = max(density.rk4.v_y)
P_max = max(pressure.v_y)
for i in xrange(loops):
    temperature.rk4.v_y[i] /= T_max
    luminosity.Solver.v_y[i] /= L_max
    mass.rk4_mass.v_y[i] /= M_max
    density.rk4.v_y[i] /= Rho_max
    #pressure.v_y /= P_max

#plt.plot(opacity.solver.v_t, opacity.solver.v_y)
#plt.show()


#plt.plot(density.rk4.v_t, kappa.v_y)
#import math
#for i in xrange(loops):
#    kappa.v_y[i] = math.log10(kappa.v_y[i])
#plt.plot(density.rk4.v_t, kappa.v_y)
#plt.show()

plt.plot(array(temperature.rk4.v_t)/const.Rstar, temperature.rk4.v_y)
plt.plot(array(luminosity.Solver.v_t)/const.Rstar, luminosity.Solver.v_y)
plt.plot(array(mass.rk4_mass.v_t)/const.Rstar, mass.rk4_mass.v_y)
plt.plot(array(density.rk4.v_t)/const.Rstar, density.rk4.v_y)
plt.show()

plt.plot(density.rk4.v_t, pressure.v_y)
plt.show()
