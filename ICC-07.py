# ENTRADA:
n = int(input())
c = int(input())
m = int(input())

dinheiro = n
preco = c
promocao = m

# PROCESSAMENTO:
embalagens = dinheiro // preco
chocolates = dinheiro // preco

while (embalagens >= promocao):
    embalagensGanhas = embalagens // promocao
    chocolates += embalagensGanhas
    embalagens -= embalagensGanhas * promocao
    embalagens += embalagensGanhas

# SAIDA:
print(chocolates)
