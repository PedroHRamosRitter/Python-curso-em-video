from rich import print
from rich import inspect

# Declaração de classe
class Funcionario:
    # Atributos de Classe
    empresa = "Curso em Vídeo"

    def __init__(self, nome, setor, cargo):
        # Atributos de instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str: # estou dizendo com ->  que esta funcao retorna str(string)
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}." # Funcionario.empresa no lugar de self.__class__.empresa


Funcionario.empresa = "GOL"

c1 = Funcionario("Pedro", "TI", "Programador")
# c1.empresa = "Estudonauta"
# print(c1.empresa)
print(c1.apresentacao())
# inspect(c1, methods=True)

c2 = Funcionario("Maria", "Administração", "Diretora")
print(c2.apresentacao())
