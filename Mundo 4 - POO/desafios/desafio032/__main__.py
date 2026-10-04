from desafio032 import *

def main():
    cc = ContaBancaria(112, "Pedro", 3000)
    print(f"Vou tentar sacer...")
    cc.sacar(500)
    print(f"Tentando mudar o nome...")
    cc.nome = "Ramos Ritter"
    print(cc)

if __name__ == "__main__":
    main()