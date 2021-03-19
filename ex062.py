'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

n1 = int(input('Digite o \033[1;36m1º\033[0;38m termo da PA: '))
n = int(input('Digite o \033[1;36mN-ésimo\033[0;38m termo da PA: '))
r = int(input('Digite a \033[1;36mrazão\033[0;38m da PA: '))
print('\nPA: \n')
awnser = 'S'
y = 1

for x in range(n1, n + 1, r):
    print(f'p{y} = {x}')
    y += 1

while awnser != 'N':
  
    awnser = str(input('\nDeseja ver novos termos? (\033[1;32mS\033[0;38m/\033[1;31mN\033[0;38m) ')).strip().upper()[0]

    if awnser == 'S':
        n1 = int(input('\nDigite o \033[1;36m1º\033[0;38m termo da PA: '))
        n = int(input('Digite o \033[1;36mN-ésimo\033[0;38m termo da PA: '))
        r = int(input('Digite a \033[1;36mrazão\033[0;38m da PA: '))
        print('\nPA: \n')
        y = 1
        
        for x in range(n1, n + 1, r):
            print(f'p{y} = {x}')
            y += 1

    elif awnser == 'N':
        print('\n\033[1;36mSaindo.. :)')
        break

    else:
        print('\n\033[1;31mDigite uma resposta válida !\033[0;38m')
