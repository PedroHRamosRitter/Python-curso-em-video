from desafio031 import *
from rich import print, inspect

def main():
    r = Retangulo(1, 5)
    try:
        r.base = 12
        r.altura = 33
        r.medidas = [3, 9]
    except Exception as e:
        print(F"Ocorreu um erro do tipo: {type(e).__name__}: {e}")

    print(f"{r.medidas}")


if __name__ == "__main__":
    main()