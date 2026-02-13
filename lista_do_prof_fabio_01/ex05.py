# Entrada

numero = int(input("Digite um número inteiro de 3 dígitos (ex: 452): "))

# Processamento

unidade = numero % 10
dezena = (numero // 10) % 10
centena = numero // 100

soma_digitos = centena + dezena + unidade

# Saída

print(f"A soma dos dígitos é: {soma_digitos}")