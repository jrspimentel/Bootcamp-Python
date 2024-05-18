# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

try:
    data = input("Insira uma data no formato 'dd/mm/aaaa': ")
    separando = data.split("/")
    print (f"Dia: {separando[0]}, Mês: {separando[1]} e Ano: {separando[2]} ")
except:
    print("Formato Inválido!")