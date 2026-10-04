print('{:=^40}'.format(' LOJAS Pedro '))
preco = float(input('Preço das compras: '))
# m = int(input('FORMAS DE PAGAMENTO \n [ 1 ] Á vista \n [ 2 ] Á vista no cartão \n [ 3 ] 2x no cartão \n [ 4 ] 3x ou mais no cartão \n Qual é a opção?  '))
print('''FORMAS DE PAGAMENTO 
[ 1 ] Á vista 
[ 2 ] Á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
m = int(input('Qual é a opção? '))






if m == 1:
    total = preco - (preco * 10 / 100)
elif m == 2:
    total = preco - (preco * 5 / 100)
elif m == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif m == 4:
    total = preco + (preco * 20 / 100)
    parcelas = int(input('Quantas parcelas: '))
    parcela = total / parcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, parcela))
else:
    print('Metódo de pagamento inválido!')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preco, total ))