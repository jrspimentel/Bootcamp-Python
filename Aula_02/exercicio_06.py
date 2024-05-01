# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

try:
    num1 = float(input("Insira o primeiro número flutuante: "))
    num2 = float(input("Insira o primeiro número flutuante: "))
    soma = round(num1 + num2, 2)
    print(f"A soma dos valores {num1} e {num2} é igual ao {soma}")
except ValueError :
    print("Valor digitado não é um número!")