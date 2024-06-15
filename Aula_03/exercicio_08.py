### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# Dicionário
dic = {
    'nome': 'Renato',
    'idade': '29',
    'cidade': '',
    'profissao': 'Analista de Dados',
    'telefone': None
}


# Filtrando os itens faltantes (valores que são strings vazias ou None)
faltantes = {chave: valor for chave, valor in dic.items() if valor == '' or valor is None}

# Imprimindo os itens faltantes
print(faltantes)
