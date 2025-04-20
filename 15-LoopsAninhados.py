# Loops Aninhados = Um loop dentro de outro loop (externo, interno)
#                   loop externo:
#                       loop interno:
# Também é o código de um retangulo
linhas = int(input("Coloque o número de linhas: "))
colunas = int(input("Coloque o número de colunas: "))

simbolo = input("Coloque um símbolo a ser usado: ")


for j in range(linhas):
    for i in range(colunas):
        print(simbolo, end=" ")
    print()