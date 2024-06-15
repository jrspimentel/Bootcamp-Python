### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

while True:
    entrada = input("Digite algo (ou 'sair' para sair): ")
    if entrada.lower() == 'sair':
        break
    print("Você digitou:", entrada)
print("Saindo do programa...")
