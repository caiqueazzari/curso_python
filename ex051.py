#Desenvolva um programa que leia o primeiro termo e a razão de um PA. No final, mostre os 10 primeiros termos dessa progressão.

print('Calculo de progressão aritmética! ')
n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

a10 = n1 + (10 - 1) * r

for x in range(n1, a10 + 1, r):
    print(x)

