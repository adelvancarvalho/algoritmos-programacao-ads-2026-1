# Entrada

meses_totais = int(input("Digite a quantidade de meses: "))

# Processamento

anos = meses_totais // 12
meses_restantes = meses_totais % 12

# Saída

print(f"{meses_totais} meses equivalem a: {anos} ano(s) e {meses_restantes} mês(es).")