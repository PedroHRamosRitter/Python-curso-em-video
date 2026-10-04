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



def lin():
    print('-' * 30)

def resumo(n, a, r):
        lin()
        print(f'RESUMO DO VALOR'.center(30))
        lin()
        print(f'Preço analisado: \t{moeda(n)}')
        print(f'Dobro do preço: \t{dobro(n, formato = True):>}')
        print(f'Metade do preço: \t{metade(n, formato = True):>}')
        print(f'{a}% de aumento: \t{aumentar(n, por = a, formato = True):>}')
        print(f'{r}% de redução: \t{diminuir(n, por = r, formato = True):>}')
        lin()
        # \t -> tabulação tipo uma tabela