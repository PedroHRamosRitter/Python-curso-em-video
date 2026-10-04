class Carteira:

    def __init__(self, valor:int|float = 0):
        self.__saldo = valor

    def __str__(self):
        return f"Você tem R${self.saldo:,.2f}"

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        raise PermissionError(f"Você não tem auterização para alterar o saldo desse jeito")

    def __eq__(self, outro): # Sobreescrevendo o ==
        if self.__saldo == outro.__saldo:
            return True
        else:
            return False

    def __iadd__(self, valor: int|float): # sobreescrevendo o +=
        self.__saldo = self.__saldo + valor
        return self

    def __isub__(self, valor: int|float): # sobreescrenvdo o -=
        self.__saldo = self.__saldo - valor
        return self

    def __le__(self, outro):
        if self.__saldo <= outro.__saldo:
            return True
        else:
            return False
