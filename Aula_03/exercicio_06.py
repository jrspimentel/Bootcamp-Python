### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

texto = 'O rato roeu a roupa do rei de roma'
texto_separado = texto.split()
contagem_palavras = {}

for palavras in texto_separado:
    if palavras in contagem_palavras:
        contagem_palavras[palavras] +=1
    else:
        contagem_palavras[palavras] = 1

print(contagem_palavras)