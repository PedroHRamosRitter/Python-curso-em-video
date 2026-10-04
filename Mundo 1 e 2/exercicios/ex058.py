from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez')
        elif jogador > computador:
            print('Menos...Tente mais uma vez')

print('Acertou com {} tentativas. Parabéns!'.format(palpites))



'''from random import randint
from time import sleep

print('Vou pensar em um número de 0 a 10 tente adivinhar...')
computador = randint(0, 10)
jogador = int(input('Digite um número de 0 a 10: '))

print('-=-' * 20)
print('PROCESSANDO...')
print('-=-' * 20)
sleep(3)

while jogador > 10 or jogador < 0:
    print('Número inválido, tente novemente')
    computador = randint(0, 10)
    jogador = int(input('Digite um número de 0 a 10:'))

while computador != jogador:
    while jogador > 10 or jogador < 0:
        print('Número inválido, tente novemente')
        computador = randint(0, 10)
        jogador = int(input('Digite um número de 0 a 10:'))

    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador,jogador))
    computador = randint(0, 10)
    jogador = int(input('Digite um número de 0 a 10: '))

print('PARABÉNS! Você conseguiu me vencer!')'''
















