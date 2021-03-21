'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivar que ele conquistou no final do jogo.
'''

from random import randint
from time import sleep

print('-=' * 30)
jogo = str('Par ou ímpar')
print(f'{jogo:^60}')
print('-=' * 30)
consec = 0

while True:
    num_p = int(input('\nDigite um valor: '))
    escolha_p = ' '
    while escolha_p not in 'PIÍ':
        escolha_p = str(input('\nPar ou Impar? ')).strip().upper()[0]
    print('\nProcessando..')
    sleep(2)
    num_c = randint(1, 10)
    resultado = (num_c + num_p) % 2
    print(f'\nSeu número: {num_p}\n\nNúmero do computador: {num_c} ', end='')
    print(f'\n\n{num_p} + {num_c} = {num_c + num_p} = Par. ' if resultado == 0
          else f'\n\n{num_p} + {num_c} = {num_c + num_p} = Ímpar.')

    if escolha_p == 'I' or escolha_p == 'Í':
        if resultado == 1:
            print(f'\n\033[1;32mVocê ganhou!\033[0;38m ')
        else:
            print('\n\033[1;31mVocê perdeu!\033[0;38m \n')
            break
    elif escolha_p == 'P':
        if resultado == 0:
            print(f'\n\033[1;32mVocê ganhou!\033[0;38m ')
        else:
            print(f'\n\033[1;31mVocê perdeu! \033[0;38m\n')
            break

    consec += 1

if consec > 1:
    print('-=' * 30)
    print(f'Você ganhou \033[1;36m{consec} \033[0;38mvezes consecutivas! Parabéns!')
    print('-=' * 30)
elif consec == 1:
    print('-=' * 30)
    print(f'Você ganhou \033[1;36m1 \033[0;38mvez! Parabéns!')
    print('-=' * 30)
