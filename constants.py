#numerical constants

kb = 1.38*10**(-23)    #Boltzmann Constant
mp = 1.672*10**(-27)   #mass of proton
G = 6.627*10**(-11)    #Gravitational Constant
Msun = 1.989*10**(30)  #Mass of Sun
Rsun = 6.958*10**8     #Radius of sun
Lsun = 3.846*10**(26)  #Luminostity of the sun
Tsun = 5.778*10**3     #Temperature at the surface of the sun

#Initial conditions
M_0 = 0 
dM_0 = 0
L_0 = 0
dL_0 = 0
rho_0 = 5.856*10**4 #rho_c from section 3
drho_0 = 0
T_0 = 8.23*10**6 #T_c from section 3
dT_0 = 0
tau_0 = 0
####  dtau_0 = kappa*rho_c is insert here####

#Surface Boundary Conditions
tau_out = 2/3 #This is the opacity at the outside of the star, 
              #comes from tau(infinity) - tau(Radius of star)

# Sample Values at suface from section 3
Tstar = 3.056*10**3
Rstar = 0.865*Rsun
Mstar = 0.673*Msun
Lstar = (5.86*10**(-2))*Lsun

#steping interval
step = 0.001
