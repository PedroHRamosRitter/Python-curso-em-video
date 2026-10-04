valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).strip()[0]
    if continuar in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
elif 5 not in valores:
    print('O valor 5 não faz parte da lista!')