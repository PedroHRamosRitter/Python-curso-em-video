n = cont = soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
print('Você digiotu {} números e a soma entre eles foi {}'.format(cont, soma))

#O motivo de colocar 2 n = int(input('Digite um número [999 para parar]: ')) é
# porque não se conta o 999 e não se soma quando coloco no ínicio e no final ele não passa pelo cont e nem pela soma