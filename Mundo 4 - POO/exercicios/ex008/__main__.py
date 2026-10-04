from ex008 import *

def main():
    c1 = ContaBancaria(112, "Pedro", 3000)
    c1.depositar(500)
    c1.sacar(2_000)
    c1.saldo = 0
    print(c1)

if __name__ == "__main__":
    main()