# Conversor de temperaturas

unid = input("A temperatura esta em Celsius ou Fahrenheit?: ")
temp = float(input("Qual o valor da temperatura?: "))

if unid == 'C':
    temp = round((9 * temp) / 5 + 32, 2)
    print(f"A temperatura em Fahrenheit e de: {temp}")
elif unid == 'F':
    temp = round((temp - 32) * 5 / 9, 2)
    print(f"A temperatura em Celsius e de: {temp}")
else:
    print(f"{unid} <--- Que porra de unidade e essa?")