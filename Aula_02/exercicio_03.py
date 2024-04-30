# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

try:
    num1 = int(input("Insira o primeiro número inteiro: "))
    num2 = int(input("Insira o segundo número inteiro: "))
    resultado = num1 * num2
    print(f"A multiplicação de {num1} por {num2} é igual {resultado}")
except:
    print("O valor digitado não é um número inteiro!")