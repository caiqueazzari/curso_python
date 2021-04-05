'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e
todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

dados = dict()
lista = list()
resp = ' '
totIdade, a = 0, 0

while resp != 'N':
    dados['nome'] = str(input('Nome: ')).strip().title()
    while True:
        dados['sexo'] = str(input('Sexo: (M/F) ')).strip().upper()[0]
        if dados['sexo'] not in 'MF':
            print('Opção inválida! Digite apenas M ou F..')
        else:
            break
    dados['idade'] = int(input('Idade: '))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
    lista.append(dados.copy())
    dados.clear()

print(f'\nTotal de pessoas cadastradas: {len(lista)}')

for i, v in enumerate(lista):
    totIdade += v['idade']
media = totIdade / len(lista)
print(f'\nA média de idade foi de: {media:.2f}')

print('\nAs mulheres cadastradas foram: ', end='')
for v in lista:
    if v['sexo'] == 'F':
        print(f'{v["nome"]} ', end='')
        a = 1
if a == 0:
    print('Nenhuma', end='')

print('\n\nLista das pessoas que estão acima da média: ')
for x in lista:
    if x['idade'] > media:
        print('\n      ', end='')
        for k, v in v.items():
            print(f'{k} = {v}; ', end='')
            a = 2
if a != 2:
    print('\nNenhuma', end='')
print('\n\nFIM!')