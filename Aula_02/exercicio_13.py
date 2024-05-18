# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.


frase_inicial = input("Insira uma frase: ")
numero_caractere_anterior = len(frase_inicial)
if frase_inicial.isnumeric() is False:
    frase_final = frase_inicial.strip()
    print(f"O comprimento da frase '{frase_inicial}' antes da remoção dos espaços no inicio e final era de {numero_caractere_anterior} caracteres.") 
    print(f"O comprimento frase após a remoção dos espaços é de {len(frase_final)} caracteres!")
else: 
    print("O valor digitado não é uma string!")