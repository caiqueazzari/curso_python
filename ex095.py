'''
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

jogador = {}
time = []
gols = []
dados = 0

while True:
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for x in range(1, partidas + 1):
        gols.append(int(input(f'\tQuantos gols na {x}º partida? ')))
    jogador['gols'] = gols[:]
    jogador['Total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S e N meu filho..')
    if resp == 'N':
        break
print('-' * 45)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while dados != 999:
    print('-' * 45)
    dados = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if dados == 999:
        print('\nSaindo..')
        break
    if dados >= len(time):
        print('Jogador não cadastrado!')
    else:
        print(f' -- Levantamento do jogador {time[dados]["nome"]}')
        for i, g in enumerate(time[dados]['gols']):
            print(f'\tNa partida {i + 1}, fez {g} gols.')
