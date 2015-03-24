
import density, energy, kappa, luminosity, mass, mu, opacity, pressure, temperature
v_y = []

def get():
    #return (1.0/(2.5E-32*(mu.get_Z()/0.02)*density.get()**0.5*temperature.get()**9)\
 #+ 1.0/max(0.02*(1.0+mu.get_X()),(3.68E22*(1-mu.get_Z())*(1+mu.get_X())*(density.get()*1000)*(temperature.get()**-3.5))/10))**(-1.0)
    return (1.0/(2.5E-32*(mu.get_Z()/0.02)*((density.get()/(10**3.0))**(0.5))*(temperature.get())**(9))\
            + 1.0/max(0.02*(1.0+mu.get_X()),\
                      1.0E24*(mu.get_Z()+0.0001)*(1+mu.get_X())*((density.get()/(10**3.0))**(0.7))*(temperature.get()**(-3.5))))**(-1.0)
def iterate():
    v_y.append(get())
