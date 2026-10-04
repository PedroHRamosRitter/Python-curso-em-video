from rich import print, inspect

class Pessoa: #Superclasse
    def __init__(self, nome = "", idade = 0): # Metódo Construtor
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade +=1


class Aluno(Pessoa): # Subclasse de Pessoa
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"{self.nome}, acabou de fazer a matrícula")


class Professor(Pessoa): # Subclasse de Pessoa
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"Prof. {self.nome} começou a dar aula")


class Funcionario(Pessoa): # Subclasse de Pessoa
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f"{self.nome} acaboou de bater ponto")

a1 = Aluno("Pedro", 18, "ADS", "3ADS")
a1.fazer_aniversario()
a1.fazer_matricula()
inspect(a1, methods=True)
p1 = Professor("Francisco", 68, "Matemática", "Mestrado")
p1.dar_aula()
inspect(p1, methods=True)
f1 = Funcionario("Carlos", 30, "DevOps", "Desenvolvedor")
f1.bater_ponto()
inspect(f1, methods=True)