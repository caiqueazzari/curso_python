def leiaDinheiro(msg):
    while True:
        valor = str(input(msg)).strip().replace(',', '.')
        if valor.isalpha() or valor == '':
            print(f'\033[31m"{valor}" não é um valor válido! Tente novamente..\033[m')
        else:
            return float(valor)
