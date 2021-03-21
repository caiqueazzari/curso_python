'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a
soma entre eles (desconsiderando o flag.)
'''

s, cont= 0, 0

while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    else:
        s += n
        cont += 1

if cont == 0:
    print('\nVocê não digitou nenhum número.')
elif cont == 1:
    print('\nVocê digitou apenas um número.')
else:
    print(f'\nVocê digitou \033[1;36m{cont} \033[0;38mnúmeros.\nA soma dos números foi de \033[1;36m{s}\033[0;38m.')
