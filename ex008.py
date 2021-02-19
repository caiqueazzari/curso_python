#Escreva um programa que leia um valor em metros e o exiba em centímetros e milímetros.

n = int(input('Digite um valor em metros: '))
cm = n * 100
mm = n * 1000
print(f'{n}m equivalem {cm}cm e {mm}mm.')
