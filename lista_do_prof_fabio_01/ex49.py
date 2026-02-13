# Entrada

capital = float(input("Capital inicial a investir: R$ "))
taxa = float(input("Taxa de juros mensal"))
meses = int(input("Tempo em meses: "))

# Processamento

# Ajuste da taxa (5 virar 0.05)
i = taxa / 100

juros_simples = capital * i * meses
total_simples = capital + juros_simples

# A formula é M = C * (1 + i) elevado ao tempo
total_composto = capital * ((1 + i) ** meses)

diferenca = total_composto - total_simples

# Saída

print("--- Comparativo de Investimento ---")
print(f"Rendimento Juros Simples:   R$ {total_simples:.2f}")
print(f"Rendimento Juros Compostos: R$ {total_composto:.2f}")
print(f"A mágica dos juros compostos gerou R$ {diferenca:.2f} a mais!")

