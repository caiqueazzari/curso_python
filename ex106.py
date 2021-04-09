'''
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
OBS: Use cores
'''

from time import sleep
from random import randint

c = ('\033[m',          # 0 - sem cor
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[7;30m'       # 6 - branco
     )


def escreva(msg, cor=0):
    print(c[cor], end='')
    print('~' * (len(msg) + 4))
    print(f'  {msg}  ')
    print('~' * (len(msg) + 4))
    print(c[0], end='')

while True:
    escreva('Sistema de ajuda PYHELP', randint(1, 6))
    escolha = str(input('Função ou biblioteca > ')).strip()
    if escolha.upper() == 'FIM':
        escreva('Até logo!', randint(1, 6))
        break
    escreva(f'Acessando o manual do comando {escolha}', randint(1, 6))
    sleep(1)
    print(c[randint(1, 6)])
    help(escolha)
    print(randint(1, 6))
