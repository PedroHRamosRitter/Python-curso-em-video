n = int(input('Digite um número: '))
contador = n
fatorial = 1   # Não posso começar a multiplicação com 0 porque to número multiplicado por 0 é 0
print('Calculando {}! = '.format(n), end='')
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))