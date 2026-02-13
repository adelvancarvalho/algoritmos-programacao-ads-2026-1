# Entrada

anos_fumando = int(input("Há quantos anos você fuma? "))
cigarros_dia = int(input("Quantos cigarros por dia? "))
preco_carteira = float(input("Qual o preço da carteira? R$ "))

# Processamento

total_dias = anos_fumando * 365
total_cigarros = total_dias * cigarros_dia

total_carteiras = total_cigarros / 20

gasto_total = total_carteiras * preco_carteira

# Saída

print(f"Você já gastou um total de: R$ {gasto_total:.2f}")
