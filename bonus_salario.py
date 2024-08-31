salario = int(input("Qual o seu salário? "))
moradores = int(input("Quantas pessoas moram com você? "))
bonus = (float(moradores * (salario * 0.1)))
print(f"O seu salário será de R${salario + bonus:.2f}")