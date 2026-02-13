# Entrada

numero = int(input("Digite um número de 4 dígitos (ex: 9534): "))

# Processamento

milhar = numero // 1000
centena = (numero // 100) % 10
dezena = (numero // 10) % 10
unidade = numero % 10

soma_elementos = milhar + centena + dezena + unidade

# Saída

print(f"A soma dos elementos ({milhar}+{centena}+{dezena}+{unidade}) é: {soma_elementos}")
