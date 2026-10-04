from desafio030 import *
from rich import print, inspect

def main():
    c = Credencial()
    c.senha = str(input(f"Digite a sua senha: "))
    print(c.senha)
    c.validar("Pedro@!")

if __name__ == "__main__":
    main()