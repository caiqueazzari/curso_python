'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulher tem menos de 20 anos.'''

soma = 0
maior_idade_h = 0
tot_f_menor20 = 0
nome_h = ''
for x in range(1,5):
    nome = str(input(f'Digite o \033[31mnome \033[mda {x}º pessoa: ')).strip()
    idade = int(input(f'Digite a \033[32midade \033[mda {x}º pessoa: '))
    sexo = str(input(f'Digite o \033[33msexo \033[mda {x}º pessoa (M/F): ')).strip().upper()
    print()
    soma += idade

    if sexo == 'M':
        if idade > maior_idade_h:
            maior_idade_h = idade
            nome_h = nome
    elif sexo == 'F':
        if idade < 20:
            tot_f_menor20 += 1

print(f'A média de idade do grupo é de {soma / 4}.')
print(f'O homem mais velho do grupo é o {nome_h.title()} e ele tem {maior_idade_h} anos de idade.')

if tot_f_menor20 >= 1:
    print(f'A quantidade de mulheres com menos de 20 anos é de {tot_f_menor20}.')
else:
    print('Não existem mulheres com menos de 20 anos no grupo.')
