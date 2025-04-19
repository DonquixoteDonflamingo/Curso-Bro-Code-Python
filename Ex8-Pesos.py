# Calculadora de pesos

peso = float(input("Coloque o peso: "))
unid = input("Esta em KG ou LB? (K ou L): ")

if unid == 'K':
    peso *= 2.205
    unid = "Lbs."
    print(f"O seu peso e de: {round(peso, 2)} {unid}")
elif unid == 'L':
    peso /= 2.205
    unid = "Kgs."
    print(f"O seu peso e de: {round(peso, 2)} {unid}")
else:
    print(f"{unid} <--- Que porra de unidade e essa?")