# Carrinho de compras denovo :P

comidas = []
preços = []
total = 0

while True:
    comida = input("Coloque uma comida para comprar (q para sair): ")
    if comida.lower() == 'q':  # Corrigido: 'comida' em vez de 'comidas'
        break
    else:
        preço = float(input(f"Coloque o preço de/o/a {comida}: R$"))
        comidas.append(comida)
        preços.append(preço)

print("----- SEU CARRINHO -----")
print()
for comida in comidas:
    print(comida, end= " | ")

for preço in preços:
    total += preço

print()
print()
print(f"O total de suas compras deu: {total}R$")