X = 0.70
Y = 0.28
Z = 0.02

mu = 1.0/(2.0*X + 0.75*Y + 0.5*Z)

def iterate():
    global mu, X, Y, Z
    mu = 1.0/(2.0*X + 0.75*Y + 0.5*Z)

def get_mu():
    return mu

def get_X():
    return X

def get_Y():
    return Y

def get_Z():
    return Z