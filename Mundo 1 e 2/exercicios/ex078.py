valores = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
print('=-' * 30)
print(f'Você digitou os valores  {valores}')
for pos, n in enumerate(valores):
    if n == max(valores):
        print(f'O maior valor digitado foi {n} nas posições {pos} ...')
    if n == min(valores):
        print(f'O menor valor digitado foi {n} nas posições {pos} ...')



