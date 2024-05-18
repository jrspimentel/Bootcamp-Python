# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

try:
    c = float(input("Insira a temperatura em graus C°: "))
    f = (c * 9/5) + 32 
    print(f)
except:
    print("Você digitou um valor incorreto!")