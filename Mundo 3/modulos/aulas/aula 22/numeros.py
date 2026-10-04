from uteis import numeros
# from uteis import numeros

# fatorial = numeros.fatorial
# dobro = numeros.dobro
# triplo = numeros.triplo

# Programa Principal
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num) # Se usar o fatorial = numeros.fatorial não precisa usar o fat = numeros. so usar o fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
print(f'O triplo de {num} é {numeros.triplo(num)}')
