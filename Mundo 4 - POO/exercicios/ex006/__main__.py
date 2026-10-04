from rich import print, inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():
    a1 = Aluno("Pedro", 18, "ADS", "3ADS")
    a1.fazer_matricula()
    a1.fazer_aniversario()
    # inspect(a1, methods=True)

    p1 = Professor("Francisco", 68, "Matemática", "Mestrado")
    p1.dar_aula()
    p1.fazer_aniversario()
    # inspect(p1, methods=True)

    f1 = Funcionario("Carlos", 30, "DevOps", "Desenvolvedor")
    f1.bater_ponto()
    f1.fazer_aniversario()
    # inspect(f1, methods=True)

if __name__ == "__main__":
    main()
