matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = scol = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma dos valores pares é {spar}.')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da 3ª coluna é {scol}.')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')

# print('-=' * 30)
#
# # Soma de pares
# somapar = maior = somac3 = 0
# for p in par:
#     somapar = somapar + p
# print(f'A soma dos valores pares é {somapar}')
#
# # Soma dos valores da 3º coluna

# for s in range(0, 3):
#     somac3 = somac3 + matriz[s][2]
# print(f'A soma dos valores da 3ª coluna é {somac3}')
#
# # Maior valor da segunda linha
# for m in range(0, 3):
#     if matriz[1][m] > maior:
#         maior = matriz[1][m]
# print(f'O maior valor da segunda linha é {maior}')