#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número inteiro: '))
y = 0
s = 0

for x in range(n):
    y += 1
    if n != 1 and n % y == 0:
        s += 1

if s == 2:
    print(f'O número {n} é primo!')
else:
    print(f'O número {n} NÃO é primo!')
