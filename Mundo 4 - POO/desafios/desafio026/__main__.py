from funcionario import *

def main():

    f1 = Horista("Pedro", 12, 200)
    f1.calc_sal()
    f1.analisar_sal()

    f2 = Mensalista("Pedro", 2500)
    f2.calc_sal()
    f2.analisar_sal()

if __name__ == "__main__":
    main()