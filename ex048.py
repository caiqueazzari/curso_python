#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0

for x in range(1, 501, 2):
    if x % 3 == 0:
        soma += x

print(f'A soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500 é de {soma}.')
