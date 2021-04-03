'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
individualmente.
'''


dados, lista, resp, num = [], [], ' ', 0

while resp != 'N':
    resp = ' '
    dados.append(str(input('\nDigite o nome: ')).strip().title())
    dados.append(float(input('Digite a primeira nota: ')))
    dados.append(float(input('Digite a segunda nota: ')))
    lista.append(dados[:])
    dados.clear()
    while resp not in 'SN':
        resp = str(input('\nDeseja continuar? (S/N) ')).strip().upper()[0]
print(f'\n{"Nº":<4}{"Nome":<10}{"Média":>8}')
for x in range(len(lista)):
    print(f'{x:<4}{lista[x][0]:<10}{(lista[x][1] + lista[x][2]) / 2:>8.1f}')
while num != 999:
    num = int(input('\nMostrar as notas de qual aluno? (999 interrompe) '))
    if num == 999:
        print('\nSaindo..')
        break
    if num <= len(lista) - 1:
        print(f'\nNotas de {lista[num][0]} são {lista[num][1:3]}')
    else:
        print('\nAluno não cadastrado.. Tente novamente!')