from rich import print, inspect
from poligno import Quadrado, Circulo

def main():
    q = Quadrado(20)
    print(f"[blue]Um quadrado de lado [green]{q.lado}cm[/] perimetro [green]{q.perimetro():.1f}[/][red]cm[/]")
    print(f"[blue]Um quadrado de lado [green]{q.lado}cm[/] área [green]{q.area():.1f}[/][red]cm²[/]")

    c = Circulo(12)
    print(f"[red]Um círculo de raio [blue]{c.raio}cm[/] tem perímetro de {c.perimetro():.1f}[/][green]cm[/]")
    print(f"[red]Um círculo de raio [blue]{c.raio}cm[/] tem área de {c.area():.1f}[/][green]cm²[/]")

if __name__ == "__main__":
    main()
