#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite uma temperatura em ºC: '))
f = (c*1.8) + 32
print(f'A temperatura {c:.1f}ºC equivale a {f:.1f}ºF.')
