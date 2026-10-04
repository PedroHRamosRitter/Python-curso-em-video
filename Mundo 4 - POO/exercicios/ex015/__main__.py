from classes import *

def main():
    c1 = Carteira(1020)
    c2 = Carteira(140)

    c1 += 50
    c1 -= 10

    if (c1 == c2):
        print(f"Vocês tem o mesmo valor na carteira")
    else:
        print(f"As carteiras tem valores diferentes")

    if (c1 <= c2):
        print(f"A segunda carteira tem mais dinheiro")
    else:
        print(f"A primeira carteira tem mais dinheiro")

    print(c1)
    print(c2)

if __name__ == "__main__":
    main()