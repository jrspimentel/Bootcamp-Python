# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

try:
    num1 = float(input("Insira o primeiro número flutuante: "))
    num2 = float(input("Insira o primeiro número flutuante: "))
    media = (num1 + num2) / 2
    print(f"A média dos valores {num1} e {num2} é igual ao {round(media, 2)}")
except ValueError :
    print("Valor digitado não é um número!")