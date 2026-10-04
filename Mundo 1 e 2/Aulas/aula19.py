# Tuplas -> ()
# Listas -> [] ou list()
# Dicionários -> {} ou dict()

# dados = {}
# dados = dict()

# dados = {'nome': 'Pedro', 'idade': 25}
# print(dados)
# print(dados['nome'])
# print(dados['idade'])
# dados['nome'] = 'Gustavo'
# dados['sexo'] = 'M'
# del dados['idade']
# print(dados)

# filme = {'filme': 'Star Wars','ano': '1977', 'diretor': 'George Lucas' }

# values -> Pega o que esta dentro dos dois pontos de todos
# keys -> Pega o que esta fora dos dois pontos pega todos
# items -> Pega values, keys
# Exemplo abaixo

# print(filme)
# print(filme.values())
# print()
# print(filme.keys())
# print()
# print(filme.items())
# for k, v in filme.items():
    # k -> keys
    # v -> values
    # print(f'O {k} é {v}')

# locadora = [{'titulo': 'Star Wars', 'ano': '1977', 'diretor': 'George Lucas'}, {'tiulo': 'Avengers', 'ano': '2012', 'diretor': 'Joss Whedon'}, {'titulo': 'Matrix', 'ano': '1999', 'diretor': 'Wachowski'}]
# # print(locadora[0]['ano'])
# # print(locadora[2]['ano'])
# for k, v in locadora[0].items():
#     print(f'{k} é {v}')
# print()
# for k, v in locadora[1].items():
#     print(f'{k} é {v}')
# print()
# for k, v in locadora[2].items():
#     print(f'{k} é {v}')


#  Aula Prática


pessoas = {'nome': 'Pedro', 'sexo': 'M', 'idade': '18'}
# print(pessoas)
# print(pessoas['nome'])
# print(pessoas['sexo'])
# print(pessoas['idade'])
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items()) # Representacao gráfica de listas
# for k, v in pessoas.items():
#     print(f'{k.capitalize()} = {v.capitalize()}')
# del pessoas['sexo']
# pessoas['nome'] = 'Renato'
# pessoas['idade'] = '61'
# pessoas['peso'] = '107.5'
# for k, v in pessoas.items():
#     print(f'{k.capitalize()} = {v.capitalize()}')

# brasil = []
# estado1 = {'uf': 'Rio Grande do Sul', 'sigla': 'RS'}
# estado2 = {'uf': 'Santa Catarina', 'sigla': 'SC'}
# estado3 = {'uf': 'Paraná', 'sigla': 'PR'}
# estado4 = {'uf': 'São Paulo', 'sigla': 'SP'}
# estado5 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# brasil.append(estado1)
# brasil.append(estado2)
# brasil.append(estado3)
# brasil.append(estado4)
# brasil.append(estado5)
# # print(estado1)
# # print(estado2)
# # print(estado3)
# # print(estado4)
# # print(estado5)
# print(brasil)
# print(brasil[0])
# print(brasil[2])
# print(brasil[0]['uf'])
# print(brasil[2]['uf'])

# copy -> copiar
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    # brasil.append(estado) -> ERRO so aparece o ÚLTIMO ESTADO tem que fazer uma copia
    # brasil.append(estado[:]) -> ERRO pois NÃO É POSSIVEL fazer um FATIAMENTO
    brasil.append(estado.copy()) # copy() AQUI DA CERTO
print(brasil)
for e in brasil: # estado
    for k, v in e.items(): # keys  # values # estado
        print(f'O campo {k} tem o valor {v}')
# for e in brasil:
#     for v in e.values():
#         print(v, end=' ')
#     print()