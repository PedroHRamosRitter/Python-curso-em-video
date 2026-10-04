# Declaração de Classe
class Gafanhoto:
    """
    Essa classe cria um gafanhoto, que é uma pessoa que tem nome e idade.
    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome, idade)

    """

    def __init__(self, nome = "vazio", idade = 0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def __str__(self): # Dunder Method
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade."

    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"

# Funções
def lin():
    print(f'-=' * 30)

# Declaração de Objetos
n1 = Gafanhoto("Pedro", 18)
n1.aniversario()
# print(n1)
lin()

print(n1.__dict__) # Exibição em dicionário -> Attribute -> No final não tem ()
print(n1.__getstate__()) # Exibição em dicionário -> Method -> No final tem () -> Pode ser personalizado usando def (funções)
print(n1.__class__)


# n2 = Gafanhoto("Maria", 16)
# print(n2)
# print(n2.__getstate__())
# print(n1.__doc__) # Dunder Attribute