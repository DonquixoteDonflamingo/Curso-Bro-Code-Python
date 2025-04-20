#  Coleções = "Variável" única usada para armazenar vários valores
#     Lista = [] Ordenado e alterável. Duplicatas permitidas.
# Conjuntos = {} Não ordenado e imutável, mas Adicionar/Remover OK. Sem duplicatas
#    Tuplas = () Ordenado e imutável. Duplicatas OK. MAIS RÁPIDO

frutas = ["Maça", "Laranja", "Banana", "Coco", "Abacaxi"]

# print(dir(frutas))
# print(help(frutas))
# print(frutas[::-1])
# for fruta in frutas:
#     print(fruta)

# print(len(frutas)) # Para saber o tamanho da lista
# print("Maça" in frutas) # Retona se um valor especifico esta contido na lista. Retorna um Bool

# frutas[0] = "Bomba" # Os valores de uma lista podem ser alterados

# frutas.append("Bomba") # .append anexa um elemento ao final da lista
# frutas.remove("Maça") # Retira um elemento da especifico da lista
# frutas.insert(0, "Bomba") # Insere um elemento em um index especificado
# frutas.sort() # Classifica a lista em ordem
# frutas.reverse() # Inverte uma lista. Não oinverte em ordem alfabetica mas sim na ordem em que aparecem
#                  # na lista.
# Para reverter uma lista em ordem alfabetica usa-se primeiro o .sort() depois o .reverse()
# frutas.clear() # Limpa uma lista
# print(frutas.index("Maça")) # Printa o index de um determinado elemento
# print(frutas.count("Banana")) # Conta quantas vezes determinado elemento aparece em uma lista
