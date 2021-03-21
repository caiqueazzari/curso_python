'''
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
'''

n = int(input('Qual tabuada você quer ver? '))

while True:
    if n >= 1:
        print('')
        for x in range(0, 11):
            print(f'{n} x {x} = {n * x}')
            x += 1
    elif n < 0:
        print('\nSaindo.. :)')
        break
    else:
        print('\nDigite um número inteiro válido! ')

    n = int(input('\nDeseja ver outra tabuada (Digite um número negativo para sair)? '))
