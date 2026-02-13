# Entrada

total_dias = int(input("Digite a idade expressa em dias: "))

# Processamento

anos = total_dias // 365
resto = total_dias % 365
meses = resto // 30
dias = resto % 30

# Saída

print(f"Isso corresponde a: {anos} anos, {meses} meses e {dias} dias.")
