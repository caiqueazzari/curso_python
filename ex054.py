#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maiores_de_idade = 0
menores_de_idade = 0

for x in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {x}º pessoa: '))
    if date.today().year - ano >= 18:
        maiores_de_idade += 1
    elif date.today().year - ano < 18:
        menores_de_idade += 1

print(f'\nA quantidade de pessoas que atingiram a maioridade é de {maiores_de_idade}.')
print(f'A quantidade de pessoas que ainda são menores de idade é de {menores_de_idade}.')
