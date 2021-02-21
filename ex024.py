#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

city = str(input('Digite o nome de uma cidade: '))
list = city.upper().split()

if list[0] == "SANTO":
    print('Essa cidade começa com "Santo".')
else:
    print('Essa cidade não começa com "Santo".')
