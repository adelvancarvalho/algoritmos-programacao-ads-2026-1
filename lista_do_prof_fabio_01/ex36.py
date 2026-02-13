# Entrada

anos = int(input("Quantos anos você tem? "))
meses = int(input("E quantos meses? "))
dias = int(input("E quantos dias? "))

# Processamento

total_dias = (anos * 365) + (meses * 30) + dias

# Saída

print(f"Sua idade total em dias é: {total_dias}")
