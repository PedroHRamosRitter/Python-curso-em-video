salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))




# s =  float(input('Qual é o seu salário: '))
# c1 = s + s * 15/100
# c2 = s + s * 10/100
#
# if s<=1250.00:
#     print('Você recebeu um aumento de R$: {:.2f}'.format(c1))
# else:
#     print('Você recebeu um aumento de R$: {:.2f}'.format(c2))
