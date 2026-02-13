# Entrada

n1 = int(input("Numerador 1: "))
d1 = int(input("Denominador 1: "))
n2 = int(input("Numerador 2: "))
d2 = int(input("Denominador 2: "))

# Processamento

novo_denominador = d1 * d2

novo_numerador = (n1 * d2) + (n2 * d1)

# Saída

print(f"A soma das frações é: {novo_numerador}/{novo_denominador}")
