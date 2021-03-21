'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou
não continuar a digitar valores.'''

awnser, cont, media, lista, soma = 'S', 0, 0, [], 0

while awnser != 'N':

    if awnser == 'S':
        num = int(input('\nDigite um número inteiro: '))
        cont += 1
        soma += num
        lista.append(num)

    awnser = str(input('\nDeseja continuar digitando números? (S/N) ')).strip().upper()[0]

    if awnser == 'N':
        print('\nProcessando..')

    else:
        print('\nDigite uma opção Válida!')

if len(lista) == 1:
    print(f'\nVocê digitou apenas um número, o {num}.')
else:
    print(f'\nVocê digitou {cont} números.')
    print(f'\nA média dos números digitados foi de {soma / cont}.')
    print(f'\nO maior valor digitado foi {max(lista)} e o menor foi {min(lista)}.')
