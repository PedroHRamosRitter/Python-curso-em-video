from desafio029 import *
from rich import print, inspect

def main():
    d = Diario("abc")
    d.escrever(f"Olá tudo bem?")
    d.escrever(f"Meu nome é Pedro")
    try:
        d.ler(f"abc")
    except Exception as e:
        print(f"[red]Erro: {e}")


if __name__ == "__main__":
    main()