#  1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

num1 = input("Insira o primeiro número inteiro: ")
num2 = input("Insira o segundo número inteiro: ")
if num1.isspace() or num2.isspace():
    print("Você digitou espaço, ao invés de números inteiros")
else:
    try:
        num1 = int(num1)
        num2 = int(num2)
        soma = num1 + num2
        print(f"A soma dos números {num1} e {num2} é igual {soma}")
    except ValueError:
        print("Você não digitou número inteiro")
        



 