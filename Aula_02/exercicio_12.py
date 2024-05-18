# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.


nome_completo = input("Insira seu nome completo: ")
if nome_completo.isnumeric() is False:
    nome_completo = nome_completo.lower()
    print(nome_completo) 
else: 
    print("O valor digitado não é uma string!") 
