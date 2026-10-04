produto=float(input('Qual é o preço do produto? R$'))
desconto= produto - produto*5/100

print('O produto que custava R${}, na promoçao com desconto de 5% vai custar R${:.2f}' .format(produto, desconto))