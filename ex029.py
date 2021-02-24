'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

vel = float(input('CET-SP | Digite a velocidade do carro em Km/h: '))

if vel >= 81:
    print('Veículo multado!')
    print(f'Valor da multa R${7 * (vel - 80):.2f}!'.replace('.', ","))
print('Velocidade aceitável.')
