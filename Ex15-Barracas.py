# Programa de barracas de concessão?
# dicionario {chave:valor}

menu = {
    "popcorn": 3.00,
    "icecream": 4.50,
    "sinners": 2.50,
    "sentenced": 5.00,
    "forcouped": 7.00,
    "thetown": 1.50,
    "inbrasil": 9.00
}

carrinho = []
total = 0

print("________________MENU_________________")
for chave, valor in menu.items():
    print(f"{chave:10}: R${valor:.2f}")
print("-------------------------------------")

while True:
    comida = input("Selecione um item do menu! (Q para sair) ").lower()
    if comida == 'q':
        break
    elif comida in menu:
        carrinho.append(comida)
        print(f"{comida} adicionado ao carrinho!")
    else:
        print("Item não encontrado. Tente novamente!")

print("-------------------------------------")
for comida in carrinho:
    total += menu.get(comida)
    print(comida:, end=" ")

print()
print(f"O TOTAL DO CARRINHO E DE: R${total:.2f}")