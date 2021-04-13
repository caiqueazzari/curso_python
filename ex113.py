'''
Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de
tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número inteiro!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mO usuário decidiu interromper a entrada de dados.\033[m')
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            numFloat = str(input(msg)).strip().replace(',', '.')
            numFloat = float(numFloat)
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31m\nO usuário decidiu não digitar nenhum número. \033[m')
            return 0
        else:
            return numFloat


# Programa principal
i = leiaInt("Digite um número inteiro: ")
f = leiaFloat("Digite um número Real: ")
print(f'O número inteiro digitado foi {i} e o real foi {f}')
