#Escreva um programa que leia um valor em metros e o exiba em centímetros e milímetros.

n = int(input('Digite um valor em metros: '))
c = n * 100
m = n * 1000
print(f'{n}m equivalem {c}cm e {m}mm.')
