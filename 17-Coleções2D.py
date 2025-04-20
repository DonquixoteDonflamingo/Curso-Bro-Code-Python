frutas =    ["Maça", "Laranja", "Banana", "Coco"]
vegetais =  ["Aipo", "Cenoura", "Batata"]
carnes =    ["Galinha", "Peixe", "Peru"]

mantimentos = [frutas, vegetais, carnes]

for coleção in mantimentos:
    for comida in coleção:
        print(comida, " ")
    print()