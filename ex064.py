'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).'''

cont, x, soma, num = 0, 1, 0, 0
print('\n[Digite 999 caso queira parar de adicionar números.]')

while num != 999:
    num = int(input(f'\nDigite o {x}° número inteiro: '))
    x += 1
    cont += 1
    soma += num

print(f'\nQuantidade de números digitados: {cont}.')
print(f'\nA soma de todos os {cont - 1} números digitados é de {soma - 999}.')
