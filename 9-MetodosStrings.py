# nome = input("Coloque o seu nome inteiro: ")

# len() = retorna o tamanho da string em int, ele conta " "
# result = len(nome)
# .find = Acha a primeira ocorrencia de um caractere especifico, começa com 0
# result = nome.find(" ") + 1
# .rfind = Acha a ultima ocorrencia de um caractere especifico, começa com 0 
# Quando ele não acha determinado caractere ele retorna -1, como eu coloquei um +1 no final para saber o numero
# do caractere ele vai retornar 0 :P
# result = nome.rfind('Q') + 1
# .capitalize() = Vai deixar a primeira letra de uma string em maisculo, ele retorna uma string
# nome = nome.capitalize()
# .upper = Irá deixar todas as letras em uma string maiusculas, retorna uma string
# nome = nome.upper()
# .lower = Deixa tudo minusculo
# nome = nome.lower()
# .isdigit = Irá retornar True ou False se uma string tiver apenas números
# resultado = nome.isdigit()
# .isalpha = Retorna se uma string contem apenas caracteres, " " não e uma letra então, irá retorar False
# result = nome.isalpha()

numero = input("Coloque o seu numero de telefone: ")

# .count = Conta quantas vezes determiando caractere aparece em uma string
# result = numero.count("-")
# .replace() = Um dos mais uteis, ele substitui qualquer ocorrencia de determinado caractere por outro, retorna uma string
numero = numero.replace("-", "")

print(numero)

# print(help(str))