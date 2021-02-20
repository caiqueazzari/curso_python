#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
#que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

nomes = []
ordem = [0, 1, 2, 3]

for x in range(4):
    for y in range(4):
        nomes.append(input(f'Digite o nome do {y + 1}º aluno: '))
        x + 1
        y + 1
    break

random.shuffle(ordem)
print(f'\nApós o sorteio, foi sorteada uma ordem para as apresentações dos trabalhos: \n')

for x in range(4):
    y = ordem[x]
    print(f'{x + 1}º a apresentar é o(a): {nomes[y]}')
    x + 1
