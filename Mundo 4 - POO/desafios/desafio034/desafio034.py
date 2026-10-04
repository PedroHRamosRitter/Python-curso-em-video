from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario):
        self._nome = nome
        self.__salario = salario

    @abstractmethod
    def calcular_bonus(self):
        pass

    def __str__(self):
        return f"{self._nome} ganha R${self.__salario:,.2f} e por ser {__class__.__name__} o bônus será de R$"

class Gerente(Funcionario):
    pass

class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcular_bonus(self):




class Designer(Funcionario):
    pass