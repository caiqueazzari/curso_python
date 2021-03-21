'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
o usuário quer ou não continuar. No final, mostre:

A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.
'''

print('-=' * 20)
print('Cadastro de pessoas')
print('-=' * 20)
pessoa, cont_maiordeIdade, cont_mulher, cont_homem = 0, 0, 0, 0

while True:
    pessoa += 1
    idade = int(input(f'\nDigite a \033[1;36midade \033[0;38mda \033[1;36m{pessoa}° \033[0;38mpessoa: '))
    sexo = str(input(f'Digite o \033[1;36msexo \033[0;38mda \033[1;36m{pessoa}° \033[0;38mpessoa (M/F): ')).strip().upper()[0]

    if idade >= 18:
        cont_maiordeIdade += 1

    if sexo == 'F' and idade < 20:
        cont_mulher += 1

    if sexo == 'M':
        cont_homem += 1

    continuar = str(input('\nDeseja continuar cadastrando (S/N)? ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'\nCom base nas pessoas cadastradas: \n')
print(f'{cont_maiordeIdade} pessoas são maiores de idade.')
print(f'{cont_homem} homens foram cadastrados.')
print(f'{cont_mulher} mulheres tem menos de 20 anos.')
