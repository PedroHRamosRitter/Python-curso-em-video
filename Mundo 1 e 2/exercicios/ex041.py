from datetime import date
ano = date.today().year
nascimento = int(input('Qual o ano de nascimento do atleta? '))
idade = ano - nascimento
print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('A categoria é MIRIM')
elif idade <= 14:
    print('A categoria é INFANTIL')
elif idade <= 19:
    print('A categoria é JUNIOR')
elif idade <= 20:
    print('A categoria é SÊNIOR')
else:
    print('A categoria é MASTER')