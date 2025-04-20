#  Coleções = "Variável" única usada para armazenar vários valores
#     Lista = [] Ordenado e alterável. Duplicatas permitidas.
# Conjuntos = {} Não ordenado e imutável, mas Adicionar/Remover OK. Sem duplicatas
#    Tuplas = () Ordenado e imutável. Duplicatas OK. MAIS RÁPIDO

# print(len(frutas)) # Para saber o tamanho
# print(dir(frutas))
# print(help(frutas))
# print("Maça" in frutas) # Retona se um valor especifico esta contido na lista. Retorna um Bool

frutas = {"Maça", "Laranja", "Banana", "Coco", "Coco"} # Ele exclui elementos duplicados

# frutas.add("Bomba")
# frutas.remove("Maça")
# frutas.pop() # Remove o primeiro elemento, mas como Conjuntos não são ordenados, ele retira um item aleatorio
# frutas.clear()

print(frutas)