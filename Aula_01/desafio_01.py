# DESAFIO 01

# Solicite o nome ao usuário:
nome = print("Olá, " + input("Informe seu nome: " ) + "!")

# Solicite o salário ao usuário:
salario = float(input("Informe seu salário: "))

# Informe o bônus
bonus =  float(input("Informa o percentual do bonus: "))

# Calculo do bônus anual de 2024
valor_bonus = 1000 + (salario * bonus)
# Imprime o bônus
print(f"O valor do bônus de 2024 será: R$ {valor_bonus}")