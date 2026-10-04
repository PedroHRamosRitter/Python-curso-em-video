def ficha(jogador='<desconhecido>', gol=0):
    print(f'O jogador {jogador} fez {gol} gol(s) no campeoneto.')
# Programa Principal
print('-' * 30)
nome = str(input('Nome do jogador: '))
gols = str(input('Número de Gols: '))
if gols.isnumeric(): # isnumeric() -> este valor pode ser um número
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)

