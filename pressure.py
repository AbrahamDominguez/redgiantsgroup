import const
from RK4 import RK4
import density, energy, kappa, luminosity, mass, mu, opacity, pressure, temperature

v_y = []

def get_P():
    return (3.0*const.pi**2)**(2.0/3.0)*(const.hbar**2)/(5.0*const.me)*(density.get()/const.mp)**(5.0/3.0)\
           + density.get()*const.kb*temperature.get()/(mu.get_mu()*const.mp) \
           + (1.0/3.0)*(temperature.get()**4)*const.a

def dP_T(rho, T):
    return rho*const.kb/(mu.get_mu()*const.mp)\
           + 4.0/3.0*(T**3 * const.a)

def dP_rho(rho, T):
    return (3.0*const.pi**2)**(2.0/3.0)*(const.hbar**2)/(3.0*const.me)*(rho)**(2.0/3.0)*(1.0/const.mp)**(5.0/3.0)\
           + const.kb*T/(mu.get_mu()*const.mp)

def iterate():
    v_y.append(get_P())

def get_dP_T():
    return dP_T(density.get(), temperature.get())

def get_dP_rho():
    return dP_rho(density.get(), temperature.get())