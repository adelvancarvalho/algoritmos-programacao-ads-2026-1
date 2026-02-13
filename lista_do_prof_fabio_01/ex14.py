# Entrada

nota1 = float(input("Digite a 1ª nota: "))
peso1 = float(input("Digite o peso da 1ª nota: "))

nota2 = float(input("Digite a 2ª nota: "))
peso2 = float(input("Digite o peso da 2ª nota: "))

nota3 = float(input("Digite a 3ª nota: "))
peso3 = float(input("Digite o peso da 3ª nota: "))

# Processamento

soma_pesos = peso1 + peso2 + peso3
soma_notas_com_peso = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)

media_ponderada = soma_notas_com_peso / soma_pesos

# Saída

print(f"A média ponderada do aluno é: {media_ponderada:.2f}")