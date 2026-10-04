
def area(l, c):
    m = (l * c)
    print(f'A área de um terreno {l}x{c} é de {m}m².')

#Programa Principal
print('Controle de Terrenos')
print('-' * 20)
area(
    float(input('Larguera (m): ')),
    float(input('Comprimento (m): '))
)

