expressao = input('Digite a expressão: ')
pilha = list()
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        elif len(pilha) == 0:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('A expressão é válida!')
else:
    print('A espressão é inválida!')