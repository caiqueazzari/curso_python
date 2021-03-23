'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Corinthians.
'''

times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 
         'Bragantino', 'Ceará SC', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco da Gama', 'Goiás',
         'Coritiba', 'Botafogo')

print('\nOs primeiros colocados são: \n')

for x in range(0, 5):
    print(x + 1, times[x])

print('\nOs últimos 4 colocados da tabela são: \n')

for x in range(15, 20):
    print(x + 1, times[x])

print('\nOs times em ordem Alfabética: \n')

ordem = sorted(times)

for x in range(0, 20):
    print(ordem[x])

print(f'\nO Corinthians está na {times.index("Corinthians")}° posição.')
