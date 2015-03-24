"""
+-------------------------------------------------+
|LUMINOSITY HELPER FUNCTION PHYS 375 FINAL PROJECT|
+-------------------------------------------------+
|James Lambert                                    |
|Last Modified:  March 14, 2015                   |
+-------------------------------------------------+ 
"""
####################################################################
#NECESSARY IMPORTS#
import numpy as np
from RK4 import RK4
import const
import density, energy, kappa, luminosity, mass, mu, opacity, pressure, temperature
####################################################################



def lumDeriv( r, L ):
    """
    Function which defines the derivative of luminosity with respect to position
    in terms of the density, rho and epsilon (energy constant) and radius, r
    """
    return 4.0*const.pi*((r)**(2.0))*density.get()*energy.get()

Solver = RK4( lumDeriv, const.L_0 )

def init():
    global Solver
    Solver.init()

def iterate():
    Solver.iterate()

def get():
    return Solver.get()