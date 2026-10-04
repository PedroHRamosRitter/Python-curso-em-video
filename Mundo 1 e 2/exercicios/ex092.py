from datetime import date
pessoa = {}
anoatual = date.today().year

pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = int(input('Ano de Nascimento: '))
pessoa['idade'] = anoatual - pessoa['idade']
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem):'))

if pessoa['ctps'] != 0:
    pessoa['anoclt'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + 35
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')




















#     print(pessoa)
#     print(f'Nome tem o valor {pessoa['nome']}')
#     print(f'Idade tem o valor {pessoa['idade']}')
#     print(f'CTPS tem o valor {pessoa['clt']}')
#     print(f'Contratação tem o valor {pessoa['anoclt']}')
#     print(f'Salário tem o valor {pessoa['salario']}')
#     print(f'Aposentadoria tem o valor {pessoa['aposentadoria']}')
# else:
#     print(pessoa)
#     print(f'Nome tem o valor {pessoa['nome']}')
#     print(f'Idade tem o valor {pessoa['idade']}')
#     print(f'CTPS tem o valor {pessoa['clt']}')