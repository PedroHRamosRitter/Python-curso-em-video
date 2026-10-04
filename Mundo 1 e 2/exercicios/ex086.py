matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3): # l -> linha
    for c in range(0, 3): # c -> coluna
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]:  '))
        # matiz -> [linha][coluna]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print() # print para quebre a linha para que toda vez que der 3 colunas quebrar a linha






















