'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while.'''

print('Calculo de progressão aritmética! ')
n1 = int(input('Digite o 1º termo da PA: '))
r = int(input('Digite a razão da PA: '))
x = 0
print('PA: ', end='')

while x < 10:
    print(f'{n1 + (x * r)}', ' > ' if x <= 8 else '', end='')
    x += 1
