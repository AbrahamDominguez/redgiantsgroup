# -*- coding: utf-8 -*-
import const
import integrate # NOT YET A THING :(


rho = const.rho_0
T = const.T_0

def shot(rho, T, M_0, L_0, *args):
    err_bound = 1e20
    #integrate the star up to surface radius
    L_star, T_star, R_star = integrate.integrate(rho, T)
    
    #Compare luminosities to Stefan Boltzmann law to check continuity
    sb_luminosity = 4 * const.pi * (R_star ** 2) * (T_star ** 4)
    
    ticker = 0      # if this gets to 10 000 we stop....   
    
    while ticker <= 10000:
        if L_star < sb_luminosity:
            if abs(L_star - sb_luminosity) <= err_bound:
                return L_star, T_star, R_star
            else:
                rho += 10.0
            
        elif L_star > sb_luminosity:
            if abs(L_star - sb_luminosity) <= err_bound:
                return L_star, T_star, R_star
            else:
                rho -= 10.0
        ticker += 1
    return 'FUCK'   #Returned if we dont get a solution after 10 000 iterations....