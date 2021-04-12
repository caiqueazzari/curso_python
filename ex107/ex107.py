'''
Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.
'''

from moeda import aumentar, diminuir, dobro, metade

valor = float(input('Digite um preço: R$'))
print(f'Com um aumento de 10%, temos R${aumentar(valor, 10):.2f}')
print(f'Com um desconto de 13%, temos R${diminuir(valor, 13):.2f}')
print(f'O dobro de R${valor:.2f} é R${dobro(valor):.2f}')
print(f'A metade de R${valor:.2f} é de R${metade(valor):.2f}')
