'''Faça um programa que leia o sexo de uma pessoa, mas só aceite valores 'M' ou 'F' caso esteja errado,
peça a digitação novamente até ter um valor correto.'''

sexo = ''

while sexo == '':

    escolha = str(input('Digite o seu sexo: (M/F) ')).upper()
    if escolha == 'M' or escolha == 'F':
        sexo = escolha

print('Fim')
