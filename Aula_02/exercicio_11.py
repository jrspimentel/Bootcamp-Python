# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

texto = input("Insira uma string para converter as letras em maiúsculas: ")
if texto.isnumeric() is False:
    texto_maiusculo = texto.upper()
    print(texto_maiusculo) 
else: 
    print("O valor digitado não é uma string!") 

