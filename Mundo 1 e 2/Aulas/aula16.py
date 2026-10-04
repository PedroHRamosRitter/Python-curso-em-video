# As tuplas são IMUTÀVEIS
# parenteses, conchetes, chaves -> O que usar abaixo
# Tupla = ()
# Lista = []
# Dicionario = {}

# lanche = "Hambúrguer"
# lanche = "Suco"
# lanche = "Pizza"
# lanche = "Pudim"
# print(lanche)
# Não adiona tipo uma lista

# lanche = () -> No Python novo a parir do 3.5 não precisa usar parenteses

#lanche = ('Hambúerguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')  # Aqui fiz uma lista usando as tuplas
# print(lanche[3])
# print(lanche)
# print(lanche[-2]) # Mostra ao contrario no caso a pizza
# print(lanche[1:3]) # Vai mostar o suco e pizza o pudim não vai porque não conta o último elemento
# print(lanche[:2])  # Vai até o suco porque não conta o último elemento
# print(lanche[-2:]) # Pega a pizza e o pudim
# print(lanche[1:]) # Mostra do elemento 1 até acabar
#
# # lanche[1] = 'Refrigerante' -> Tuplas são imutaveis não funiona
# print(lanche)

# for comida in lanche:
#     print(f'Eu vou comer {comida}')
#
# for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} na posição {cont}')
#
# # print(len(lanche))
# for pos, comida in enumerate(lanche):  # Para cada comida no lanche
#     print(f'Eu vou comer {comida} na posição {pos}') # Imprimi Eu vou come (para cada comida) comida
# print('Comi pra caramba!') # No final somente um Comi para caramba

# print(sorted(lanche)) # Sorted mostra em ordem, como a tupla é imutavel nao mudou, so mostrou em ordem
# print(lanche)

a = (2, 5, 4)
b = (5, 8, 1, 2)

print(a)
print(b)

c = a + b
print(c)
# print(len(c))
# print(c.count(5)) # Mostra quantas vezes apareceu o elemento no caso o 5
# print(c.count(9))
# print(c.index(8)) # Mostra em que posição esta o elemento no caso o 8
print(c.index(5))
print(c.index(5, 1)) # A partir da posição 1 mostra onde esta o 5

pessoa = ('Pedro', 18, 'M', 99.88) # Pode ter dados diferentes dentro da tupla
print(pessoa)
# del(pessoa) # Apaga a pessoa -> E a tupla é imutável so podendo ser apagada
# del(pessoa[1]) # Erro pois não se pode apagar somente o elemento da posição 1 de uma tupla
# print(pessoa)

