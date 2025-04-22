# Dicionarios = Uma coleção de pares {chave:valor}
#               ordenada e alterável. Sem duplicatas

capitais = {"Brasil":"Brasilia",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscou"}

# print(dir(capitais))
# print(help(capitais))

# print(capitais.get("Brasil"))

# if capitais.get("Russia"):
#    print("Essa capital  existe")
# else:
#    print("Essa capital não existe")

# capitais.update({"Alemanha":"Berlin"}) # Ataliza com um novo valor
# capitais.update({"Brasil":"Xique-Xique"}) # Atualiza um valor
# capitais.pop("China") # Retira um item do dicionario
# capitais.popitem() # Retira o ultimo item
# capitais.clear() # Limpa por completo o dicionario

# keys = capitais.keys()    # Para obter todas as chaves de um dicionario,
                          # As chaves são um objeto que se assemelha a uma lista

valores = capitais.values() # Para obter todos os valores de um dicionario
                            # Também retorna um objeto que se assemelha a uma lista

item = capitais.items() # Retorna um objeto de dicionario
                        # Que se assemelha a uma listaa 2D de tuplas

for chave, valor in capitais.items():
    print(f"{chave}: {valor}")