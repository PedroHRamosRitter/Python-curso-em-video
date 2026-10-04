from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

# print(f'Os valores sorteados foram: {numeros}')
# maior = menor = numeros[0]
#
# for n in range(0, 5): # Aqui tem ques ser range para fazer de 1 a 5
#     if numeros[n] > maior:
#         maior = numeros[n]
#     elif numeros[n] < menor:
#         menor = numeros[n]
#
# print(f'O maior valor sorteado foi {maior}')
# print(f'O menor valor sorteado foi {menor}')

print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\n  O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')