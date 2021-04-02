'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

values = [[], []]

for x in range(0, 7):
    n = int(input(f'Digite o {x + 1}° valor: '))
    if n % 2 == 0:
        values[0].append(n)
    else:
        values[1].append(n)

print(f'Os valores pares digitados foram {sorted(values[0])}')
print(f'Os valores impares digitados foram {sorted(values[1])}')