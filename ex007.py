#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média.

aluno = str(input('Digite o nome do(a) aluno(a): '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
s = n1 + n2
m = s / 2
print(f'A média das notas do(a) {aluno} é de: {m:.2f}.')
