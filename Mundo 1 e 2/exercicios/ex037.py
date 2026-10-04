n = int(input('Digite um número inteiro: '))
bc = int(input('Escolha a base da conversão sendo \n [ 1 ] binário \n [ 2 ] octal \n [ 3 ] hexadecimal: \n Sua opção: '))

if bc == 1:
    binário = bin(n) [2:]
    print('{} convertido para BINÁRIO é {} '.format(n, binário))
elif bc == 2:
    octal = oct(n) [2:]
    print('{} convertido para OCTAL é {} '.format(n, octal))
elif bc == 3:
    hexadecimal = hex(n) [2:]
    print('{} convertido para HEXADECIMAL é {} '.format(n, hexadecimal))
else:
    print('Opço inválida!')