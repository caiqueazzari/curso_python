'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER'''

atleta = str(input('Digite o nome do atleta: ')).capitalize()
idade = int(input('Digite a idade do atleta: '))

if idade <= 9:
    print(f'{atleta} está na categoria MIRIM!')
elif idade > 9 and idade <= 14:
    print(f'{atleta} está na categoria INFANTIL!')
elif idade > 14 and idade <= 19:
    print(f'{atleta} está na categoria JUNIOR!')
elif idade > 19 and idade <=20:
    print(f'{atleta} está na categoria SÊNIOR!')
else:
    print(f'{atleta} está na categoria MASTER!')
