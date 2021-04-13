def cores(num):
    c = ('\033[0m',  # 0 - sem cor
         '\033[1;31m',  # 1 - vermelho
         '\033[1;32m',  # 2 - verde
         '\033[1;33m',  # 3 - amarelo
         '\033[1;34m',  # 4 - azul
         '\033[1;35m',  # 5 - roxo
         '\033[1;38m'  # 6 - branco
         )
    return c[num]


def linha(tam=50):
    print('-' * tam)


def cabeçalho(msg, tam=50, cor=0):
    linha()
    print(f'{cores(cor)}{msg:^{tam}}{cores(0)}')
    linha()


def menu(lst):
    while True:
        cabeçalho('Menu principal', cor=1)
        c = 1
        for x in lst:
            print(f'{cores(6)}{c} - {cores(4)}{x}')
            c += 1
        linha()
        while True:
            try:
                escolha = int(input(f'{cores(3)}Digite uma opção: \033[0m'))
                if escolha <= 0 or escolha > len(lst):
                    print(f'{cores(1)}Digite uma opção válida! ')
                    continue
            except (ValueError, TypeError):
                print(f'{cores(1)}Digite uma opção válida! ')
            else:
                break
        if 0 < escolha < len(lst):
            cabeçalho(f'{f"Opção {escolha}"}', cor=4)
        else:
            cabeçalho(f'{"Saindo :("}', cor=1)
            break
        return escolha