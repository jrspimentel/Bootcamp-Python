# DESAFIO 01  USANDO TRY

try:
    # Solicite o nome ao usuário:
    nome =  input("Informe seu nome: ")
    
    # Verifica se o "nome" está vazio
    if len(nome) == 0: 
        raise ValueError ("O nome não pode está vazio")
    # Verifica se digitou apenas espaços ou se contém espaços no inicio do "nome"
    elif nome.isspace(): 
        raise ValueError("Nome inválido, favor digite corretamente!")
    # Verifica se o "nome" contém números
    elif any(char.isdigit() for char in nome): 
         raise ValueError("O nome não pode conter números")
    else:
        print("Nome válido: ", nome)    
except ValueError as e:
    print(e)

# Solicita ao usuário o salario e converte pra float
try:
    salario = float(input("Informe seu salário: "))

    #Validações do Salário
    if  salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")

# Solicita ao usuário que digite o valor do bônus recebido e converte para float
try:
    bonus_recebido = float(input("Digite o valor do bônus recebido: "))
    if bonus_recebido < 0:
        print("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")

# Assumindo uma lógica de cálculo para o bônus final e KPI
bonus_final = bonus_recebido * 1.2  # Exemplo, ajuste conforme necessário
kpi = (salario + bonus_final) / 1000  # Exemplo simples de KPI

# Imprime as informações para o usuário
print(f"Seu KPI é: {kpi:.2f}")
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")