def aumentar(preco=0, taxa=0, format=False):
    """
    Essa função aumenta o preço de um produto, com uma taxa de x%.
    preco = preço do produto
    taxa = taxa em %
    format = formatar para um tipo monetário
    """
    res = preco + (preco * taxa/100)
    return res if format is False else monetário(res)


def diminuir(preco=0, taxa=0, formato=False):
    """
    Essa função diminui o preço de um produto, com uma taxa de x%.
    preco = preço do produto
    taxa = taxa em %
    format = formatar para um tipo monetário
    """
    res = preco - (preco * taxa/100)
    return res if format is False else monetário(res)


def metade(preco=0, formato=False):
    """
    Essa função mostra a metade do preço de um produto
    preco = preço do produto
    format = formatar para um tipo monetário
    """
    res = preco / 2
    return res if not formato else monetário(res)


def dobro(preco=0, formato=False):
    """
    Essa função mostra a metade do preço de um produto
    preco = preço do produto
    format = formatar para um tipo monetário
    """
    res = preco * 2
    return res if not formato else monetário(res)


def monetário(preco: float = 0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, aumento=0, reducao=0):
    print('-' * 30)
    print(f'{"Resumo do valor":^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{monetário(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de desconto: \t{diminuir(preco, reducao, True)}')
    print('-' * 30)
