from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'dados.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    cabecalho('MENU PRINCIPAL')
    menuResposta(1, 'Ver pessoas cadastradas', 2, 'Cadastrar nova pessoas', 3, 'Sair do Sistema')

    opcao = leiaInt('\033[1;33mSua Opção: \033[m')
    if opcao == 1:
        cabecalho('PESSOAS CADASTRADAS')
        lerArquivo(arq)

    elif opcao == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif opcao == 3:
        break
    else:
        print(f'\033[1;31mERRO! Digite uma opção válida!\033[m')
    sleep(1)
sleep(0.5)
print(f'\033[1;31mSaindo do sistema... Até logo!\033[m')
