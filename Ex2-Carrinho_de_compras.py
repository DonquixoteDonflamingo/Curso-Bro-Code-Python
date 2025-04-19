# Exercicio 2 Carrinho de compras

item = input("Qual item gostaria de comprar?")
preco = float(input("Qual e o preço?"))
quantidade = int(input(f"Quantos de {item}/s voce gostaria de comprar?"))
total = preco * quantidade

print(f"Voce comprou {quantidade} de {item}/s")
print(f"O se total deu R${total}")