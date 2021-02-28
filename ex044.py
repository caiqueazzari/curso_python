'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto.
- À vista no cartão: 5% de desconto.
- Em até 2x no cartão: preço normal.
- 3x ou mais no cartão: 20% de juros.'''

from time import sleep

preço = str(input('Digite o preço do produto: R$'))
preço = float(preço.replace(',', '.'))
pagamento = int(input('Opções de pagamento:'
                      '\n\t1 - Dinheiro: 10% de desconto'
                      '\n\t2 - Cheque: 10% de desconto'
                      '\n\t3 - 1x no cartão: 5% de desconto'
                      '\n\t4 - 2x no cartão: 0% de desconto'
                      '\n\t5 - 3x ou mais no cartão: 20% de juros'
                      '\nDigite a opção de pagamento: '))
print('Processando..')
sleep(3)

if pagamento == 1 or pagamento == 2:
    print(f'Valor a ser pago pelo produto: \033[1mR${preço - (preço * 0.10):.2f}')
elif pagamento == 3:
    print(f'Valor a se pagar pelo produto: \033[1mR${preço - (preço * 0.05):.2f}')
elif pagamento == 4:
    print(f'Valor a ser pago pelo produto: 2 parcelas de \033[1mR${preço / 2:.2f}')
elif pagamento == 5:
    print(f'Valor total a ser pago pelo produto: \033[1mR${preço + (preço * 0.20):.2f}')
else:
    print('\033[1mOpção inválida.')
    
