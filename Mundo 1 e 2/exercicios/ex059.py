from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar 
    [ 3 ] Maior
    [ 4 ] Novos números 
    [ 5 ] Sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))

    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção == 2:
        produto =  n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            print('Entre {} e {] o maior valor é {}'.format(n1, n2, n1))
        elif n1 < n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))
        else:
            print('Entre {} e {} os dois valores são iguais'.format(n1, n2))
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
#Caso queira usar str no opcao voce coloca while opção != '5': que vai dar certo usando o str






# n1 = int(input('Digite o primeiro número: '))
# n2 = int(input('Digite o segundo número: '))
#
# print('''Você tem as seguintes opções:
#     [ 1 ] somar
#     [ 2 ] multiplicar
#     [ 3 ] maior
#     [ 4 ] novos números
#     [ 5 ] sair do programa''')
#
# opcao = int(input('Qual opção você deseja: '))
#
# while opcao > 5 or opcao < 1:
#     print('Número inválido tente novemente')
#     n1 = int(input('Digite o primeiro número: '))
#     n2 = int(input('Digite o segundo número: '))
#
#     print('''Você tem as seguintes opções:
#         [ 1 ] somar
#         [ 2 ] multiplicar
#         [ 3 ] maior
#         [ 4 ] novos números
#         [ 5 ] sair do programa''')
#
#     opcao = int(input('Qual opção você deseja: '))
#
# if opcao == 1:
#     print('A soma de {} mais {} é igual a {}'.format(n1, n2, n1 + n2))
# elif opcao == 2:
#     print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, n1 * n2))
# elif opcao == 3:
#     if n1 > n2:
#         print('O maior valor é {}'.format(n1))
#     elif n2 > n1:
#         print('O maior valor é {}'.format(n2))
#     else:
#         print('Os dois valores são iguais')
# while opcao == 4:
#     n1 = int(input('Digite o primeiro número: '))
#     n2 = int(input('Digite o segundo número: '))
#     print('''Você tem as seguintes opções:
#         [ 1 ] somar
#         [ 2 ] multiplicar
#         [ 3 ] maior
#         [ 4 ] novos números
#         [ 5 ] sair do programa''')
#     opcao = int(input('Qual opção você deseja: '))
#     if opcao == 1:
#         print('A soma de {} mais {} é igual a {}'.format(n1, n2, n1 + n2))
#     elif opcao == 2:
#         print('A multiplicação entre {} e {} é igual a {}'.format(n1, n2, n1 * n2))
#     elif opcao == 3:
#         if n1 > n2:
#             print('O maior valor é {}'.format(n1))
#         elif n2 > n1:
#             print('O maior valor é {}'.format(n2))
#         else:
#             print('Os dois valores são iguais')
# else:
#     print('Fim do programa')
