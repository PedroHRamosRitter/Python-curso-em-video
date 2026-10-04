from random import randint
from time import sleep
def sorteia(lst):
    print('Sorteando os 5 valores da lista: ', end='')
    for c in range(0, 5):
        lista.append(randint(1, 10))
    sleep(0.7)
    for n in lst:
        print(f'{n} ', end = '')
        sleep(0.5)
    print('PRONTO!')
def somaPar(par):
    soma = 0
    for n in par:
        if n % 2 == 0:
            soma += n
    print(f'Somando os valores pares de {lista}, temos {soma}')

# Programa Principal
lista = []
sorteia(lista)
somaPar(lista)