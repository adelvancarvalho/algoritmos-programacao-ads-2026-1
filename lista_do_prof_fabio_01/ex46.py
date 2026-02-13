# Entrada

valor_mercadoria = int(input("Valor da mercadoria: R$ "))

# Processamento

prestacao = valor_mercadoria // 3

entrada = valor_mercadoria - (prestacao * 2)

# Saída

print(f"Valor da Entrada: R$ {entrada}")
print(f"2 Prestações de : R$ {prestacao}")


