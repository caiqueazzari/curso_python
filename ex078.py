'''
Faça um programa que leia 5 valores e guarde os em uma lista.

No final, mostre qual foi o maior e o menor valor digitado, e as suas respectivas posições na lista.
'''

valores, posMaior, posMenor = list(), list(), list()

for x in range(0, 5):
    valores.append(int(input(f'Digite o valor da poisição {x}: ')))

for c, x in enumerate(valores):
    if x == max(valores):
        posMaior.append(c)
    if x == min(valores):
        posMenor.append(c)

print(f'\nVocê digitou os valores {valores}')
print(f'\nO maior valor digitado foi {max(valores)} nas posições {posMaior}')
print(f'\nO menor valor digitado foi {min(valores)} nas posições {posMenor}')