'''
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
'''

valores = tuple(int(input(f'\nDigite o {x + 1}° valor: '))for x in range(0, 5))

print('\nVocê digitou os valores: ', end='')
for x in range(0, 5):
    print(valores[x], '- ' if x < 4 else f'', end='')

contador = valores.count(9)

if contador > 1:
    print(f'\n\nO valor 9 apareceu {valores.count(9)} vezes.')
elif contador == 1:
    print('\n\nO valor 9 apareceu 1 vez.')
else:
    print('\n\nO valor 9 não apareceu nenhuma vez.')

if 3 in valores:
    print(f'\nO valor 3 apareceu pela primeira vez na {valores.index(3) + 1}° posição.')
else:
    print('\nO valor 3 não apareceu nenhuma vez.')

countPar = 0

for x in valores:
    if x % 2 == 0:
        countPar += 1
        par = x

if countPar >= 1:
    if countPar == 1:
        print(f'\nO único número par lido foi o {par}.')
    if countPar > 1:
        print(f'\nOs números pares digitados foram: ', end='')
        for x in valores:
            if x % 2 == 0:
                print(f'{x} ', end='')
print()
