ficha = list()
while True:
    nome = str(input('Qua o nome do aluno: ')).capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    nota3 = float(input('Nota 3: '))
    media = (nota1 + nota2 + nota3) / 3
    ficha.append([nome, [nota1, nota2, nota3], media])
    r = str(input('Quer continuar? [S/N] ')).strip()
    if r in 'Nn':
        break

print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<8}{"MÉDIA":>8}')
print('-' * 30)
for i, a in enumerate(ficha):
    print(f'{i+1:<4}{a[0]:<8}{a[2]:>8.1f}')
while True:
    opc = int(input('Quer ver notas de qual aluno? [999 interrompe] '))
    if opc == 999:
        break
    if opc <= len(ficha):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< Volte sempre! >>>')