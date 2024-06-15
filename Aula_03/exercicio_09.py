### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.

# Opção 1
lista = [1, 2, 3, 4, 5, 6, 7, 8]
lista_par = []
for i in lista:
    if i % 2 == 0:
        lista_par.append(i)

print(lista_par)
