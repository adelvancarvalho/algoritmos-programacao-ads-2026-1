# Entrada

a = float(input("Coeficiente a: "))
b = float(input("Coeficiente b: "))
c = float(input("Coeficiente c: "))
d = float(input("Coeficiente d: "))
e = float(input("Coeficiente e: "))
f = float(input("Coeficiente f: "))

# Processamento

divisor = (a * e) - (b * d)

x = (c * e - b * f) / divisor
y = (a * f - c * d) / divisor

# Saída

print(f"O valor de X é: {x}")
print(f"O valor de Y é: {y}")
