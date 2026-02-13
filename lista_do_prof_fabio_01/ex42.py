# Entrada

print("--- Ponto 1 ---")
x1 = float(input("Digite x1: "))
y1 = float(input("Digite y1: "))

print("--- Ponto 2 ---")
x2 = float(input("Digite x2: "))
y2 = float(input("Digite y2: "))

# Processamento

parte_x = (x2 - x1) ** 2
parte_y = (y2 - y1) ** 2

distancia = (parte_x + parte_y) ** 0.5

# Saída

print(f"A distância entre os pontos é: {distancia:.2f}")
