'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
'''

valores = list()
resp = ' '
while resp != 'N':

    resp = ' '
    num = int(input('Digite um número: '))

    if num not in valores:
        valores.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor já digitado, não adicionarei novamente..')

    while resp not in 'SN':
        resp = str(input('Deseja digitar mais números? (S/N) ')).strip().upper()[0]

print(f'Valores digitados: {sorted(valores)}')