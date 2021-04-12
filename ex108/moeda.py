def aumentar(preco=0, taxa=0):
    """
    Essa função aumenta o preço de um produto, com uma taxa de x%.
    preco = preço do produto
    taxa = taxa em %
    """
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco=0, taxa=0):
    res = preco - (preco * taxa/100)
    return res


def metade(preco=0):
    res = preco / 2
    return res


def dobro(preco=0):
    res = preco * 2
    return res


def monetário(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
