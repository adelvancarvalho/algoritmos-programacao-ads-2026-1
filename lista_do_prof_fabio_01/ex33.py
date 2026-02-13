# Entrada

numero = int(input("Digite um número de 3 dígitos: "))

# Processamento

c = numero // 100
d = (numero // 10) % 10
u = numero % 10

inverso = (u * 100) + (d * 10) + c
soma = numero + inverso

# Saída
print(f"{numero} + {inverso} = {soma}")
