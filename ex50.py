# Entrada

print("--- Dimensões da Piscina ---")
comprimento = float(input("Comprimento (m): "))
largura = float(input("Largura (m): "))
profundidade = float(input("Profundidade (m): "))
vazao = float(input("Vazão da torneira (Litros por minuto): "))

# Processamento

volume_m3 = comprimento * largura * profundidade
volume_litros = volume_m3 * 1000

minutos_totais = int(volume_litros / vazao)

# 1 dia = 1440 minutos
dias = minutos_totais // 1440
resto_minutos = minutos_totais % 1440

horas = resto_minutos // 60
minutos_finais = resto_minutos % 60

# Saída

print(f"\n--- Resultado Final ---")
print(f"A piscina tem {volume_litros:.0f} Litros.")
print(f"Tempo para encher: {dias} dia(s), {horas} hora(s) e {minutos_finais} minuto(s).")

