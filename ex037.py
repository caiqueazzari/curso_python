  '''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal'''

from time import sleep

num = int(input('Digite um número inteiro: '))
base = int(input(''
                 '\t - 1 para binário'
                 '\n\t - 2 para octal'
                 '\n\t - 3 para hexadecimal'
                 '\nEscolha a base de conversão: '))
print('Processando...')
sleep(3)

if base == 1:
    print(f'A conversão do número {num} em binário é: {bin(num)}')
elif base == 2:
    print(f'A conversão do número {num} em octal é: {oct(num)}')
elif base == 3:
    print(f'A conversão do número {num} em hexadecimal é: {hex(num)}')
else:
    print('Número inválido!')
