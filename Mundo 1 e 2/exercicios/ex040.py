n1 = float(input('Qual foi a sua nota do 1º semestre? '))
n2 = float(input('Qual foi a sua nota do 2º semestre? '))
média = (n1 + n2) / 2

if média >= 7.0:
    print('Aprovado')
elif 6.9 > média >= 5.0:
# elif média <= 6.9 and média >= 5.0:
    print('Recuperação')
elif média <5.0:
    print('Reprovado')
# else:
#     print('Reprovado')
