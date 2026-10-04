def fatorial(n, show=False):
    """
    -> Calcula o atorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            if c == 1:
                print(' = ', end='')
    return f
# Programa Principal
print('-=' * 20)
num = int(input('Digite um número: '))
mostrar = str(input('Quer mostrar o processo de fatoração [S/N]: ')).strip()[0]
if mostrar not in 'SsNn':
    while True:
        print('Digite apena S ou N.', end=' ')
        mostrar = str(input('Tente novamente: ')).strip()[0]
        if mostrar in 'SsNn':
            break
if mostrar in 'Ss':
    mostrar = True
elif mostrar in 'Nn':
    mostrar = False
print(fatorial(num, show=mostrar))