import const
import inspect

class RK4:
   

    def updateK(self):
        self.k1 = self.f(self.t, self.y)
        self.k2 = self.f(self.t + const.step/2.0, self.y + const.step/2.0*self.k1)
        self.k3 = self.f(self.t + const.step/2.0, self.y + const.step/2.0*self.k2)
        self.k4 = self.f(self.t + const.step, self.y + const.step*self.k3)

    def __init__(self, func_derivative, initial_value, initial_t = 0):
        if not callable(func_derivative):
            raise RuntimeError("func_derivative is not a function")
        else:
            l = len(inspect.getargspec(func_derivative)[0])
            if l != 2:
                raise RuntimeError("func_derivative should have only 2 parameters, not " + str(l))

        self.t = initial_t
        self.f = func_derivative
        self.y = initial_value

        self.v_t = []
        self.v_y = []

        
    def init(self):
        self.updateK();  

    def iterate(self):
        #print("first: " + str(self.y) + " ~ " + str(const.step/6.0*(self.k1 + 2.0*self.k2 + 2.0*self.k3 + self.k4)))
        self.y += const.step/6.0*(self.k1 + 2.0*self.k2 + 2.0*self.k3 + self.k4)
        #print("second: " + str(self.y))
        #print("first: " + str(self.t) + " ~ " + str(const.step))
        self.t += const.step
        #print("second: " + str(self.t) + " ~ " + str(const.step))
        self.v_t.append(self.t)
        self.v_y.append(self.y)
        self.updateK()

    def get(self):
        return self.y
