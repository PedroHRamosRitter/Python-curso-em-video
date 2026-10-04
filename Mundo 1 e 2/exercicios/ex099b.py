from time import sleep
def lin():
    print('-=' * 40)
def maior (*valores):
    cont = maior = 0
    print(f'Analisando os valores passados...')
    for n in valores:
        print(f'{n} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    lin()
# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()