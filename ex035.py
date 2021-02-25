#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

t1 = float(input('\033[31mDigite o valor da primeira reta: '))
t2 = float(input('\033[31mDigite o valor da segunda reta: '))
t3 = float(input('\033[31mDigite o valor da terceira reta: '))

if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('\033[33mOs valores acima podem formar um triângulo! ')
else:
    print('\033[33mOs valores não podem formar um triângulo! ')
