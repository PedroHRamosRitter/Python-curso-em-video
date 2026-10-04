def leiaDinheiro(msg):
    valido = False
    while not valido:
        p = str(input(msg)).replace(',', '.').strip()
        if p.isalpha() or p == '':
            print(f'\033[0;31mErro: \'{p}\' é um preço inválido.\033[m')
        else:
            valido = True
            return float(p)
        if valido:
            break