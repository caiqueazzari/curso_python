'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase: ')).upper().strip()
contador = frase.count('A')
print(f'A palavra "A" aparece {contador} vezes na frase!')
print(f'A primeira vez que a palavra "A" apareceu, foi na posição: {frase.find("A") + 1}')
print(f'A última vez que a palavra "A" apareceu, foi na posição: {frase.rfind("A") + 1}')
