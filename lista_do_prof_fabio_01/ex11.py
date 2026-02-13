# Entrada

numero = int(input("Digite um número inteiro de 3 dígitos: "))

# Processamento

unidade = numero % 10
dezena = (numero // 10) % 10
centena = numero // 100

# Remontando o número de trás para a frente

numero_invertido = (unidade * 100) + (dezena * 10) + centena

# Saída

print(f"O inverso de {numero} é: {numero_invertido}")