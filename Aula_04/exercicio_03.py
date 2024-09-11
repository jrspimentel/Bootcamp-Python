# 3 Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.

dicionario : dict = {
    'livro': 'Storytelling com Dados',
    'autor': 'knaflic',
    'ano': '2015'
} 

dict = dicionario.items()

for keys, values in dict:
    print(f'{keys}: {values}')