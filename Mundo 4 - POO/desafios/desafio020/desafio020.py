from rich import print
from rich.panel import Panel
#from rich import inspect

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, jogo):
        self.favoritos.append(jogo)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f"Nome real: [black on blue]{self.nome} [/]"
        conteudo += f"\nJogos favoritos:"
        for num, game in enumerate(self.favoritos):
            conteudo += f"\n:video_game: [blue]{game}[/]"
        painel = Panel(conteudo, title=f"<{self.nick}>", width=40)
        print(painel)

j1 = Gamer("Pedro", "Barry")
j1.add_favoritos("CS2")
j1.add_favoritos("Ben 10")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()

j2 = Gamer("Renato", "Renato")
j2.add_favoritos("Call of Duty")
j2.add_favoritos("Gran Turismo 7")
j2.add_favoritos("Doom")
j2.ficha()
