produto: str = "sapato"
produto_2: str = "camiseta"
produto_3: str = "videogame"

lista = ['sapato', 'camiseta', 'videogame', 'computador']

p = []

for produto in lista:
    if produto in lista:
        p.append(produto)  # Adiciona o item individual, não a lista completa
print(p)