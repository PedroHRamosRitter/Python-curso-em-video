from rich import print
from rich.panel import Panel

# Declaração de Classe
class Churrasco:
    consumo_padrao:float = 0.400
    preco_kg:float = 82.40

    def __init__(self, titulo, quantidade):
        self.titulo = titulo
        self.participantes = quantidade

    def calcular_qtd_carne(self) -> float:
        return self.participantes * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * self.__class__.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.participantes

    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/] com {self.participantes} [blue]convidados[/]"
        conteudo += f"\nCada participante comerá 0.4Kg e cada Kg custa R$82.40"
        conteudo += f"\nRecomendo [blue]comprar {self.calcular_qtd_carne():,.3f}Kg[/] de carne"
        conteudo += f"\nO custo total será de [green]R${self.calcular_custo_total():,.2f}[/]"
        conteudo += f"\nCada pessoa pagará [yellow]R${self.calcular_custo_individual():,.2f}[/] para participar."
        painel = Panel(conteudo, title=self.titulo)
        print(painel)

# Declaração de Objeto

# Considere:
# Consumo padrão: 400g por pessoa
# Preço: R$82,40/kg

c1 = Churrasco("Churrasco dos guri", 15)
c1.analisar()