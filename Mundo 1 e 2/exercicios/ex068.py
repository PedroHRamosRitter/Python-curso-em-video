from random import randint
cont = 0
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=' * 10)
while True:
    n1 = int(input('Diga um valor: '))
    jogador = ' '
    while jogador not in 'PI':
        jogador = str(input('Par ou Ìmpar? [P/I] ')).upper().strip()[0]
    computador = randint(0, 11)
    total = n = n1 + computador


    if n % 2 == 0:
        n = 'Par'
    else:
        n = 'Ìmpar'

    # print(f'Você jogou {n1} e o computador {computador}. Total de {total} ', end ='')
    # print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')


    if jogador == 'P':
        if n == 'Par':
            print(f'''Você jogou {n1} e o computador {computador}. Total de {total} deu PAR
Você venceu!
Vamos jogar novamente...
''')
            print('=-=' * 10)
            cont += 1
        else:
            print(f'''Você jogou {n1} e o computador {computador}. Total de {total} deu ÍMPAR
Você PERDEU!
''')
            print('=-=' * 10)
            break
    elif jogador == 'I':
        if n == 'Par':
            print(f'''Você jogou {n1} e o computador {computador}. Total de {total} deu PAR
Você PERDEU!
''')
            print('=-=' * 10)
            break
        else:
            print(f'''Você jogou {n1} e o computador {computador}. Total de {total} deu ÍMPAR
Você venceu!
Vamos jogar novamente...
''')
            print('=-=' * 10)
            cont += 1
print(f'GAME OVER! Você venceu {cont} vezes.')
