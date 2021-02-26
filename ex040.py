'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

aluno = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2

if media < 5:
    print(f'O aluno {aluno} foi REPROVADO por conta da sua média ser inferior a 5!')
elif media >= 5 and media <= 6.9:
    print(f'O aluno {aluno} ficou de RECUPERAÇÃO pois não atingiu a média 7!')
elif media >= 7 and media <= 10:
    print(f'O aluno {aluno} foi APROVADO!')
else:
    print('Nota inválida! Digite números entre 0 e 10')
