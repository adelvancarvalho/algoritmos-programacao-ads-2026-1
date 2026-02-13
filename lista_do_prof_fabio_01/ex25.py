# Entrada

metros_totais = int(input("Digite uma quantidade inteira de metros: "))

# Processamento

km = metros_totais // 1000
metros_restantes = metros_totais % 1000

# Saída

print(f"{metros_totais}m correspondem a: {km} Km e {metros_restantes} metros.")