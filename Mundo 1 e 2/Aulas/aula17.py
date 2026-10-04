# Tuplas -> ()
# Listas -> []


# listas são MUTÁVEIS
#

# lanche = ['Hambúrguer', 'Suco', 'Pizza', 'Pudim']
# print(lanche)
# print(lanche[1])
# lanche[3] = 'Picole' # Trocar no lanche 3 por picole
# print(lanche)
# lanche.append('Cookie')  # O metodo append adiciona o cookie na ultima posicao
# print(lanche)
# lanche.insert(0, 'Cachorro quente') # Adicionar na poisação 0, cachorro quente
# print(lanche)
# del lanche[3] # Remove o terceiro item da lista (comecando do 0)
# print(lanche)
# lanche.pop(3) # Remove o terceiro item da lista (comecando do 0)  -> Normalmente para tirar o ultimo elemento
# #lanche.pop() # Tira o ultimo elemento
# print(lanche)
# lanche.remove('Cookie') # Para remover um nome especifico
# print(lanche)
# if 'pizza' in lanche:
#     lanche.remove('Pizza')
# print(lanche)
# valores = list(range(4, 11)) # 4 5 6 7 8 9 10
# print(valores)
# valores = [8, 2, 5, 4, 9, 3, 0]
# print(valores)
# valores.sort()
# print(valores)
# valores.sort(reverse=True)
# print(valores)
# print(len(valores))

# Aula prática

# num = [2, 5, 9, 1]
# num[2] = 3
# # num[4] = 7 -> Não pode porque não pode criar assim tem que ser o metodo append ou insert
# num.append(7)
# num.sort(reverse=True)
# num.insert(2, 2)
# num.remove(2) # Elimina o primeiro 2
# if 5 in num:
#     num.remove(5)
# else:
#     print(f'Não achei o número 4')
# print(num)
# print(f'Essa lista tem {len(num)} elementos.')

valores = list()
# valores.append(5)
# valores.append(9)
# valores.append(4)
# for v in valores:
#     print(f'Na posição {v}...', end='')

# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
#
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Chegeui ao final da lista.')

a = [2, 3, 4, 7]
b = a[:] # Quando faço isto eu faço uma copia de valores de A
b[2] = 8

# b = a
# b[2] = 8 # Aqui quando você muda deste jeito voce muda a lista A e a B pois são iguais
print(f'Lista A: {a}')
print(f'Lista B: {b}')