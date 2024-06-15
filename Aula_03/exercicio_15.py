### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

lista =  [1, 2, 3 , 4, "parar", 5, 6]
valor = 0
while valor < len(lista):
    if lista[valor] == "parar":
        print("Parada encontrada, processamento encerrado")
        break
    print(f"Processando valor: {lista[valor]}")
    valor +=1