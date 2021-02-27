'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 25 anos: SÊNIOR
- Acima: MASTER'''

from datetime import date

atleta = str(input('Digite o nome do atleta: ')).capitalize()
ano = int(input('Digite o ano de nascimento do atleta do atleta: '))

idade = date.today().year - ano

if idade <= 9:
    print(f'{atleta} tem {idade} anos e está na categoria MIRIM!')
elif idade <= 14:
    print(f'{atleta} tem {idade} anos e está na categoria INFANTIL!')
elif idade <= 19:
    print(f'{atleta} tem {idade} anos e está na categoria JUNIOR!')
elif idade <=25:
    print(f'{atleta} tem {idade} anos e está na categoria SÊNIOR!')
else:
    print(f'{atleta} tem {idade} anos e está na categoria MASTER!')
