print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
contador = 1

while contador <= 10:
    print('{}'.format(termo), end= ' → ')
    termo += razão
    contador += 1
print('Fim')
