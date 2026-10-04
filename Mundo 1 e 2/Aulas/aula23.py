# Tratemento de erros e eeceções

# print(x)

# n = int(input('Número: '))
# print(f'Você digitou o número {n}  ')

# a = int(input('Numerador: '))
# b = int(input('Denominador: '))
# r = a / b
# print(f'O resultado é {r}')

# r = 2 / '2'
# print(R)

# lst = [3, 6, 4]
# # print(lst[3]) -> elementos 0, 1, 2  -> [3] -> indexError quando é dicionário é key error

# import uteis ->  ModuleNotFoundError -> Não encontrado


# Exception = exceção

# try = tente (operação)
# except = Se não acontece uma exceção (falhou)
# else = Caso der certo mostrar o que ...
# finally = se der certo ou errado mostrar o que ...

# except = pode ter varios except no try

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except Exception as erro: # Exception as erro no
#     print(f'\033[0;31mO problema econtrado foi {erro.__class__}\033[m')
# else:
#     print(f'\033[0;32mO resultado é {r:.2f}\033[m')
# finally:
#     print('\033[1;97mVolte sempre! Muito obrigado!\033[m')


try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print(f'\033[0;31mTivemos um problema com os tipos de dados que você digitou.\033[m')
except ZeroDivisionError:
    print(f'\033[0;31mNão e possível dividir um número por zero!\033[m')
except KeyboardInterrupt:
    print(f'\033[0;31mO usuário preferiu não informar os dados!\033[m')
except Exception as erro:
    print(f'\033[1;31mO erro encontrado foi {erro.__cause__}\033[m')
else:
    print(f'\033[0;32mO resultado é {r:.2f}\033[m')
finally:
    print(f'\033[1;97mVolte sempre! Muito obrigado!\033[m')