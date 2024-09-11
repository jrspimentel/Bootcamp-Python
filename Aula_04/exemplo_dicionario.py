
produto_1 : dict =  {'nome': 'sapato', 'valor': 100.50, 'quantidade': 1}

produto_2 : dict = {'nome': 'televisao','valor': 999.50,'quantidade': 2}


produtos = []
produtos.append(produto_1)
produtos.append(produto_2)
produtos_juntos = produtos

lista = []

for p in produtos:
    lista.append(p)
print(lista)