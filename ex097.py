'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável.
Ex:
escreva(‘Olá, Mundo!’) Saída:
~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~
'''


def escreva(msg):
    print('~' * (len(msg) + 4))
    print(f'  {msg}  ')
    print('~' * (len(msg) + 4))


mensagem = str(input('Digite a mensagem: '))
escreva(mensagem)
