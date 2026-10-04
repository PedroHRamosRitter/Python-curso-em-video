a=int(input('Quantos dias alugados?'))
km=float(input('Quantos Km rodados?'))
c1= a*60
c2= km*0.15
total=c1+c2
print('O total a pagar é de R${:.2f}' .format(total))