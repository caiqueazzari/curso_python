'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = [[], [], []]
par, soma, maior = 0, 0, 0
for x in range(0, 3):
    for y in range(0, 3):
        matriz[x].append(int(input(f'Digite um valor para {x, y}: ')))
        if matriz[x][y] % 2 == 0:
            par += matriz[x][y]
        if y == 2:
            soma += matriz[x][y]
        if x == 0:
            maior = matriz[x][y]
        else:
            if matriz[1][y] > maior:
                maior = matriz[1][y]
print()
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{matriz[x][y]:^5}]', end='')
    print()
print(f'\nA soma dos valores pares é de: {par}')
print(f'A soma dos valores da terceira coluna é de: {soma}')
print(f'O maior valor da segunda linha é {maior}.')
