#  Entrada

kg_latao = float(input("Quantos Kg de latão você quer produzir? "))

# Processamento

qtd_cobre = kg_latao * 0.70
qtd_zinco = kg_latao * 0.30

# Saída

print(f"Você vai precisar de {qtd_cobre:.2f} kg de Cobre.")
print(f"Você vai precisar de {qtd_zinco:.2f} kg de Zinco.")
