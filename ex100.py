'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma
entre todos os valores pares sorteados pela função anterior.
'''

from random import randint
from time import sleep

num = []


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for x in range(0, 5):
        lista.append(randint(1, 10))
        print(num[x], end=' ')
        sleep(0.5)
    print('Pronto!')


def somaPar(lista):
    soma = 0
    for x in num:
        if x % 2 == 0:
            soma += x
    print(f'Somando os valores pares de {num}, temos {soma}.')

sorteia(num)
somaPar(num)

