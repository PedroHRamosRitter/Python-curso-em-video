def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m².')
# Programa Principal
print('Controle de Terrenos')
print('-' * 40)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)