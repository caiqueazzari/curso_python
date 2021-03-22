'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''

from time import sleep

white = '\033[38m'
blue = '\033[36m'

totalSpent, countExpensives, cheapest, cheapestName = 0, 0, 1, ''

while True:
    productName = str(input('\nType the name of the product: ')).strip().title()
    price = float(input('\nType the price of the product: R$'))
    totalSpent += price

    if cheapest == 1:
        cheapest = price
        cheapestName = productName
    if price < cheapest:
        cheapest = price
        cheapestName = productName

    if price > 1000:
        countExpensives += 1

    awnser = ' '
    while awnser not in 'Y/N':
        awnser = str(input('\nNeed to read one more product? (Y/N)')).strip().upper()[0]

    if awnser == 'Y':
        continue
    elif awnser == 'N':
        print('\nExiting.. ')
        sleep(1)
        break

print(f'\nTotal spent on this purchase: R${totalSpent:.2f}.')
if countExpensives > 1:
    print(f'\n{countExpensives} products costs more than R$1000.')
elif countExpensives == 1:
    print(f'\nOnly one product cost more than 1000.')
else:
    print('\nNo product cost more than 1000.')
print(f'\n{cheapestName} is the cheapest product that costs R${cheapest:.2f}.')
