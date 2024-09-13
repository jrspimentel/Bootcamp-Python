import csv

caminho = 'exemplo.csv'

dados = []

#lendo
def ler_csv(caminho):
    with open(caminho, mode= 'r', encoding='utf-8') as arquivo:
        ler_arquivo = csv.DictReader(arquivo)
        for linha in ler_arquivo:
            dados.append(linha)
    
    return dados
       

print(ler_csv(caminho))


# Escrevendo
with open(caminho, mode= 'w', encoding='utf-8') as arquivo:
    campos = ['nome', 'quantidade', 'preco', 'disponibilidade']
    escrever = csv.DictWriter(arquivo, fieldnames= campos)
    escrever.writeheader()
    escrever.writerow({'nome': 'Fulano', 'quantidade': 4, 'preco': 47.7, 'disponibilidade': False})
    escrever.writerow({'nome': 'Ciclano', 'quantidade': 18, 'preco': 148.7, 'disponibilidade': 'false'})