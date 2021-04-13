'''
Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
'''

import requests


def siteTester(site='http://pudim.com.br'):
    """
    Teste se um site está acessível
    informe a url completa, contendo http ou https.
    Exemplo: https://pudim.com.br
    """
    try:
        requests.get(site)
    except:
        return f'\033[31mO site {site} não está disponível no momento.\033[m'
    else:
        return f'\033[34mO site {site} está disponível!\033[m'


print(siteTester('https://facebook.com'))
print()
help(siteTester)