'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

print('-' * 40)
print(f'{"Listagem de preços":^40}')
print('-' * 40)

tabela = ('Caderno', 5.00, 'Borracha', 2.00, 'Lápis', 1.00, 'Régua', 2.00, 'Mochila', 250, 'Livro', 40, 'Estojo', 10)

for x in range(0, len(tabela), 2):
    print(f'{tabela[x]:.<31}R${tabela[x + 1]:>7.2f}')
