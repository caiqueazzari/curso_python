'''Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer.'''

from random import randint
from time import sleep
print('=*=' * 10)
print('|\t\033[31m  Jogo da adivinhação!\033[38m\t |')
print('=*=' * 10, '\n')
print('O computador irá pensar em um número de 0 a 10, tente adivinhar qual ele pensou! \n')

computador = randint(0, 11)
escolha = ''
palpites = 0

while escolha != computador:

    escolha = int(input('\033[38mDigite um número de 0 a 10: '))
    computador = randint(0, 10)
    print('\nProcessando...')
    sleep(1)
    palpites += 1

    if escolha == computador:
        print(f'\nVocê acertou o número que o computador estava pensando! (\033[1;36m{escolha}\033[0;38m)')
        print('\n\t\033[32mParabéns!')
        if palpites == 1:
            print(f'\n \033[38mFoi necessário apenas \033[36m1 \033[38mpalpite para você vencer!')
        else:
            print(f'\n \033[38mForam necessários \033[36m{palpites} \033[38mpalpites para você vencer vencer!')
    else:
        print(f'\nO computador pensou no número \033[1;36m{computador}\033[0;38m, portanto você errou!\n\n\t\033[31mTente novamente!\n')
