'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

expression = str(input('Digte uma expressão: '))
parenteses = list()

for x in expression:
    if x == '(':
        parenteses.append('(')
    elif x == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break

if len(parenteses) == 0:
    print('\033[32mSua expressão é válida!')
else:
    print('\033[31mSua expressão é inválida!')