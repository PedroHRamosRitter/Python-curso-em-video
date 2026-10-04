# def lin():
#     print('-' * 30)
#
#
# # Programa Principal
# lin()
# print('     CURSO EM VÍDEO      ')
# lin()
# print('     APRENDA PYTHON      ')
# lin()
# print('     PEDRO HENRIQUE      ')
# lin()

# def mensagem(msg):
#     print('-' * 30)
#     print(msg)
#     print('-' * 30)
#
#
# mensagem('SISTEMA DE ALUNOS')
# mensagem('PEDRO')
# mensagem(10)


# def título(txt):
#     print('-' * 30)
#     print(txt)
#     print('-' * 30)
#
# # Programa Principal
# título('     CURSO EM VÍDEO      ')
# título('     APRENDA PYTHON      ')
# título('     PEDRO HENRIQUE      ')


# a = 4
# b = 5
# s = a + b
# print(s)
#
# a = 8
# b = 9
# s = a + b
# print(s)
#
# a = 2
# b = 1
# s = a + b
# print(s)

# O programa abaixo e igual o de cima usando a funcao(def).

# def soma(a, b):
#     s = a + b
#     print(s)
#
#
# # Programa Principal
# soma (4, 5)
# soma( 8, 9)
# soma(2, 1)
# # Se eu colocar soma(4) da ERRO pois so passei 1 parametro e no def soma disse que era 2 parametros
# soma(4, 1)

# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}')
#
#
# # Programa Principal
# soma(4,5)
# # soma(b = 4, a=  5)
# soma(7, 4)


# def contador(*num):
#     tam = len(num)
#     print(f'Recebi os valores {num} e são ao todo {tam} números')
#     # for valor in num:
#     #     print(f'{valor}, ', end='')
# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

# def dobra(lst): # lst -> lista
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1
#
# valores = [7, 2, 5, 0, 4]
# dobra(valores)
# print(valores)

# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos += 1
#
# valores = [6, 3, 9, -1, 0, 2]
# dobra(valores)
# print(valores)

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores}, temos {s}')
soma(5, 2)
soma(2, 9 , 4)
soma(7, 7, 3)
soma(8, 0)


