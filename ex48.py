# Entrada

distancia = float(input("Distância da viagem (Km): "))
velocidade = float(input("Velocidade média esperada (Km/h): "))
consumo = float(input("Consumo do carro (Km/L): "))
preco_gasolina = float(input("Preço da gasolina (R$): "))

# Processamento

tempo_em_horas = distancia / velocidade 
horas_inteiras = int(tempo_em_horas)    
minutos = (tempo_em_horas - horas_inteiras) * 60 

litros_gastos = distancia / consumo
custo_total = litros_gastos * preco_gasolina

# Saída

print("--- Resumo da Viagem ---")
print(f"Duração estimada: {horas_inteiras} horas e {minutos:.0f} minutos")
print(f"Combustível necessário: {litros_gastos:.1f} Litros")
print(f"Custo total com gasolina: R$ {custo_total:.2f}")

