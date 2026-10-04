from classesex005 import Aluno, Professor, Funcionario
from rich import inspect

a1 = Aluno("Pedro", 18, "ADS", "3ADS")
a1.fazer_aniversario()
p1 = Professor("Francisco", 68, "Matemática", "Mestrado")
p1.dar_aula()
f1 = Funcionario("Carlos", 30, "DevOps", "Desenvolvedor")
f1.bater_ponto()