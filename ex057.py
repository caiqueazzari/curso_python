'''Faça um programa que leia o sexo de uma pessoa, mas só aceite valores 'M' ou 'F' caso esteja errado,
peça a digitação novamente até ter um valor correto.'''

sexo = str(input('Digite o seu sexo: (M/F) ')).strip().upper()

while sexo not in 'MF':
    print('Dados inválidos! ')
    sexo = str(input('Digite o seu sexo: (M/F) ')).strip().upper()

print(f'Sexo {sexo} registrado com sucesso.')
