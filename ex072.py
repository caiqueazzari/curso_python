'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.
'''
num_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
                'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('\nDigite um número entre 0 e 20: '))
    if num >= 0 and num <= 20:
        break
print(f'\nO número {num} por extenso é: {num_extenso[num]}')
