'''
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número
a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela
o processo de cálculo do fatorial.
'''


def fatorial(n, show=False):
    """
    Calcula o fatorial de um número
    n = número a ser calculado
    show = mostra a conta
    return = o valor fatorial de n
    """
    f = 1
    for x in range(n, 0, -1):
        if show:
            print(x, "x " if x > 1 else '= ', end='')
        f *= x
    return f


print(fatorial(5, True))
print()
help(fatorial)
