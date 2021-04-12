'''
Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como
um valor monetário formatado.
'''

from moeda import *

valor = float(input('Digite um preço: R$'))
print(f'Com um aumento de 10%, temos {aumentar(valor, 10, True)}')
print(f'Com um desconto de 13%, temos {diminuir(valor, 13, True)}')
print(f'O dobro de {monetário(valor)} é {dobro(valor, True)}')
print(f'A metade de {monetário(valor)} é de {metade(valor, True)}')
