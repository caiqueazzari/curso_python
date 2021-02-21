#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

name = str(input('Digite um nome: '))
list = name.upper().split()

print('Analisando o nome...')

if "SILVA" in list:
    print(f'Você possuí "Silva" no nome!')
else:
    print(f'Você não possuí "Silva" no nome!')
