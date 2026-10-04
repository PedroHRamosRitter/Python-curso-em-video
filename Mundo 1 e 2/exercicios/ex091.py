from operator import itemgetter
from random import randint
from time import sleep
jogador = {}
print('valores sorteados:')
jogador['jogador1'] = randint(1, 6)
jogador['jogador2'] = randint(1, 6)
jogador['jogador3'] = randint(1, 6)
jogador['jogador4'] = randint(1, 6)
for k, v in jogador.items():
    print(f'O jogador {k} tirou {v}')
# for c in jogador:
#     print(f'{c} tirou {jogador[c]}')
    sleep(1)
print('-=' * 30)
print('  == Ranking dos jogadores ==')
ranking = list()
ranking = sorted(jogador.items(), key=itemgetter(1), reverse = True)
for i, c in enumerate(ranking):
    print(f'    {i+1} lugar: {c[0]} com {c[1]}')
    sleep(1)
