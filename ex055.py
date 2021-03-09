#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

menor = 0
maior = 0

for x in range(1, 6):
    peso = float(input(f'Digite o peso da {x}º pessoa: '))
    if x == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O maior peso foi de {maior:.1f}kg \nO menor foi de {menor:.1f}kg')
