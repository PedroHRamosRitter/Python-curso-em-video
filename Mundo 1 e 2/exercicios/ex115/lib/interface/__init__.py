def lin():
    print('-' * 50)

def cabecalho(txt):
    # print(f'{txt}'.center(50))
    lin()
    print(f'{txt:^50}')
    lin()

def menuResposta(n1, msg1, n2, msg2, n3, msg3):
    print(f'\033[1;33m{n1}\033[m - \033[1;34m{msg1}\033[m')
    print(f'\033[1;33m{n2}\033[m - \033[1;34m{msg2}\033[m')
    print(f'\033[1;33m{n3}\033[m - \033[1;34m{msg3}\033[m')
    lin()
def leiaInt(msg):
    while True:
        try:
            return int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO! Digite um número inteiro válido.\033[m')
