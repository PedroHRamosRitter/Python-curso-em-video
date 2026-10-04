def dobro(n = 0, formato = False):
    resp = n * 2
    return resp if formato is False else moeda(resp)

def metade(n = 0, formato = False):
    resp = n / 2
    return resp if formato is False else moeda(resp)

def aumentar(n = 0, por = 0, formato = False):
    resp = n + n * por / 100
    return resp if formato is False else moeda(resp)

def diminuir(n = 0, por = 0, formato = False):
    resp = n - n * por / 100
    return resp if formato is False else moeda(resp)

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:>.2f}'.replace('.', ',')








