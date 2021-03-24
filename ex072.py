'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.
'''

num_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
                'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

resposta = ' '
while resposta != 'N':
    while True:
        resposta = ' '
        num = int(input('\nDigite um número entre 0 e 20: '))

        if 0 <= num <= 20:
            break
        else:
            print('\nTente novamente.. ')

    print(f'\nO número {num} por extenso é: {num_extenso[num]}')

    while resposta not in 'SN':
        resposta = str(input('\nDeseja ver outro número por extenso? (S/N) ')).strip().upper()[0]
