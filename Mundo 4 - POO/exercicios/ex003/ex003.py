class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criado com sucesso. Saldo atual de R${self.saldo:,.2f}")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self.id}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"\033[1;31mSaque NEGADO de R${valor:,.2f} não conta {self.id}: SALDO INSUFICIENTE\033[m")
        else:
            self.saldo -= valor
            print(f"\033[1;32mSaque de R${valor:,.2f} autorizado na conta {self.id}[m")


c1 = ContaBancaria(112, "Pedro", 3000)
c1.depositar(500)
c1.sacar(2_000_000)
print(c1)

c2 = ContaBancaria(123, "Maria", 10)
c2.depositar(1200)
c2.sacar(100)
print(c2)
