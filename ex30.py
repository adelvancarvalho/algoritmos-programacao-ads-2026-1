# Entrada

minutos_totais = int(input("Digite a quantidade de minutos: "))

# Processamento

dias = minutos_totais // 1440
resto_dias = minutos_totais % 1440

horas = resto_dias // 60
minutos_restantes = resto_dias % 60

# Saída

print(f"Isso equivale a: {dias} dia(s), {horas} hora(s) e {minutos_restantes} minuto(s).")
