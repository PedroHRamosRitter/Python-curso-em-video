from desafio028 import *
from rich import  print, inspect

def main():
    t = Termostato()
    try:
        t.temperatura = 25.5
    except Exception as e:
        print(f"Hove um prolema: {e}")

    print(f"A temperatura atual é de {t.temperatura}")
if __name__ == "__main__":
    main()