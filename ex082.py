'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

valores, par, impar, resp, x = list(), list(), list(), ' ', 0

while resp != 'N':
    resp = ' '
    valores.append(int(input('Digite um valor: ')))
    if valores[x] % 2 == 0:
        par.append(valores[x])
    else:
        impar.append(valores[x])
    while resp not in 'SN':
        resp = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
    x += 1

print(f'Valores digitados: {valores}')
print(f'Valores pares digitados: {par}')
print(f'Valores impares digitados: {impar}')
