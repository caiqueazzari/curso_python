'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''

dados = dict()

dados['Nome'] = str(input('Nome: ')).strip().title()
dados['Média'] = float(input(f'Média de {dados["Nome"]}: '))

if dados['Média'] < 7:
    dados['Situação'] = 'Reprovado'
elif dados['Média'] >= 7:
    dados['Situação'] = 'Aprovado'

for k, v in dados.items():
    print(f'{k} é igual a {v}.')