'''Crie um programa que leia dois valores e mostre em um menu na tela:

[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''

sair = ''
num = []

for x in range(0, 2):
    num.append(int(input(f'Digite o \033[36m{x + 1}º \033[38mvalor inteiro: ')))

print('\nO que você deseja fazer com os números? ')

while sair != 'sair':
    escolha = int(input('\n\t[1] Somar os números'
                        '\n\t[2] Multiplicar os números'
                        '\n\t[3] Achar qual é o maior'
                        '\n\t[4] Escolher novos números'
                        '\n\t[5] Sair do programa'
                        '\n\nEscolha uma das opções: '))

    if escolha == 1:
        print(f'\nA soma dos números \033[36m{num[0]} \033[38me \033[36m{num[1]} \033[38mé de \033[36m{num[0] + num[1]}'
              f'\033[38m.')
        print('\n\033[1;38mO que você deseja fazer com os números agora? \033[0;38m')
    elif escolha == 2:
        print(f'\nA multiplicação dos números \033[36m{num[0]} \033[38me \033[36m{num[1]} \033[38mé de \033[36m'
              f'{num[0] * num[1]}\033[38m.')
        print('\n\033[1;38mO que você deseja fazer com os números agora? \033[0;38m')
    elif escolha == 3:
        print(f'\nO maior número digitado é o \033[36m{max(num)}\033[38m.')
        print('\n\033[1;38mO que você deseja fazer com os números agora? \033[0;38m')
    elif escolha == 4:
        print('')
        num = []
        for x in range(0, 2):
            num.append(int(input(f'Digite o \033[36m{x + 1}º \033[38mvalor inteiro: ')))
    elif escolha == 5:
        print('\nSaindo... :)')
        sair = 'sair'
    else:
        print('\n\033[1;38mEscolha inválida, digite uma escolha válida!!\033[0;38m')
