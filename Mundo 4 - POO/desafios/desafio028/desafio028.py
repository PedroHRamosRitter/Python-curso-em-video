class Termostato:
    def __init__(self):
        self.__temperatura = 24

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 != 0:
            raise ValueError(f"Temperatura de {valor} é inválida")
        if 16 <= valor <= 30:
            self.__temperatura = valor
        elif valor <= 15:
            self.__temperatura = 16
        else:
            self.__temperatura = 30

    @property
    def ftemperatura(self):
        return f"{self.__temperatura}ºC"
        # return f"{self.__temperatura}{chr(176)}C"


