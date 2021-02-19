'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

Considere:
US$1,00 = RS$5,43
'''

money = float(input('Quanto dinheiro você tem na carteira neste momento? R$'))
print(f'\nConsiderando que US$1,00 equivale a RS$3,27, você pode comprar US${money / 5.43:.3}.')
