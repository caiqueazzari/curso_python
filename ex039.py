'''Faça um programa que leia o ano de um jovem e informe, de acordo com sua idade
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

print('\033[31m=*=\033[m' * 7)
print('\033[1mAlistamento militar!')
print('\033[31m=*=' * 7)

idade = int(input('\033[mInforme a sua idade: '))

if idade <= 17:
    if (18 - idade) == 1:
        print(f'Você deverá se alistar daqui {18 - idade} ano.')
    elif (18 - idade) != 1:
        print(f'Você deverá se alistar daqui {18 - idade} anos.')
elif idade == 18:
    print('Já é hora de se alistar!')
elif idade > 18:
    if idade == 19:
        print('Você deveria ter se alistado no ano passado! Vá até a JMS mais próxima da sua casa imediatamente!')
    if idade > 19:
        print(f'Você deveria ter se alistado há {idade - 18} anos! Vá até a JMS mais próxima da sua casa imediatamente!')
