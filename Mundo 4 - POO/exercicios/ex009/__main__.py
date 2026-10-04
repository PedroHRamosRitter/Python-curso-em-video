from ex009 import *
from rich import print, inspect

def main():
    av1 = Avaliacao("Pedro", "Matemática")
    av1.set_nota(10)
    print(f"{av1.nome} tirou {av1.get_nota()} em {av1.disciplina}")
    inspect(av1, private=True ,methods=True) # private -> mostrar os dados privados, no caso nota

if __name__ == "__main__":
    main()