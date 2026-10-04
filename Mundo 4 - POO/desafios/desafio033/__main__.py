from desafio033 import *
from rich import print, inspect

def main():
    a = Aluno("Pedro", 2008, "ADS")
    a.nascimento = 2024
    a.add_curso("INFO")


    # inspect(a, private=True, methods=True)
if __name__ == "__main__":
    main()