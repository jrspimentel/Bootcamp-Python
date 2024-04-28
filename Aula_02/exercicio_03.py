# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

try:
    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))
    resultado = num1 * num2
    print(f"A multiplicação de {num1} por {num2} é igual {resultado}")
except:
    print("O valor digitado não é um número!")