#Crie um jogo que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint

print('\033[34m=*=' * 10)
print('\t\t\t\033[1;38mJokenpô')
print('\033[34m=*=' * 10)
print('\033[mBem-vindo ao jogo! Você jogará contra mim, o seu computador!')
p = int(input('Faça a sua escolha!'
                '\n\t 1 - Pedra'
                '\n\t 2 - Papel'
                '\n\t 3 - Tesoura'
                '\nDigite a sua escolha: '))
pc = randint(1, 3)
print('Processando..')
sleep(2)

if p == pc:
    print('Empate!')
elif p == 2 and pc == 1 or p == 1 and pc == 3 or p == 3 and pc == 2:
    print('Droga! Você ganhou..')
elif pc == 2 and p == 1 or pc == 1 and p == 3 or pc == 3 and p == 2:
    print('Eu ganhei! HAHAHAHA!')
