'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
de uma Sequência de Fibonacci. Exemplo:'''

print("-=" * 20)
print('Sequência de Fibonnaci')
print("-=" * 20)
nterms = int(input('Quantos termos você quer mostar?: '))
print(f'Sequência de Fiobannaci até o {nterms}º termo. ')
n1, n2 = 0, 1
count = 0

while count < nterms:
    print(n1, end=' ')
    f = n1 + n2
    n1 = n2
    n2 = f
    count += 1
