#Refaça o DESAFIO 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.

n = int(input('Digite um número inteiro: '))
print(f'A tabuada de {n} é: ')

for x in range(1, 11):
    print(n, 'x', x, ':', n * x)

