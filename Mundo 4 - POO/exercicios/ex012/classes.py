from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome:str = ""):
        self.nome = nome

    @abstractmethod
    def emitir_som(self):
        print(f"{self.nome} é {self.__class__.__name__} e está emitindo um som")

class Pato(Animal):
    pass

    def emitir_som(self):
        print(f"{self.nome} acabou de dizer 'QUACK! QUACK!'")

class Cachorro(Animal):
    pass

    def emitir_som(self):
        print(f"{self.nome} acabou de dizer 'AU! AU! AU!'")

class Akita(Cachorro):
    pass

    def emitir_som(self):
        print(f"{self.nome} acabou de dizer 'RUF! RUF! RUF!'")

class ViraLata(Cachorro):
    pass

    def emitir_som(self):
        print(f"{self.nome} acabou de dizer 'au! au!'")

class Gato(Animal):
    pass

    def emitir_som(self):
        print(f"{self.nome} acabou de dizer 'MIAU! MIAU!'")

class Galinha(Animal):
    pass

    def emitir_som(self):
        print(f"{self.nome} acabou de dizer 'PÓ! PÓ! PÓ!'")