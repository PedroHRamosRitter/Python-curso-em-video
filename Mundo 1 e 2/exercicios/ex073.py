brasileirao = ('Palmeiras', 'Flamengo', 'Fluminense', 'São Paulo', 'Athletico-PR',
               'Bahia', 'Bragantino', 'Vasco da Gama', 'Coritiba', 'Vitória', 'Cruzeiro',
               'Botafogo', 'Atlético-MG', 'Internacional', 'Grêmio', 'Santos', 'Corinthians',
               'Mirassol', 'Remo', 'Chapecoense')
# for t in brasileirao:  -> Para cada time no brasileirao
#     print(t)  -> Imprima time, e imprime um time por linha
print('-=-' * 30)
print(f'Lista de times do Brasileirão: {brasileirao}')
print('-=-' * 30)
print(f'Os 5 primeiros são: {brasileirao[:5]}')
print('-=-' * 30)
print(f'Os 4 últimos são: {brasileirao[-4:]}')
print('-=-' * 30)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('-=-' * 30)
print(f'O Grêmio esta na {brasileirao.index('Grêmio') + 1}ª posição')