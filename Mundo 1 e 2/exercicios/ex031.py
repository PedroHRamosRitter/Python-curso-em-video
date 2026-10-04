distância = float(input('Qual é a distância de sua viagem? '))
print('Você estâ prestes a começar uma viagem de {}Km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))


# viagem = int(input('Qual a distância da viagem? '))
#
# v1 = viagem * 0.5
# v2 = viagem * 0.45
#
# if viagem<=200:
#     print('O valor da viagem é de R$: {}'.format(v1))
# else:
#     print('O valor da viagem é de R$: {}'.format(v2))