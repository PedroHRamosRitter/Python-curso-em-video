def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print(f'\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return  0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print(f'\033[1;31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n

# def leiaInt(msg):
#     valido = False
#     while not valido:
#         try:
#             n = str(input(msg)).strip()
#             n.isnumeric()
#             valido = True
#             return int(n)
#         except(ValueError, TypeError):
#             print(f'\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
#             valido = False
#             continue # O continue vai voltar neste caso para o while de novo para refazer a pergunta
#
#
#         except KeyboardInterrupt:
#             print(f'\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
#             valido = True
#             n = 0
#             return int(n)
#         except:
#             print(f'\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
#             valido = False
#
#         # Também poderia usar
#         # else:
#         #   return n
#
#         if valido:
#             break
#
#
# def leiaFloat(msg):
#     valido = False
#     while not valido:
#         try:
#             n = str(input(msg)).replace(',', '.').strip()
#             n.isdecimal()
#             valido = True
#             return float(n)
#
#         except(ValueError, TypeError):
#             print(f'\033[1;31mERRO: por favor, digite um número real válido. \033[m')
#             valido = False
#             continue
#
#         except KeyboardInterrupt:
#             print(f'\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
#             valido = True
#             n = 0
#             return float(n)
#         except:
#             print(f'\033[0;31mERRO: por favor, digite um número real válido.\033[m')
#             valido = False
#
#         # Também poderia usar
#         # else:
#         #   return n
#
#         if valido:
#             break