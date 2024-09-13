'''
8. Ordenação Personalizada
Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
'''

pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Pedro", "idade": 25},
    {"nome": "Carol", "idade": 20}
]

def ordenar_dicionario(pessoas):
    dict_ordenado = sorted(pessoas, key= lambda x:x['nome'])
    return dict_ordenado

print(ordenar_dicionario(pessoas))

