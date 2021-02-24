'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200km e R$ 0,45 para viagens mais longas'''

from time import sleep

viagem = float(input('Qual foi a distância da viagem em km? '))
print('Processando..')
sleep(3)

if viagem <= 200:
    topay = viagem * 0.50
    print(f'O preço a se pagar pela viagem é de R${topay:.2f}.')
elif viagem >= 201:
    topay = viagem * 0.45
    print(f'O preço a se pagar pela viagem é de R${topay:.2f}.')
else:
    print('Informação inválida!')
