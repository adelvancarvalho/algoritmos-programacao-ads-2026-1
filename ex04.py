# Entrada

cotacao_dolar = float(input("Digite o valor atual de 1 Dólar em Reais (R$): "))
valor_em_dolar = float(input("Digite a quantidade de Dólares que você tem (US$): "))

# Processamento

valor_em_real = valor_em_dolar * cotacao_dolar

# Saída

print(f"O valor equivalente é: R$ {valor_em_real:.2f}")