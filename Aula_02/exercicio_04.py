# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

try:
    num1 = int(input("Insira o primeiro número inteiro: "))
    num2 = int(input("Insira o segundo número inteiro: "))
    divisao_inteira = num1 // num2
    print(f"A parte inteira da divisão de {num1} por {num2} é igual a {divisao_inteira}")
except ValueError:
    print("Você não digitou um número inteiro.")
except ZeroDivisionError:
    print("A divisão por zero não é permitida.")

        
