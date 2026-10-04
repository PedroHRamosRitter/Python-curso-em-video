from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod

    def calc_frete(self):
        pass

class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)


    def calc_frete(self):
        self.frete = self.distancia * Moto.fator
        return f"R${self.frete:.2f}"

class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)


    def calc_frete(self):
        self.frete = self.distancia * Caminhao.fator
        if self.distancia >= 50:
            return f"R${self.frete:.2f}"
        else:
            self.frete = 0
            return f"Raio mínimo de 50 Km"


class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)


    def calc_frete(self):
        self.frete = self.distancia * Drone.fator
        if self.distancia <= 10:
            return f"R${self.frete:.2f}"
        else:
            self.frete = 0
            return f"O máximo é 10 Km"


