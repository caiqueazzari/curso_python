'''
Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como
um valor monetário formatado.
'''

from moeda import *

valor = float(input('Digite um preço: R$'))
print(f'Com um aumento de 10%, temos {monetário(aumentar(valor, 10))}')
print(f'Com um desconto de 13%, temos {monetário(diminuir(valor, 13))}')
print(f'O dobro de {monetário(valor)} é {monetário(dobro(valor))}')
print(f'A metade de {monetário(valor)} é de {monetário(metade(valor))}')
