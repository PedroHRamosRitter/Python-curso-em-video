import cafeteira
# from cafetaria import *


def main():
    b1 = cafeteira.Cafe()
    b2 = cafeteira.Cha()
    b3 = cafeteira.Leite()

    b1.preparar()
    b2.preparar()
    b3.preparar()

if __name__ == "__main__":
    main()