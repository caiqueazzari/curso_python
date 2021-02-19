#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

an = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print(f'O ângulo {an:.2f} tem o seno de {sen:.2f}, cosseno de {cos:.2f} e tangente de {tan:.2f}.')
