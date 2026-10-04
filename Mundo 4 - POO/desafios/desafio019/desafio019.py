from rich import print
from time import sleep

pagina_atual = 1
pagina = 1

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: [blue]Você acabou de abrir o livro '[green]{self.titulo}[/]' que tem [red]{self.total_paginas}[/] páginas no total. Você agora está na página [yellow]{self.pagina_atual}[/]")

    def avancar_pagina(self, qtd = 1):
        cont = 0
        for pg in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág{self.pagina_atual} :arrow_forward: ", end='')
                cont += 1
                sleep(0.05)
        print(f"[blue]Você avançou {cont} páginas agora está na página [yellow]{self.pagina_atual}[/][/]")

        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao final do livro '{self.titulo}'[/]")

    def fim_do_livro(self):
        return True if self.pagina_atual == self.total_paginas else False

l1 = Livro("Bíblia Sagrada", 100)
l1.avancar_pagina(5)
l1.avancar_pagina(50)
l1.avancar_pagina(50)


