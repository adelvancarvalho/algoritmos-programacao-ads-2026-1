# Entrada

altura = float(input("Altura da parede (m): "))
largura = float(input("Largura da parede (m): "))
qtd_janelas = int(input("Quantas janelas a parede tem? "))

# Processamento

area_total = altura * largura
area_janelas = qtd_janelas * (1.2 * 1.0)
area_pintura = area_total - area_janelas

litros_necessarios = area_pintura / 3

capacidade_lata = 3.6
latas = litros_necessarios / capacidade_lata

# Saída

print(f"--- Relatório do Pintor ---")
print(f"Área real de pintura: {area_pintura:.2f} m²")
print(f"Litros de tinta necessários: {litros_necessarios:.2f} L")
print(f"Você precisará de aproximadamente: {latas:.2f} latas")
