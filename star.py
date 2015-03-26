import density, luminosity, mass, mu, const, energy, density, kappa, pressure, temperature

mass.init()
luminosity.init()
density.init()
temperature.init()
opacity.init()

class star:
    def __init__ (self, rho_c, T_c, X, Y, Z): #use mu.get_{X,Y,Z}() for X Y Z
        self.rho_c = rho_c
        self.T_c = T_c
        self.X = X
        self.Y = Y
        self.Z = Z