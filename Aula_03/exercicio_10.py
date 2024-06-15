### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.  


vendas = [
    {"categoria": "alimentos", "valor": 600},
    {"categoria": "limpeza", "valor": 450},
    {"categoria": "alimentos", "valor": 800}
]

total_categoria = {}
for i in vendas:
    categoria = i["categoria"]
    valor = i["valor"]
    if categoria in total_categoria:
        total_categoria[categoria] += valor
    else:
        total_categoria[categoria] = valor

print(total_categoria)