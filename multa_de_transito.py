via = str(input("Aonde você está dirigindo? Uma rua, uma avenida ou uma rodovia? ")).upper().strip()
velocidade = int(input("Qual velocidade você está dirigindo? "))
if via == ("RUA") and velocidade <= 40:
    print("Parabens, você está dirigindo de maneira segura!")
elif via == ("AVENIDA") and velocidade <= 60:
    print("Parabens, você está dirigindo de maneira segura!")
elif via == ("RODOVIA") and velocidade <= 80:
    print("Parabens, você está dirigindo de maneira segura!")
else:
    print("Tome cuidado, as leis de transito são para proteger todo mundo!")
    multa = float(velocidade * 0.7)
    if via == ("RUA"):
        grau_multa = multa * 3
    elif via == ("AVENIDA"):
        grau_multa = multa * 2
    elif via == ("RODOVIA"):
        grau_multa = multa * 1
    print(f"Você tem uma multa no valor de R$ {grau_multa:.2f}")