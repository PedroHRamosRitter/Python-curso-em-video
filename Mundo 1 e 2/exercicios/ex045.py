from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))

# if jogador == 0 or jogador == 1 or jogador == 2:
if jogador <= 0 or jogador <= 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('-=' * 11)
    print('Computador jogou {}'.format(itens[computador]))
    print('jogador jogou {}'.format(itens[jogador]))
    print('-=' * 11)
else:
    print('JOGADA INVÁLIDA. TENTE NOVAMENTE!')

if computador == 0: # computador jogou PEDRA

    if jogador == 0: #jogaodor jogou PEDRA
        print('EMPATE')
    elif jogador == 1: # jogador jogou Papel
        print('JOGADOR VENCE')
    elif jogador == 2: #jogador jogou TESOURA
        print('COMPUTADOR VENCE')

elif computador == 1: # computador jogou PAPEL

    if jogador == 0: # jogador jogou PEDRA
        print('COMPUTADOR VENCE')
    elif jogador == 1: # jogador jogou PAPEL
        print('EMPATE')
    elif jogador == 2: # jogador jogou TESOURA
        print('JOGADOR VENCE')

elif computador == 2: #computador jogou TESOURA

    if jogador == 0: # jogador jogou PEDRA
        print('JOGADOR VENCE')
    elif jogador == 1: # jogador jogou PAPEL
        print('COMPUTADOR VENCE')
    elif jogador == 2: # jogador jogou TESOURA
        print('EMPATE')
