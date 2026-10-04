def dobro(n = 0):
    resp = n * 2
    return resp
def metade(n = 0):
    resp = n / 2
    return resp
def aumentar(n = 0, por = 0):
    resp = n + n * por/100
    return resp
def diminuir(n = 0, por = 0):
    resp = n - n * por/100
    return resp

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')

# Replace -> Troca onde tenha ponto para virgula

# def moeda(n = 0):
#     return f'R${n:.2f}'