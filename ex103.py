'''
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que
algum dado não tenha sido informado corretamente.
'''


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} marcou {gols} gol(s).')


jogador = str(input('Digite o nome do jogador: ')).strip().upper()
n = str(input('Quantidade de gols: '))

if n.isnumeric():
    n = int(n)
else:
    n = 0

if jogador == '':
    ficha(gols=n)
else:
    ficha(jogador, n)
