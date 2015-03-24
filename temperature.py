from RK4 import RK4
import const
import density, energy, kappa, luminosity, mass, mu, opacity, pressure, temperature

def dT_dr_conv(r, T):
    return ((1.0-1.0/const.gamma)*(T/pressure.get_P())*(const.G*mass.get()*density.get())/(r**2))

def dT_dr_rad(r, T):
    return (3.0*kappa.get()*density.get()*luminosity.get()/(16*const.a*const.c*(T**3.0)*const.pi*(r**2.0)))

def dT_dr(r, T):
    conv = dT_dr_conv(r,T)
    rad = dT_dr_rad(r,T)
    print rad, conv
    if rad < conv:
        print "rad"
    #else:
       # print "conv"
    return -min(abs(conv), abs(rad))

rk4 = RK4(dT_dr, const.T_0, 1E-10)

def init():
    rk4.init()

def iterate():
    rk4.iterate()

def get():
    return rk4.get()