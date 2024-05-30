### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

idade = int(input("Insira a sua idade: "))
email =  input("Insira um e-mail válido no formado 'usuario@exemplo.com: ")

if not 18 <= idade <= 65:
    print("Idade fora do intervalo permitido!")
elif "@" not in email or "." not in email:
    print("Este e-mail é inválido!")
else:
    print("Dados de usuário válidos! ") 
