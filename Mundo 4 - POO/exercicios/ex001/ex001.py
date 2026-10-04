# self é um nome generico de um atriubtode instancia e todos os atributos de instancia vai ter self
# quando coloco def __init__(self) -> troca o self e coloca outro no caso n1
# self significa por assim dizer ele mesmo -> no caso n1.aniversario que e igual a Pedro.aniversaior e nome

# Declaração de Classe
class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atributosde Instância
        self.nome = ""
        self.idade = 0

    # Mtodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1
        #self.idade += 1

    def mensagem(self):
        return f"{self.nome} é gafanhoto e tem {self.idade} anos de idade."


# Declaração de Objetos
n1 = Gafanhoto()
n1.nome = "Pedro"
n1.idade = 18
print(n1.mensagem())
print(f'-=' * 30)
n1.aniversario()
print(n1.mensagem())
print(f'-=' * 30)
n2 = Gafanhoto()
n2.nome = "Maria"
n2.idade = 16
print(n2.mensagem())
print(f'-=' * 30)

g3 = Gafanhoto()
g3.aniversario()
print(g3.mensagem())
g