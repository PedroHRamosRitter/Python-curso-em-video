n = s = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n  # s += n porque é igual a soma = soma + número que da a soma que já tem mais o número digitado
#print('A soma vale {}'.format(s))
print(f'A soma vale {s}') #forma nova se chma f strings


nome = 'José'
idade = 33
print(f'O {nome} tem {idade} anos.') #Python 3.6+
print('O {} tem {} anos.'.format(nome, idade)) # Python 3
print('O %s tem %d anos.' %(nome, idade)) # Python 2











'''while True:
    cont = 1
    print(cont, '...', end='')
    cont += 1
'''