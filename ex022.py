'''Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
- Quantas letras tem o primeiro nome.'''

name = str(input('Digite o seu nome completo: '))
print(f'Olá {name.strip().title()}! \nO seu nome com todas as letras maiúsculas: {name.upper().strip()}')
print(f'O seu nome com todas as letras minúsculas: {name.lower().strip()}')
lista = name.split()
print(f'O seu nome contém {len(name.strip().replace(" ", ""))} letras!')
print(f'O seu primeiro nome possui {len(lista[0])} letras!')
