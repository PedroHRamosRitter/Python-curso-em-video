valorcasa = float(input(' Qual o valor da casa: R$ '))
salário = float(input('Qual o seu salário: R$ '))
anos = int(input('Quantos anos deseja pagar: R$ '))

prestação = valorcasa / anos
prestaçãomensal = prestação / 12
calculo = salário - salário * 70/100

if calculo >= prestaçãomensal:
    print('Seu emprestimo foi aprovado!')
else:
    print('Infelizmente seu emprestimo foi negado!')

# Para saber a prestação mais fácil so fazer valorcasa / (anos * 12)
# print('Para pagar uma casa de R${:.2f} em {} anos'.format(valorcasa, anos), end='')