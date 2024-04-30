# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

try:
    num = float(input("Insira um número para elevar ao quadrado: "))
    quadrado = num**2
    print(f"O quadrado do número {num} é igual a {quadrado}")      
except ValueError: 
    print("Valor digitado não é um número")
