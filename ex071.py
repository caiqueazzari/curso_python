'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$100, R$50, R$20, R$10, R$5, R$2 e R$1.
'''

from time import sleep

print('-=' * 20)
print('{:^40}'.format('Caixa eletrônico'))
print('-=' * 20)

moeda, cedula2, cedula5, cedula10, cedula20, cedula50, cedula100 = 0, 0, 0, 0, 0, 0, 0
saque = float(input('\nCedulas disponíveis:'
                    '\n\nR$100,00'
                    '\nR$50,00'
                    '\nR$20,00'
                    '\nR$10,00'
                    '\nR$5,00'
                    '\nR$2,00'
                    '\nR$1,00'
                    '\n\n\033[1;31m[Atenção! Valor que não for soma das notas acima será perdido!]\033[0;38m'
                    '\n\nQual valor você quer sacar? R$'))
total = saque

while True:

    if saque >= 100:
        cedula100 += 1
        saque -= 100
    elif saque >= 50:
        cedula50 += 1
        saque -= 50
    elif saque >= 20:
        cedula20 += 1
        saque -= 20
    elif saque >= 10:
        cedula10 += 1
        saque -= 10
    elif saque >= 5:
        cedula5 += 1
        saque -= 5
    elif saque >= 2:
        cedula2 += 1
        saque -= 2
    elif saque == 1:
        moeda += 1
        saque -= 1
    else:
        break

print('\nProcessando..')
sleep(2)

print(f'\n\033[1;32mValor sacado:  {total:.2f}\033[0;38m\n')

if cedula100 > 1:
    print(f'{cedula100} celulas de R$100,00')
elif cedula100 == 1:
    print(f'{cedula100} celula de R$100,00')

if cedula50 > 1:
    print(f'{cedula50} celulas de R$50,00')
elif cedula50 == 1:
    print(f'{cedula50} celula de R$50,00')

if cedula20 > 1:
    print(f'{cedula20} celulas de R$20,00')
elif cedula20 == 1:
    print(f'{cedula20} celula de R$20,00')

if cedula10 > 1:
    print(f'{cedula10} celulas de R$10,00')
elif cedula10 == 1:
    print(f'{cedula10} celula de R$10,00')

if cedula5 > 1:
    print(f'{cedula5} celulas de R$5,00')
elif cedula5 == 1:
    print(f'{cedula5} celula de R$5,00')

if cedula2 > 1:
    print(f'{cedula2} celulas de R$2,00')
elif cedula2 == 1:
    print(f'{cedula2} celula de R$2,00')

if moeda == 1:
    print(f'{moeda} moeda de R$1,00')

print('\nVolte sempre! :)')
