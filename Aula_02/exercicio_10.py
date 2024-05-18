# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# Importando biblioteca 
from math import pi

# Calculo da área do círculo
try:
    raio = float(input("Insira o raio do círculo para calcular a área: "))
    calculo_da_area = pi * raio ** 2
    print(f"A área do círculo de {raio} é {calculo_da_area:.2f} ")
except:
    print("O valor digitado está incorreto!")