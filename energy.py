import density, energy, kappa, luminosity, mass, mu, opacity, pressure, temperature

energy = None

def get():
    global energy
    e_pp = 1.07E-7 * density.get()/1E5 *mu.get_X()**2 * (temperature.get()/1E6)**4
    e_CNO = 8.24E-26 * density.get()/1E5 * 0.03 * mu.get_X()**2 * (temperature.get()/1E6)**19.9
    e_3alpha = 3.85E-8 * (density.get()/1E5)**2*mu.get_Y()**3*(temperature.get()/1E8)**44
    return e_pp + e_CNO# + e_3alpha