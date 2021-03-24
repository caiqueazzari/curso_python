'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = ('cachorro', 'caderno', 'abacaxi', 'arroz', 'carne', 'bola', 'gato', 'notenook')

for x in palavras:
    print(f'\nVogais da palavra {x}: ', end='')
    for y in x:
        if y in 'aeiou':
            print(y, end=' ')
    print()