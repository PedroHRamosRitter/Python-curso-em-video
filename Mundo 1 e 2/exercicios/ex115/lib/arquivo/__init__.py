def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # open -> abre um arquivo, rt -> Abri em modo de leitura
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # wt+ o mais para criar e o wt e arquivo de texto # w de write
        a.close()
    except:
        print(f'\033[1;31mHouve um ERRO na criação do arquivo!\033[m')
    else:
        print(f'\033[1;32mArquivo {nome} criado com sucesso!\033[m')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt') # r de ride
    except:
        print(f'\033[1;31mERRO ao ler o arquivo!\033[m')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '') # Tirei quebra de linha por nada para que no print não mostre a linha quebrada
            print(f'{dado[0]:<30} {dado[1]:>12} anos')

    finally:
        a.close()

def cadastrar(arq, nome = '<desconhecido>', idade = 0):
    try:
        a = open(arq, 'at') # a de append t de texto

    except:
        print(f'\033[1.31mHouve um ERRO na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'\033[1;31mHouve um erro na hora de escrever os dados!\033[m')
        else:
            print(f'\033[1;32mNovo registro de {nome} adicionado.\033[m')
            a.close()
