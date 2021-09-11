from __future__ import annotations
# The error from Mypy to sympy library can be fixed in the future, here the error in github: https://github.com/sympy/sympy/pull/18244
from sympy import symbols # type: ignore
from sympy import Symbol # https://github.com/sympy/sympy/blob/master/sympy/core/symbol.py
from sympy import I
from typing import Optional, List, NoReturn

class Nodo:
    def __init__(self, name: str, elements: List[BasicComponent]):
        self.name = name
        self.elements : List[BasicComponent] = []

    def addElement (self, component : BasicComponent):
        self.elements.append(component)

class Orientation:
    def __init__(self, name: bool):
        self.value = name

class Ground:
    def __init (self, nodo : Nodo):
        self.nodo = nodo

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
                elif (value <= 0):
                    self.doable = False
                else:
                    raise ValueError("Sorry, the value have to be a number")
            self.orientation = orientation

class VoltageSource(BasicComponent):
    def __init__(
        self,
        name: str, 
        nodo1: Nodo, 
        nodo2: Nodo, 
        value: Optional[float] = None, # If is Float can be int, here why: https://www.python.org/dev/peps/pep-0484/#the-numeric-tower
        orientation : Orientation
        ):
            super().__init__(name, nodo1, nodo2, value, orientation)

class CurrentSource(BasicComponent):
    def __init__(
        self,
        name: str, 
        nodo1: Nodo, 
        nodo2: Nodo, 
        value: Optional[float] = None, # If is Float can be int, here why: https://www.python.org/dev/peps/pep-0484/#the-numeric-tower
        orientation : Optional[Orientation] = None
        ):
            super().__init__(name, nodo1, nodo2, value, orientation)
            self.orientation = None

class PassiveComponent(BasicComponent):
    def __init__(
        self,
        name: str, 
        nodo1: Nodo, 
        nodo2: Nodo, 
        value : Optional[float] = None, # If is Float can be int, here why: https://www.python.org/dev/peps/pep-0484/#the-numeric-tower
        orientation : Optional[Orientation] = None
        ):
            super().__init__(name, nodo1, nodo2, value)
            self.orientation = None
            self.s = symbols('s', positive=True) 
    
class Inductor(PassiveComponent):
    def __init__(        
        self,
        name: str, 
        nodo1: Nodo, 
        nodo2: Nodo, 
        value : Optional[float] = None, # If is Float can be int, here why: https://www.python.org/dev/peps/pep-0484/#the-numeric-tower
        orientation : Optional[Orientation] = None
        ):
            super().__init__(name, nodo1, nodo2, value)
            self.Z = I * self.s * self.name

class Capacitor(PassiveComponent):
    def __init__(        
    self,
    name: str, 
    nodo1: Nodo, 
    nodo2: Nodo, 
    value : Optional[float] = None, # If is Float can be int, here why: https://www.python.org/dev/peps/pep-0484/#the-numeric-tower
    orientation : Optional[Orientation] = None
    ):
        super().__init__(name, nodo1, nodo2, value)
        self.Z = -I * (1 / self.s * self.name)

class Resistor(PassiveComponent):
    def __init__(        
    self,
    name: str, 
    nodo1: Nodo, 
    nodo2: Nodo, 
    value : Optional[float] = None, # If is Float can be int, here why: https://www.python.org/dev/peps/pep-0484/#the-numeric-tower
    orientation : Optional[Orientation] = None
    ):
        super().__init__(name, nodo1, nodo2, value)
        self.Z = self.name