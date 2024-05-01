# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

try:
    base = float(input("Insira um número para calcular a potência: "))
    potencia = float(input("Insira um número para o expoente da potência: "))
    calculo = base**potencia
    print(f"O número {base} elevado a potência {potencia} é igual {calculo}")
except:
    print("O valor digitado não é um número!")