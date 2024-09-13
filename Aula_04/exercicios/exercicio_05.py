# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

lista = ["maçã", "banana", "cereja"]
dicionario = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}


lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = sum(precos[item] for item in lista_compras)
print(f"Preço total: {total}")