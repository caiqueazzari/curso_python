'''Escreve um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random
from time import sleep

num = random.randint(0, 5)

print("Jogo da adivinhação!")

choice = int(input('Digite um número de 0 a 5: '))

print('Processando...')
sleep(2)

if choice == num:
    print(f'Você acertou! O número escolhido pelo computador foi {num}!')
else:
    print(f'Você errou! O número escolhido pelo computador foi {num}!')
