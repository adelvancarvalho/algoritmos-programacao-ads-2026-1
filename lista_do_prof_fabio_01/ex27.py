# Entrada

segundos_totais = int(input("Digite a quantidade de segundos: "))

# Processamento

horas = segundos_totais // 3600
resto_horas = segundos_totais % 3600  # O que sobrou que não formou uma hora

minutos = resto_horas // 60
segundos_restantes = resto_horas % 60 

# Saída

print(f"Isso equivale a: {horas} hora(s), {minutos} minuto(s) e {segundos_restantes} segundo(s).")
