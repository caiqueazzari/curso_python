'''
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
'''

from moeda import *

valor = float(input('Digite um preço: R$'))
print(f'Com um aumento de 10%, temos {aumentar(valor, 10, True)}')
print(f'Com um desconto de 13%, temos {diminuir(valor, 13, True)}')
print(f'O dobro de {monetário(valor)} é {dobro(valor, True)}')
print(f'A metade de {monetário(valor)} é de {metade(valor, True)}')
