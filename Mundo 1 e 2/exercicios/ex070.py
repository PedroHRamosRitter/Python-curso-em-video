totmil = cont = s = menor = 0
barato = ''
print('-' * 50)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-' * 50)
while True:
    nome = str(input('Nome do Produto: ')).capitalize()
    preço = float(input('Preço: R$'))
    s += preço
    cont += 1

    if preço > 1000:
        totmil += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome

    # else:
    #     if preço < menor:
    #         menor = preço
    #         barato = nome

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R${s:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi o {barato} que custa R${menor:.2f}')
