'''Crie um programa que leia uma frase qualquer e diga se ela é palíndromo, desconsiderando os espaços.
Ex: Apos a sopa'''

frase = str(input('Digite uma frase: ')).replace(' ', '').upper()
frase_invertida = frase[::-1]

print(f'O inverso dessa frase é {frase_invertida}.')

if frase == frase_invertida:
    print('A frase é um palíndromo! ')
else:
    print('A frase não é um palíndromo! ')
