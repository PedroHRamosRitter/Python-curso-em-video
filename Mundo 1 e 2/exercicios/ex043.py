peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))

# imc = peso / (altura * altura)
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc <= 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')


 # elif <= imc < 25 :
 #    print('Peso ideal')
 # elif <= imc < 30:
 #    print('Sobrepeso')
 # elif <= imc < 40:
 #    print('Obesidade')
 # elif >= 40:
 #    print('Obesidade mórbida')

 # Podendo também se fazer assim