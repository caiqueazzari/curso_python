#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la , sabendo que cada litro de tinta pinta uma área de 2m².

l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))
A = a * l
tinta = A / 2
print(f'A área da parede é {A:.3f}m² e precisa de {tinta:.3f} litros de tinta para ser pintada.')
