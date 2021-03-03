#Crie um jogo que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint

escolhas = ('Pedra', 'Papel', 'Tesoura')

print('\033[34m=*=' * 10)
print('\t\t\t\033[1;38mJokenpô')
print('\033[34m=*=' * 10)
print('\033[mBem-vindo!')
p = int(input('Faça a sua escolha!'
                '\n\t 1 - Pedra'
                '\n\t 2 - Papel'
                '\n\t 3 - Tesoura'
                '\nDigite a sua escolha: ')) - 1
pc = randint(0, 2)
print('Processando..')
sleep(2)
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Pô!!!')

print('-=' * 15)
print(f'O computador escolheu {escolhas[pc]}')
print(f'O jogador escolheu {escolhas[p]}')
print('-=' * 15)
print('Resultado: ')

if p == pc:
    print('\033[1mEmpate!')
elif p == 1 and pc == 0 or p == 0 and pc == 2 or p == 2 and pc == 1:
    print('\033[1mO jogador ganhou!')
elif pc == 1 and p == 0 or pc == 0 and p == 2 or pc == 2 and p == 1:
    print('\033[1mO computador ganhou!')
