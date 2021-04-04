'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

dados = dict()
gols = list()

dados['Nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))

for x in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {x}? ')))

dados['Gols'] = gols[:]
dados['Total'] = sum(gols)

print('-' * 60)
print(dados)
print('-' * 60)

for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')

print('-' * 60)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')

for i, v in enumerate(dados['Gols']):
    print(f'\tNa partida {i}, fez {v} gols.')
print(f'Um total de {dados["Total"]} gols')