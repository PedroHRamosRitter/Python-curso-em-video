velocidade = float(input('Qual é a velocidade atual do carro?'))

if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança')
























# v = float(input('Qual foi a velocidade em Km/h que você estava com seu carro: '))
#
# valor = (v - 80) * 7
#
# # Caso passe de 80km sera multado por 7 reais o km acima do limite
#
# print('A sua velocidade foi de {} e o limite máximo é de: '.format(v))
#
# if v<=80:
#     print('Você não ultrapassou o limite de velocidade, BOA VIAGEM!')
# else:
#     print('Você ultrapassou o limite de velocidade e tomara uma multa de {:.2f} Reais'.format(valor))
#