from interface import *
from arquivo import *


arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

opções = ['Ver pessoas cadastradas no sistema',
          'Cadastrar nova pessoa',
          'Sair do sistema']

escolha = 0
while escolha != 3:
    escolha = menu(opções)

    if escolha == 1:
        lerArquivo(arq)
    elif escolha == 2:
        print('-' * 50)
        print(f'\033[1;34m{"Novo cadastro":^50}\033[0m')
        print('-' * 50)
        nome = str(input('Nome:'))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    else:
        break
