#numerical constants

Msun = 1.989*10**(30)  #Mass of Sun
Rsun = 6.958*10**8     #Radius of sun
Lsun = 3.846*10**(26)  #Luminostity of the sun
Tsun = 5.778*10**3     #Temperature at the surface of the sun
kb = 1.3806488E-23 #Boltzmann Constant
sigma_B = 5.670373E-8
me = 9.10938291E-31 #mass of expectron kg
mp = 1.67262178E-27 #mass of proton kg
u = 1.66053873E-27 #kg
m_H = (1.00794*u) #mass of hydrogen kg
eV = 1.60217657E-19 #joules
h = 6.62606957E-34
G = 6.67384E-11 #Gravitational Constant
hbar = 1.054571596E-34
pi = 3.141592654
c = 299792458.0
q_e = 1.602176462E-19
H_0 = (70.0*1000.0/3.08567758E22)
GYR = (365.25*24.0*60.0*60.0*1E9)
AU = 149597870700.0 #meters
pc = (206264.81 * AU)
a = 4.0*sigma_B/c

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
kappa_0 = 1 # For now anyway
dtau_0 = kappa_0*rho_0

gamma = 5.0/3.0

#Surface Boundary Conditions
tau_out = 2.0/3.0 #This is the opacity at the outside of the star, 
              #comes from tau(infinity) - tau(Radius of star)

# Sample Values at suface from section 3
Tstar = 3.056*10**3
Rstar = 0.865*Rsun
Mstar = 0.673*Msun
Lstar = (5.86*10**(-2))*Lsun

#steping interval
step = 0.001
