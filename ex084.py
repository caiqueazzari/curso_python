'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
Quantas pessoas foram cadastradas.
Uma listagem com as pessoas mais pesadas.
Uma listagem com as pessoas mais leves.
'''

print('{:^30}'.format('Cadastro de pessoas'))

dados, lista, leve, pesado, resp = [], [], 0, 0, ' '

while resp != 'N':
    resp = ' '
    dados.append(str(input('Digite o nome: ')).strip().title())
    dados.append(float(input('Digite o peso: ')))

    if len(lista) == 0:
        leve = pesado = dados[1]
    else:
        if dados[1] < leve:
            leve = dados[1]
        elif dados[1] > pesado:
            pesado = dados[1]

    lista.append(dados[:])
    dados.clear()

    while resp not in 'SN':
        resp = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]

print(f'O total de pessoas cadastradas foi de: {len(lista)}.')
print(f'O maior peso cadastrado foi {pesado}. Peso de ', end='')
for x in lista:
    if x[1] == pesado:
        print(x[0], end=' ')

print(f'\nO menor peso cadastrado foi {leve}. Peso de ', end='')
for x in lista:
    if x[1] == leve:
        print(x[0], end=' ')
