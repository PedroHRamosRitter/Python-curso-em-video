from classes import Aluno, Professor, Funcionario
from rich import inspect

def main():
    a1 = Aluno("Pedro", 18, "ADS", "3ADS")
    a1.fazer_aniversario()
    a1.fazer_matricula()
    #inspect(a1, methods=True)

    p1 = Professor("Francisco", 68, "Matemática", "Mestrado")
    p1.fazer_aniversario()
    p1.dar_aula()
    #inspect(p1, methods=True)

    f1 = Funcionario("Carlos", 30, "DevOps", "Desenvolvedor")
    f1.fazer_aniversario()
    f1.bater_ponto()
    #inspect(f1, methods=True)

    # x = Pessoa("Gustavo", 49)
    # x.fazer_aniversario()
    # inspect(x, methods=True)

    a1.estudar()
    p1.estudar()
    f1.estudar()


if __name__ == "__main__":
    main()