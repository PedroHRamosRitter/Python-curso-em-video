pessoas = list()
temp = list()
maior = menor = 0
while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    pessoas.append(temp[:])
    temp.clear()
    r = str(input('Quer continuar? [S/N] ')).strip()[0]
    if r in 'Nn':
        break

print('-=' * 30)
print(f'Os dados foram: {pessoas}')
# A
print(f'O número de pessoas cadastradas: {len(pessoas)}')

for p in pessoas:
    if maior == 0 and menor == 0:
        maior = menor = p[1]
    else:
        if p[1] > maior:
            maior = p[1]

        if p[1] < menor:
            menor = p[1]

# B
print(f'O maior peso foi de {maior}Kg. Peso de ',end='')
for n in pessoas:
 if n[1] == maior:
     print(f'[{n[0].capitalize()}] ', end='')
print()
# C
print(f'O menor peso foi de {menor}Kg. Peso de ',end='')
for n in pessoas:
    if n[1] == menor:
        print(f'[{n[0].capitalize()}] ', end='')