'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep
sorteio = []
print('-' * 60)
print(f'{"Sorteador de números da MEGA SENA":^60}')
print('-' * 60)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'\nSorteando {jogos} jogos..\n')
sleep(1)
for x in range(0, jogos):
    for y in range(0, 6):
        num = randint(1, 60)
        if num not in sorteio:
            sorteio.append(num)
    print(f'Jogo {x + 1}: {sorteio}')
    sorteio.clear()
    sleep(1)
print('\nBoa sorte!')