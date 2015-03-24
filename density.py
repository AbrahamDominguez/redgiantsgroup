from RK4 import RK4
import const
import density, energy, kappa, luminosity, mass, mu, opacity, pressure, temperature

def rho_dot(r,rho):
    return -(const.G*mass.get()*rho/r**2 + pressure.get_dP_T()*temperature.dT_dr(r, temperature.get()))/pressure.dP_rho(rho, temperature.get())

rk4 = RK4(rho_dot,const.rho_0, 1E-10)

def init():
    global rk4
    rk4.init()
 
def iterate():
    rk4.iterate()
    
def get():
    return rk4.get()