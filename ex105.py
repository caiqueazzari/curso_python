'''
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação(opcional)
'''


def notas(* n, sit=False):
    """
    Essa função análisa as notas e situações de vários alunos.
    n = notas dos alunos.
    sit = valor opcional, mostra a situação da turma.
    return = retorna o dicionário contendo as informações dos alunos.
    """
    turma = {}
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['média'] = sum(n) / len(n)
    if sit:
        if turma['média'] <= 5:
            turma['situação'] = 'PÉSSIMA'
        elif turma['média'] <= 7:
            turma['situação'] = 'RAZOÁVEL'
        else:
            turma['situação'] = 'BOA'
    return turma


print(notas(1, 6, 20, 3, 10, 5, 7, 10, sit=True))
#help(notas)