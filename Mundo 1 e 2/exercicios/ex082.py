valores =  list()
valorespar = list()
valoresimpar = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar == 'N':
            sair = True
            break

        elif continuar == 'S':
            sair = False
            break
        else:
            print('Valor inválido! ')
    if sair:
        break
for valor in valores:
    if valor % 2 == 0:
        valorespar.append(valor)
    else:
        valoresimpar.append(valor)
print('-=-' * 50)
print(f'A lista completa é {valores}')
print('-=-' * 50)
print(f'A lista de pares é {valorespar}')
print('-=-' * 50)
print(f'A lista de ímpares é {valoresimpar}')
