from abc import ABC, abstractmethod
from rich.panel import Panel
from rich import print

class Funcionario(ABC):
    sal_min = 1_621
    inss = 7.5
    def __init__(self, nome = None):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0

    @abstractmethod

    def calc_sal(self):
        pass

    def analisar_sal(self):
        base = self.salario / Funcionario.sal_min
        mensagem = f"O salário de [blue]{self.nome}[/] ({self.__class__.__name__}) é de R${self.salario:.2f} e corresponde a [yellow]{base:.2f}[/] salários mínimos."
        painel = Panel(mensagem, title="Análise de salário", width=50)
        print(painel)


class Horista(Funcionario):
    def __init__(self, nome, valor_hora = 7.37, horas_trab = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trab
        self.sal_bruto = self.valor_hora * self.horas_trabalhadas

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100)

        return self.salario

class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto = Funcionario.sal_min):
        super().__init__(nome)
        self.sal_bruto = sal_bruto



    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100)

        return self.salario