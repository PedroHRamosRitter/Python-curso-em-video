import math
num=int(input('Digite um número: '))
raiz=math.sqrt(num)
print('A raiz de {} é igual a {}' .format(num, raiz))
# print(f'A raiz de {num} é igual a {raiz}') caso queira não usar .format python 3.6 e tem que colocar o f no inicio
# print('A raiz de ' + str(num) + ' é igual a ' + str(raiz) + '.') usando Usando concatenação simples
# math.ceil(raiz) 'arredonda o numero para cima'
# math.floor(raiz) 'arredonda para baixo'
# math.trunc() para não ter casas decimais
# O import math serve para importar a biblioteca math
# caso queira usar somente uma coisa usar "from math import sqrt"
# "from math(biblioteca) import sqrt(coisa individual da biblioteca)"
# e quando você usar from math import sqrt nao pode usar math.sqrt só usar sqrt