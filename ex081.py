'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

valores = []
resp = ' '

while resp != 'N':
    resp = ' '
    valores.append(int(input('Digite um valor: ')))
    while resp not in 'SN':
        resp = str(input('Você deseja continuar? (S/N) ')).strip().upper()[0]

print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente: {sorted(valores, reverse=True)}')

if 5 in valores:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')