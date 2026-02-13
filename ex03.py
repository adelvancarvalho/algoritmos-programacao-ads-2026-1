# Entrada

minutos_input = int(input("Digite um valor em minutos: "))

# Processamento

horas = minutos_input // 60 

minutos_restantes = minutos_input % 60

# Saída

print(f"{minutos_input} minutos equivalem a: {horas} horas e {minutos_restantes} minutos")