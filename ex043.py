'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo
com a tabela abaixo:
- Abaixo do 18.5: Abaixo do peso.
- Entre 18.5 e 25: Peso ideal.
- 25 até 30: Sobrepeso.
- 30 até 40: Obesidade.
- Acima de 40: Obesidade morbida.'''

from time import sleep

print('\033[31m=*=' * 5)
print('Calculo do IMC')
print('=*=' * 5)

peso = str(input('\033[mDigite o peso: '))
altura = str(input('Digite a altura: '))

peso = float(peso.replace(',', '.'))
altura = float(altura.replace(',', '.'))
imc = peso / (altura ** 2)
print('Processando..')
sleep(3)
print(f'O IMC dessa pessoa é de: {imc:.1f}')

if imc < 18.5:
    print('Ela está abaixo do peso!')
elif imc >= 18.5 and imc <= 24.9:
    print('Ela está com o peso ideal!')
elif imc >= 25 and imc < 30:
    print('Ela está acima do peso!')
elif imc >= 30 and imc <= 40:
    print('Ela está obeso!')
elif imc > 40:
    print('Ela está com obesidade morbida!')
else:
    print('Valores inválidos.')
