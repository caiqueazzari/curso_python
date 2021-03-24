'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint

lista = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print(f'\nLista: ', end='')
for x in range(0, 5):
    print(lista[x], end=', ' if x < 4 else '.')
print(f'\n\nMaior número: {max(lista)}.\n\nMenor número: {min(lista)}.')
