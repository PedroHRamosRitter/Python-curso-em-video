valores = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar... ')
    continuar = str(input('Quer continuar? [S/N] ')).strip()[0]
    if continuar in 'Ss':
     pass
    elif continuar in 'Nn':
        break
    else:
        print('Valor inválido. Tente novamente: ')
print('-=' * 30)
valores.sort()
print(f'Você digitou os valores {valores}')
