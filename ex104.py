'''
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
'''


def leiaInt(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            num = int(num)
            return num
        else:
            print('\033[31mDigite apenas números!!\033[m')


n = leiaInt('Digite um número: ')
print(f'\nVocê acabou de digitar o número {n}.')