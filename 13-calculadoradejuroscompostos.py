# Calculadora de juros compostos

entrada = 0
taxa = 0
tempo = 0

while entrada <= 0:
    entrada = float(input("Coloque a entrada: "))
    if entrada <= 0:
        print("A entrada não pode ser menor ou igual a zero")

while taxa <= 0:
    taxa = float(input("Coloque a taxa: "))
    if taxa <= 0:
        print("A taxa não pode ser menor ou igual a zero")

while tempo <= 0:
    tempo = int(input("Coloque o tempo em anos: "))
    if tempo <= 0:
        print("O tempo não pode ser menor ou igual a zero")

total = entrada * pow((1 + taxa / 100), tempo)

print(f"O total dos seus investimentos de {entrada} a taxa de {taxa}% ao ano, por {tempo} anos será igual a: R${total:.2f}")