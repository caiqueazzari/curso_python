'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = ('cachorro', 'caderno', 'abacaxi', 'arroz', 'carne', 'bola', 'gato', 'notenook')

for x in range(len(palavras)):
    print(f'\nVogais da palavra {palavras[x]}: ', end='')
    a = palavras[x].count('a')
    e = palavras[x].count('e')
    i = palavras[x].count('i')
    o = palavras[x].count('o')
    u = palavras[x].count('u')
    if a >= 1:
        print('a ', end='')
    if e >= 1:
        print('e ', end='')
    if i >= 1:
        print('i ', end='')
    if o >= 1:
        print('o ', end='')
    if u >= 1:
        print('u ', end='')
    print()
