# Typecasting = O processo de conversão de uma variável de um tipo de dado para outro
#               str(), int(), float(), bool()

nome = "Gustavo Alves"
idade = 20
nota =  7.7
e_estudante = True

# Voce pode descobrir o tipo de dado de uma variavel usando a função type(variavel)
# print(type(e_estudante))
# Se voce fosso adicionar idade += 1 daria erro, mas, se colocar idade += "1" daria = 251 :)
nome = bool(nome)


print(nome)