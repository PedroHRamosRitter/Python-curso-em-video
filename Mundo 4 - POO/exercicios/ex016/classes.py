class Porta:
    def abrir(self):
        print(f"Abrir porta")

class Empresa:
    def abrir(self):
        print(f"Abrir empresa")

class Ovo:
    def abrir(self):
        print(f"Abrir Ovo")

class Pedra():
    pass

# METÓDO PYTHONICO POLIMORFICOO DUCK TYPING

def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f"Encontrei problemas ao tentar abrir {objeto.__class__.__name__}")