from rich import print

class Diario:
    def __init__(self, senha = "pedro"):
        self.__senha = senha.strip()
        self.__segredos = []

    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
         self.__segredos.append(msg.strip())

    def ler(self, senha = None):
        if senha != self.__senha:
            raise PermissionError(f"Senha inválida! Você não pode ler meu diário!")
        else:
            print(f"[green]Diário Liberado![/]")
            for i in range(0, len(self.__segredos)):
                print(f"- {self.__segredos[i]}")

    @property
    def senha(self):
        raise PermissionError(f"Ninguém tem permissão de ver a senha")

    @senha.setter
    def senha(self, novasenha):
        pass