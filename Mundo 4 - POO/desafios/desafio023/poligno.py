from math import pi
from abc import ABC, abstractmethod


class Poligno(ABC):
    def __init__(self, lados):
        self.qtd_lados = lados

    @abstractmethod
    def perimetro(self) -> float: # no -> estou dizendo retorne float
        pass

    @abstractmethod
    def area(self) -> float:
        pass

class Quadrado(Poligno):
    def __init__(self, lado = 1):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return self.lado * 4

    def area(self):
        return self.lado ** 2

class Circulo(Poligno):
    def __init__(self, raio = 1):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return (2 * pi) * self.raio

    def area(self):
        return pi * (self.raio ** 2)