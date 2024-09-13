'''
7 Filtragem de Dados
Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
'''
age : list = [15, 18, 47, 45, 58, 10, 14]
lista : list = []


def maior_idade(maior_igual_18 : list) -> list:
    for numero in age:
        if numero >= 18 in age:
            lista.append(numero)

    return lista


print(maior_idade(age))