from time import sleep
def lin():
    print('-=' * 40)
def maior (*valores):
    tam = len(valores)
    print(f'Analisando os valores passados...')
    if tam > 0:
        for n in valores:
            print(f'{n} ', end='')
        print(f'Foram informados {tam} valores ao todo.')
        print(f'O maior valor informadoi foi {max(valores)}')
    else:
        print('Foram informado 0 valores ao todo.')
        print('O maior valor informado foi 0')
    lin()
# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()