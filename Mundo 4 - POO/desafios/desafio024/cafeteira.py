from abc import ABC, abstractmethod


class BebidaQuente(ABC):

    def preparar(self): # metódo concreto -> são iguais para todos
        print(f"--- Iniciando o Preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print(f"Bebida pronta\n")


    def ferver_agua(self): # metódo concreto
        print(f"1. Fervendo água a 100 graus celsius.")

    @abstractmethod

    def misturar(self):
        pass

    def servir(self):
        pass



class Cafe(BebidaQuente):
    def misturar(self):
        print(f"2. Passando água pressurizada pelo pó de café moído.")

    def servir(self):
        print(f"3. Servindo em xícara pequena.")


class Cha(BebidaQuente):
    def misturar(self):
        print(f"2. Mergulhando o sachê de ervas na água.")

    def servir(self):
        print(f"3. Servindo na caneca de porcelane com limão")


class Leite(BebidaQuente):
    def misturar(self):
        print(f"2. Passando vapor pressurizada pelo bico do leite.")

    def servir(self):
        print(f"3. Servindo na caneca grande, já com café.")
