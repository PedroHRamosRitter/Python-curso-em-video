# n = int(input('Digite um número: '))
# if n % 2 == 0 and n != 2:
#     print('Número não é primo')
# elif n % 2 == 1:
#     print('O número é primo')


n = int(input('Digite um número:'))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, total))
if total == 2:
    print('Por isso ele é PRIMO!')
else:
    print('Por isso ele não é PRIMO!')