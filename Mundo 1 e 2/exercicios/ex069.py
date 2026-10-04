cont = homens = mulher = 0
while True:
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    print('-' * 20)
    if idade >= 18:
        cont += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('-' * 20)
    if continuar == 'N':
        break
print(f'{cont} pessoas tem mais de 18 anos.')
print(f'{homens} homens cadastrados.')
print(f'{mulher} mulheres tem manos de 20 anos.')
