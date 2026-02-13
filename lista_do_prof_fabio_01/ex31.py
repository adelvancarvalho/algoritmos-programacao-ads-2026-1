# Entrada

binario = int(input("Digite um número binário de 4 dígitos: "))

# Processamento

d3 = binario // 1000             
d2 = (binario // 100) % 10       
d1 = (binario // 10) % 10        
d0 = binario % 10                

decimal = (d3 * 8) + (d2 * 4) + (d1 * 2) + (d0 * 1)

# Saída

print(f"O binário {binario} corresponde ao decimal: {decimal}")
