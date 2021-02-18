#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela:

algo = input('Digite algo: ')
print(f'O tipo primitivo de {algo} é {type(algo)}')
print(f'{algo} está em maiúsculo? {algo.isupper()}')
print(f'{algo} tem apenas dígitos? {algo.isdigit()}')
print(f'{algo} está em minúsculo? {algo.islower()}')
print(f'{algo} consiste apenas em caracteres alfabéticos? {algo.isalpha()}')
print(f'{algo} todas as palavras começam com a letra maiúscula? {algo.istitle()}')
print(f'{algo} é um número? {algo.isnumeric()}')
print(f'{algo} é alfanúmerico? {algo.isalnum()}')
print(f'{algo} tem apenas espaços? {algo.isspace()}')
