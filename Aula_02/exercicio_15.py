# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
 
# Input de dados:
string_1 = str(input("Insira a primeira string: "))
string_2 = str(input("Insira a segunda string: "))

# Verificação se as strings são válidas
if not (string_1.isspace() or string_2.isspace()):
    contac = string_1 + string_2
    print(contac)
else:
    print("A informação digitada é inválida!")