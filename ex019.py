#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajuda ele,
#lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

nomes = []

for x in range(4):
    for y in range(4):
        nomes.append(input(f'Digite o nome do {y + 1}º aluno: '))
        x + 1
        y + 1
    break

print(f'O aluno sorteado foi: {choice(nomes)}')
