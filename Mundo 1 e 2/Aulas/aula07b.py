n1= int(input('digite um valor'))
n2=int(input('digite outro valor'))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1**n2
print('A soma {}, o produto é {} e a divisão é {}' .format(s, m, d))
print('Divisão inteira {} e potência {}' .format(di, e))
#caso queira colocar numeros maximos de casas decimais e so colocar nas {:.3f} siga o exemplo da linha de baixo como abaixo tem 2 casas decimais;
#caso queira que nao quebre a liha de um print para outro e so colocar antes do ultimo parentes o seguinte (, end=' ')
#Mas para quebrar a linha e só apertar /n  e /n de onde ate onde quebrar a linha /n significa (nova linha)
print('A divisão é {:.2f}' .format(d))
print('A soma {}, o produto é {} e a divisão é {}' .format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}' .format(di, e))
print('A soma {}, \n O produto {}, \n A divisão é {}' .format(s, m, d))
n1= int(input('digite um valor ='))
n2= int(input('digite outro valor ='))
soma=n1+n2
subtracao=n1-n2
multiplicacao=n1*n2
divisao=n1/n2
potencia=n1**n2
divisaointeira=n1//n2
restodadivisao=n1%n2
porcentagem=n1*n2/100

r2=int(input('Digite a raiz'))
raiz=r2**(1/2)

r3=int(input('Digite a raiz cubica'))
raizcubica=r3**(1/3)

c=input('digite algum caractere')
nmc=int(input('Digite o número de vezes que o caractere vai ser repetido'))
caractere=c*nmc
#nmc de numero multiplicado de caracteres

print('O resultado de {} mais {} é igual a {}' .format(n1, n2, soma))
print('O resultado de {} menos {} é igual a {}' .format(n1, n2, subtracao))
print('O reultado de {} multiplicado por {} é igual a {}' .format(n1, n2, multiplicacao))
print('O resultado de {} dividido por {} é igual a {}' .format(n1, n2, divisao))
print('O resultado de {} elevado por {} é igual a {}' .format(n1, n2, potencia))
print('O resultado de {} por divisão inteira de {} é igual a {}' .format(n1, n2, divisaointeira))
print('O resultado de {} pelo resto da divisão de {} é igual a {}' .format(n1, n2, restodadivisao))
print('O resultado de {} porcento de {} é igual a {}'.format(n1, n2, porcentagem))
print('O resultado da raiz de {} é {}' .format(r2, raiz))
print('O resultado da raiz cubica de {} é {}' .format(r3, raizcubica))
print('{}' .format(caractere))
