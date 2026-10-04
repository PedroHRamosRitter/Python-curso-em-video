# dados = list()
# dados.append('Pedro')
# dados.append(18)
# pessoas = list()
# pessoas.append(dados[:])  # Comando [:] sigiifica faiamento completo (uma copia por assim dizer) da estrutura dados
# # [:] -> Significa fatiamento completo
# # Estou dizendo basicamente copiar lista
# dados[0] = 'Maria'
# dados[1] = 16
# pessoas.append(dados[:])
# dados[0] = 'João'
# dados[1] = 17
# pessoas.append(dados[:])
#
# print(pessoas)
# print(pessoas[0][0])
# # [0][0] -> Como isto é lista sobre lista eu vou pegar no caso pedro
# print(pessoas[0][1])
# print(pessoas[1][1])

#Aula prática

# teste = list()
# teste.append('Pedro')
# teste.append(18)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
#
# print(galera)

# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# print(galera)
# print(galera[0])
# print(galera[0][0])
# print(galera[0][1])
# print(galera[2][1])
# print(galera[3])
# print(galera[3][1])

# for p in galera:
#     print(f'O nome é {p[0]} e a idade é {p[1]}.')
#     print()
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')

# print() -> Deixa uma linha sem nada tipo um pula linha

galera = list()
dado = list()
totmai = totmen = 0
# totmai -> total maior
# totmen -> total menor
# O c do for no caso é para significar contador
# c -> Contador
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # Aqui faz uma copia por vez para que o conchetes seja fechado sempre depois da idade
    # galera.append(dado) #-> Copia tudo vazio porque depois eu do clear
    dado.clear()
# galera.append(dado[:])  ->  Se eu colocasse so isto aqui so teria 2 conchetes 2 no inicio e 2 no final
print(galera)

for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1; print(f'Temos {totmai} maiores de idade.')
print(f'Temos {totmen} menores de idade.')