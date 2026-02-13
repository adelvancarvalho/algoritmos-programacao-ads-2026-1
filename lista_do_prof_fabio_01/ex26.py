# Entrada

dias_totais = int(input("Digite a quantidade de dias: "))

# Processamento

semanas = dias_totais // 7
dias_restantes = dias_totais % 7

# Saída

print(f"{dias_totais} dias equivalem a: {semanas} semana(s) e {dias_restantes} dia(s).")
