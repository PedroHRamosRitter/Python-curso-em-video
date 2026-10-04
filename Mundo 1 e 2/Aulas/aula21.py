# Python console help -> Ajuda interativa onde se tem o que o comando faz]
# help(print) # Outro jeito qu efunciona
# print(input.__doc__) # Vai mostrar a ajuda do input
# o .__doc__ da algumas coisa diferentes do help

# def contador(i, f, p):
#     # Criei uma docstring abaixo usando 3 aspas duplas
#     """
#     -> Faz uma contagem e mostra na tela.
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     # param -> parametro
#     c = i
#     while c <= f:
#         print(f'{c} ', end = '')
#         c += p
#     print('FIM!')
#
# # contador(0, 100, 10)
# print(contador.__doc__)

# def somar(a=0, b=0, c=0):
#     """
#     -> Faz soma de três valores e mostre o resultado na tela.
#     :param a: o primeiro valor
#     :param b: o segundo valor
#     :param c: o terceiro valor
#     """
#     s = a + b + c
#     print(f'A soma vale {s}')
#
# somar(5, 7, 2)
# # somar(2, 3)
# # somar(5)
# # somar(b=2, c=4)
# # somar(a=0, c=2)
# # somar(a=2, b=2)
# # somar(a=0, b=0, c=0)
# somar(c=0, a=1)
# somar(b=2, a=3)
# # somar()


# def teste():
#     x = 8 # x é um escopo local
#     print(f'Na função teste, n vale {n}')
#     print(f'Na função teste x, vale {x}')
# # Programa Principal
# n = 2 # n é uma váriavel global
# print(f'No Programa Principal, n vale {n}')
# teste()
# #print(f'No programa principal, n vale {x}') #-> Erro pois o x é um escopo local e só funciona detro da função teste

# def teste(b):
#     a = 8 # Neste a especifico o que acontece o python cria um escopo local do a tipo um novo a local valendo 8
#     b += 4 # Como eu não criei conexao com a no teste(a) nao muda o A muda somente o B
#     c = 2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')
#
# # Programa Principal
#
# a = 5 # este a e um A com escopo global valendo 5
# teste(a)
# print(f'A fora vale {a}')
# # print(f'B fora vale {b}') # Erro pois B que defini e um B local e so funciona na funcao teste
# # print(f'C fora vale {c}') # Erro pois C que defini e um C local e so funciona na funcao teste

# def funcao():
#     n1 = 4
#     print(F'N1 local vale {n1}')
# n1 = 2
# funcao()
# print(f'N1 global vale {n1}')


# def teste(b):
#     global a # Estou dizendo por favor use o A global
#     a = 8 # este a deixa de ser local e passa a ser global
#     b += 4
#     c = 2
#     print(f'A dentro vale {a}')
#     print(f'B dentro vale {b}')
#     print(f'C dentro vale {c}')
#
# # Programa Principal
#
# a = 5 # este A e redefinido para 8 assim que executo a função teste e passa a valer 8
# teste(a)
# print(f'A fora vale {a}')

# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s
#
# # Programa Principal
# #print(somar(3, 2, 5)) #para usar o return ou guarda dentro de uma variavel ou usar o print
# r1 = somar(3, 2, 5) # para usar o return ou guarda dentro de uma variavel ou usar o print
# r2 = somar(1, 7)
# r3 = somar(4)
# r4 = somar()
# print(f'Meus cálculos deram {r1}, {r2}, {r3} e {r4}.')


# Aula Prática

# def fatorial(num=1):
#     f = 1
#     for c in range(num, 0, -1):
#         f *= c
#     return f
#     # return não e so para número pode retorna um valor lógico, etc
# n = int(input('Digite um número: '))
# print(f'O fatorial de {n} vale {fatorial(n)}')
#
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os resultados são {f1}, {f2}, {f3}')


def par(num=0):
    if num % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
print(par(num))
if par(num):
    print(f'É par!')
else:
    print(f'Não é par!')

