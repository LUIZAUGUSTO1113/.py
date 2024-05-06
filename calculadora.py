def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a // b
    else:
        return "Não é possível dividir por zero."

def calculadora():
    print("Bem-vindo sou a calculadora!")

    while True:
        print("Escolha uma opção:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite qual a operação desejada: ")

        if escolha == '5':
            print("Obrigado por utilizar a calculadora!")
            break

        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        if escolha == '1':
            resultado = soma(num1, num2)
        elif escolha == '2':
            resultado = subtracao(num1, num2)
        elif escolha == '3':
            resultado = multiplicacao(num1, num2)
        elif escolha == '4':
            resultado = divisao(num1, num2)
        else:
            resultado = "Opção inválida. Por favor, escolha uma operação válida."

        print("Resultado: ", resultado)

        continuar = input("Deseja realizar outra operação? (Digite 's' para sim, 'n' para não): ")
        if continuar != 's':
            print("Obrigado por utilizar a calculadora!")
            break

calculadora()
# quando o resultado for quebrado???