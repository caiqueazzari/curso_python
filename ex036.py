'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o
valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado'''


print('\033[33m=*=' * 7)
print(' Empréstimo bancário')
print('=*=' * 7)

print('\n\033[mSintaxe: 200 mil = 200.000')
valor_casa = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o seu salário: R$'))
anos = int(input('Digite a quantidade de anos para pagar a casa: '))

pmensal = valor_casa / (12 * anos)

if pmensal > (sal * 0.30):
    print('\n\033[33mEmpréstimo negado!')
elif pmensal < (sal * 0.30):
    print('\n\033[33mEmpréstimo aceito!')
