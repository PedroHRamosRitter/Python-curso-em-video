tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
print(f'Você digitou os valores {tupla}')

print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla: # Se 3 estiver na tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posição')
else:
    print(f'O valor 3 não foi dgitado em nenhuma posição')
# Para cada número da tupla par adiciona 1 no contador
cont = 0
print(f'Os números pares digitados foram ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
        cont += 1


print(f'\nOs valores pares digitados foram: {cont}')