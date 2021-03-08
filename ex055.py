#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

peso = []

for x in range(1, 6):
    peso.append(float(input(f'Digite o peso da {x}º pessoa: ')))

peso = sorted(peso)
print(f'O maior peso foi de {peso[0]} e o menor foi de {peso[4]}')
