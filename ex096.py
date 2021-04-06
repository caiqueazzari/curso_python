'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
'''

branco = '\033[38m'
azul = '\033[34m'


def lin(msg):
    print('-' * 60)
    print(f'{azul}{msg:^60}{branco}')
    print('-' * 60)


def area(l, c):
    a = l * c
    print(f'A área do terreno é de {a}m².')

lin('Cálculo de área de terreno')

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(l=largura, c=comprimento)
