from sympy import symbols
from sympy import symbol # https://github.com/sympy/sympy/blob/master/sympy/core/symbol.py
from sympy import I


class Nodo:
    def __init__(self, name: str):
        self.name = name

class Orientation:
    def __init__(self, name: str):
        self.name = "positive"

class BasicComponent:
    def __init__(
        self,
        name: str, 
        nodo1: Nodo, 
        nodo2: Nodo, 
        value : Optional[float] = None, # If is Float can be int, here why: https://www.python.org/dev/peps/pep-0484/#the-numeric-tower
        orientation : Optional[Orientation] = None
        ):
            self.name : Symbol = symbols(name, positive=True) 
            self.nodo1 = nodo1 
            self.nodo2 = nodo2
            if (value is not None):
                if (value > 0):
                    self.value = value
                else:
                    raise ValueError("Sorry, value have to be greater than 0")
                    # ¿qué ocurre con selfValue si no lo defino en el init? es none? daría error? confuso.
            self.orientation = orientation

class PassiveComponent(BasicComponent):
    self.orientation = None
    w = symbols('w', positive=True) # it's omega.

class Inductor(PassiveComponent):
    self.Z = I * w * self.name

class Capacitor(PassiveComponent):
    self.Z = -I * (1 / w * self.name)

class Resistor(PassiveComponent):
    self.Z = self.name