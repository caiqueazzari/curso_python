def aumentar(preco, taxa):
    """
    Essa função aumenta o preço de um produto, com uma taxa de x%.
    preco = preço do produto
    taxa = taxa em %
    """
    res = preco + (preco * taxa/100)
    return res


def diminuir(preco, taxa):
    res = preco - (preco * taxa/100)
    return res


def metade(preco):
    res = preco / 2
    return res


def dobro(preco):
    res = preco * 2
    return res