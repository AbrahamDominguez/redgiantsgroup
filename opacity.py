import const
from RK4 import RK4
import density, energy, kappa, luminosity, mass, mu, opacity, pressure, temperature

def f(radius, opacity):
    return kappa.get() * density.get()

solver = RK4(f, const.tau_0) 

def init():
    global solver
    solver.init() 

def iterate():
    solver.iterate()

def get():
    """
    Uses the Runge-Kutta 4 method to integrate the optical depth Tau of a star
    that obeys the differential equation tau_dot = kappa * rho where rho is the 
    density of the star at a specified radius and kappa is the opacity at a specified
    radius. 
    
    All paramaters except dr are 1d arrays.
    """
    return solver.get()
