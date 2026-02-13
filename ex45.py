# Entrada

valor_saque = int(input("Qual valor deseja sacar? R$ "))

# Processamento

notas50 = valor_saque // 50
resto = valor_saque % 50

notas10 = resto // 10
resto = resto % 10            

notas5 = resto // 5
resto = resto % 5             

notas1 = resto

# Saída

print("--- Distribuição de Notas ---")
print(f"Notas de R$ 50: {notas50}")
print(f"Notas de R$ 10: {notas10}")
print(f"Notas de R$  5: {notas5}")
print(f"Notas de R$  1: {notas1}")
