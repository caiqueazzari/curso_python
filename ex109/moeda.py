def aumentar(preco=0, taxa=0, format=False):
    """
    Essa função aumenta o preço de um produto, com uma taxa de x%.
    preco = preço do produto
    taxa = taxa em %
    """
    res = preco + (preco * taxa/100)
    return res if format is False else monetário(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa/100)
    return res if format is False else monetário(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if not formato else monetário(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if format is False else monetário(res)


def monetário(preco: float = 0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
