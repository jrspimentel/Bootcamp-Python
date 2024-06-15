### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

qtd_tentativas = 3
tentativa = 1  
while tentativa <= qtd_tentativas:
    print(f"Tentativa {tentativa} de {qtd_tentativas}")
    # Aqui seria o código python oara conexão
    if True: # Simulando que deu sucesso na conexão.
        print("Conexão bem-sucedida!")
        break
        tentativa += 1
    else:
        print("Falha ao conectar após várias tentativas.")

