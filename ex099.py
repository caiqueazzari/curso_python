'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

from time import sleep


def maior(* num):
    m = 0
    print('-' * 40)
    print('Analisando os valores passados..')
    for x, y in enumerate(num):
        if x == 0:
            m = y
        else:
            if y > m:
                m = y
        print(y, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {m}')


maior(1, 3, 4, 5, 7, 8)
maior(3, 4, 5)
maior(2, 3)
maior(9)
maior()