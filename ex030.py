#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

from time import sleep

num = int(input('Digite um número inteiro: '))
print('Processando...')
sleep(3)

if num % 2 == 0:
    print(f'O número {num} é par!')
else:
    print(f'O número {num} é ímpar!')
