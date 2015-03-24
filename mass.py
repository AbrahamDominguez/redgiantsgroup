from RK4 import RK4
import const
import density, energy, kappa, luminosity, mass, mu, opacity, pressure, temperature

def dM_dr(r, M):
    return 4.0*const.pi*(r**(2.0))*density.get()

rk4_mass = RK4(dM_dr, const.dM_0)

def init():
    global rk4_mass
    rk4_mass.init()

def iterate():
    rk4_mass.iterate()

def get():
    return rk4_mass.get()
