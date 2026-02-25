def main():
    # 1. Entrada
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = input("Escolha a operação (+, -, *, /): ")

    # 2. Processamento
    resultado = 0
    calculo_valido = True 

    if operacao == '+':
        resultado = numero1 + numero2
    elif operacao == '-':
        resultado = numero1 - numero2
    elif operacao == '*':
        resultado = numero1 * numero2
    elif operacao == '/':
        if numero2 == 0:
            calculo_valido = False  
        else:
            resultado = numero1 / numero2
    else:
        calculo_valido = False      

    # 3. Saída
    if calculo_valido == True:
        print(f"O resultado de {numero1} {operacao} {numero2} é: {resultado}")
    else:
        print("Erro! Operação inválida ou você tentou dividir por zero.")

if __name__ == "__main__":
    main()
    