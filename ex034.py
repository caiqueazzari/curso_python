'''Escreve um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais de R$1.250,00. o aumento é de 15%.'''

sal = float(input('\033[036mDigite o valor do seu salário: R$'))

print('Parabéns, você acaba de receber um aumento!')

if sal > 1250:
    print(f'O seu novo salário é de: \033[mR${sal * 1.10:.2f}!')

if sal < 1250:
    print(f'O seu novo salário é de: \033[mR${sal * 1.15:.2f}!')
