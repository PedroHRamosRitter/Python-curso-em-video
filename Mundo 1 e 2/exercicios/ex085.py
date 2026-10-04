# numero = list()
# par = list()
# impar = list()
#
# for c in range(1, 8):
#     numero.append(int(input(f'Digite {c}º valor: ')))
#
# for n in numero:
#     if n % 2 == 0:
#         par.append(n)
#     else:
#         impar.append(n)
#
# print('-=' * 30)
# print(f'Os valores pares digitados foram: {sorted(par)}')
# print(f'Os valores impares digitados foram: {sorted(impar)}')

num = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitaos foram {num[0]}')
print(f'Os valores ímparaes digitados foram {num[1]}')
