# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

try:
    num = int(input("Insira o primeiro número inteiro: "))
    resto = num % 5
    print(f"O resto da divisão é {resto}")
except:
    print("O valor digitado não é um número inteiro!")
