'''Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer.'''

from random import randint
from time import sleep


print('\033[31m=*=' * 8)
print('|\t\t\033[1;38mJo ken pô\033[31m\t   |')
print('=*=' * 8)
print('\n\033[38mJogador, faça sua escolha até ganhar do computador! ')

palpite = 0
escolha_certa = ''
escolhas = ['Pedra', 'Tesoura', 'Papel']

while escolha_certa == '':
    jogador = int(input('\n\t\t 1. Pedra '
                        '\n\t\t 2. Tesoura'
                        '\n\t\t 3. Papel'
                        '\n\nQual é a sua escolha? Digite 1,2 ou 3: '))
    print('\nProcessando..')
    sleep(1)
    
    palpite += 1
    computador = randint(1, 3)

    if computador == 1 and jogador == 3 or computador == 2 and jogador == 1 or computador == 3 and jogador == 2:
        print(f'\nO computador jogou \033[36m{escolhas[computador - 1]} \033[38me você jogou \033[36m{escolhas[jogador - 1]}, portanto..')
        print('\n\t\033[1;32mVocê venceu!')
        print(f'\n\033[38mForam necessárias \033[36m{palpite} \033[38mpalpites para você ganhar :)')
        escolha_certa = 'Win'

    elif computador == jogador:
        print(f'\nTanto você como o computador jogaram \033[36m{escolhas[jogador - 1]}\033[38m, houve um \033[31mempate! \033[38mTente novamente..\033[38m\n')

    else:
        print(f'\nO computador jogou \033[36m{escolhas [computador - 1]}\033[38m e você jogou \033[36m{escolhas[jogador - 1]}\033[38m, portanto..')
        print('\n\t \033[31mVocê perdeu!')
        print('\n\033[38mTente novamente! \n')
