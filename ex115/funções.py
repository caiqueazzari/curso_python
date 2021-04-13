def menu():
    while True:
        print('-' * 50)
        print(f'{"Menu principal":^50}')
        print('-' * 50)
        print(f'\033[1;38m1\033[0m -\033[1;34m Ver menu\033[m')
        print(f'\033[1;38m2\033[0m -\033[1;34m Cadastrar nova comida\033[m')
        print(f'\033[1;38m3\033[0m -\033[1;34m Sair do menu\033[m')
        print('-' * 50)
        while True:
            try:
                escolha = int(input('\033[1;33mDigite uma opção: \033[0m'))
                if escolha <= 0 or escolha > 3:
                    print('\033[31mDigite uma opção válida! ')
                    continue
            except (ValueError, TypeError):
                print('\033[31mDigite uma opção válida! ')
            else:
                break
        print('-' * 50)
        if escolha == 1 or escolha == 2:
            print(f'{f"Opção {escolha}":^50}')
        elif escolha == 3:
            print(f'{"Saindo :(":^50}')
            print('-' * 50)
            break
        print('-' * 50)
