from time import sleep
def lin():
    print('-=' * 20)
# i -> inicio
# f -> fim
# p -> passo
def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    while i <= f:
        print(f'{i} ', end= '')
        i += p
        sleep(0.5)
# Programa Principal
contador(1, 10, 1)
print('FIM!')
lin()

def cont(i, f, p):
    while i >= f:
        print(f'{i} ', end='')
        i -= p
        sleep(0.5)

# Programa Principal
cont(10, 0, 2)
print('FIM!')
lin()
def jogador(i, f, p):
    print('Agora é sua vez de persobalizar a contagem!')
    if p == 0:
        p = 1
    if i <= f:
        while i <= f:
            print(f'{i} ', end = '')
            if p > 0:
                i += p
            elif p < 0:
                i -= p
            sleep(0.5)
    elif i >= f:
        while i >= f:
            print(f'{i} ', end = '')
            if p > 0:
                i -= p
            elif p < 0:
                i += p
            sleep(0.5)
# Programa Principal
jogador(
    int(input('Início: ')),
    int(input('Fim: ')),
    int(input('Passo: '))
)
print('FIM!')
