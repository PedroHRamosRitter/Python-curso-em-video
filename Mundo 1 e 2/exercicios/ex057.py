sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0] #Só pega a primeira letra com o [0]
while sexo not in 'MF':  # Casso não use o .upper() pode colocar assim: while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo:')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
#A lógica é o seguinte enquanto o sexo não for igual a M ou F da erro que seria o not in, caso seja falso o while vai para o print



'''sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]  #Só pego a primeira letra com o [0]
while sexo != 'M' and sexo != 'F':
    print('Sexo incorreto digite novamente')
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
if sexo == 'M':
    print('Sexo Masculino')
elif sexo == 'F':
    print('Sexo Feminino')
print('Fim')
'''