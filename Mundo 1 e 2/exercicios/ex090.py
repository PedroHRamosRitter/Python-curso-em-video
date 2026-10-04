situacao = dict()
situacao['Nome'] = str(input('Nome: ')).capitalize()
situacao['Media'] = float(input(f'Média de {situacao["Nome"]}: '))
if situacao['Media'] >= 7:
    situacao['Aluno'] = 'Aprovado'
elif 5 <= situacao['Media'] <7:
    situacao['Aluno'] = 'Recuperação'
elif situacao['Media'] < 5:
    situacao['Aluno'] = 'Reprovado'
print('-=' * 30)
for k, v in situacao.items():
    print(f' - {k} é igual a {v}')