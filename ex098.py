'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''

from time import sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
        print('O passo não pode ser igual a zero.. Alterado para 1!! Atente-se da próxima vez!')
    print('-' * 40)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if i < f:
        while i <= f:
            print(i, end=' ')
            sleep(0.5)
            i += p
    elif i > f:
        while i >= f:
            print(i, end=' ')
            sleep(0.5)
            i -= p
    print('Fim!')


contador(0, 10, 1)
contador(10, 0, 2)
print('-' * 40)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
