from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?')) #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))


# Como eu fiz

# from random import choice
# p = int(input('Adivinhe um número de 0 a 5: '))
#
# n0 = 0
# n1 = 1
# n2 = 2
# n3 = 3
# n4 = 4
# n5 = 5
#
# lista = [n0, n1, n2, n3, n4, n5]
# escolhido = choice(lista)
#
# print('O número escolhido foi {}' .format(escolhido))
# if p==escolhido:
#     print('Você venceu!')
# else:
#     print('Você perdeu!')