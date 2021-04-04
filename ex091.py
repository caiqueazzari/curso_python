'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep

sorteado = dict()
lista = list()

print('\nValores sorteados: ')
sleep(1)
for x in range(1, 5):
    sorteado[f'Jogador {x}'] = randint(1, 6)
for x, y in sorteado.items():
    print(f'O {x} tirou {y}.')
    sleep(1)

print('\nRanking dos jogadores: ')
lugar = 0
for x in sorted(sorteado.values(), reverse=True):
    for k, v in sorteado.items():
        if k in lista:
            continue
        if x == v:
            lugar += 1
            print(f'{lugar}° lugar: {k} com {v}')
            sleep(1)
            lista.append(k)
