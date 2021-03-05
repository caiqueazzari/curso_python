#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

s = 0 #soma

for x in range(1, 7):
    n = int(input(f'Digite o {x}º número: '))
    if n % 2 == 0:
        s += n

print(f'A soma dos números pares digitados é de: {s}')
