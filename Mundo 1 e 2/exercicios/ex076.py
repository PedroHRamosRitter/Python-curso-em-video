listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90,
            )
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' *  40)

# print(f'{listagem[pos]:.<30}', end=' ')
# print(f'{listagem[pos]:.>30}', end=' ')
# <  ->  Significa alinhado a esquerda sendo igual ao caso acima
# >  ->  Significa alinhado a direita sendo igual ao caso acima

for pos in range(0, len(listagem)):
    if pos % 2 == 0:  # Se voce for ver o produto ele e sempre par exemplo lapis e 0 a borracha e 2 assim por diante
        print(f'{listagem[pos]:.<30}', end=' ') # O :.<30 e para mostrar .... até que o total de caracterres em ponto(....) seja menor que 30 que conta o valor do produto e os pontos tem que dar 29 e o menor > significa alinhado a direita
    elif pos % 2 == 1: # Se o preco for impar mostrar produto e voce ve que dei end para continuar na mesma linha
        print(f'R$ {listagem[pos]:>7.2f}')
print('-' * 40)