# Entrada

custo_fabrica = float(input("Digite o custo de fábrica do carro: R$ "))

# Processamento

perc_distribuidor = custo_fabrica * 0.28
perc_impostos = custo_fabrica * 0.45

custo_consumidor = custo_fabrica + perc_distribuidor + perc_impostos

# Saída

print(f"O custo final ao consumidor é: R$ {custo_consumidor:.2f}")
