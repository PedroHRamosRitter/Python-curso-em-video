n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1>n2:
    print('O primeiro valor é maior que o segundo')
elif n2>n1:
    print('O segundo valor é maior que o primeiro')
else:
    print('Não existe valor maior, os dois são iguais')

# elif n1==n2:
#     print('Não existe valor maior, os dois são iguais')
# Pode se fazer assim também no lugar do else