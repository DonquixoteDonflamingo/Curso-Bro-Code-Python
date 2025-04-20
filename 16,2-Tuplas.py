#  Coleções = "Variável" única usada para armazenar vários valores
#     Lista = [] Ordenado e alterável. Duplicatas permitidas.
# Conjuntos = {} Não ordenado e imutável, mas Adicionar/Remover OK. Sem duplicatas
#    Tuplas = () Ordenado e imutável. Duplicatas OK. MAIS RÁPIDO

frutas = ("Maça", "Laranja", "Banana", "Coco", "Coco")

# print(dir(frutas))
# print(help(frutas))
# print(len(frutas))
# print("Maça", in frutas)
# print(frutas.index("Maça"))
# print(frutas.count("Coco"))

for fruta in frutas:
    print(fruta)