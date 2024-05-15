#1
def bombom(dinheiro,preco):
    n_bombons = dinheiro // preco
    troco = dinheiro % preco
    return n_bombons, troco 

#2
def a_mais(dinheiro, preco):
    qtd, troco = bombom(dinheiro, preco)
    return preco - troco
