'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))
topay = (0.15 * km) + (60 * dias)
print(f'O preço total a se pagar é de R${topay:.2f}.')
