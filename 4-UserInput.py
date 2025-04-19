# input() = Uma função que solicita ao usuário a inserção de dados
#           Retorna os dados inseridos como uma string
#           Se quiser fazer alguma coisa com os dados, como por exemplo adicionar 1 a idade colocada, dara erro pois e uma string

nome = input("Qual e o seu nome?:")
idade = int(input("Quantos anos voce tem?:"))
idade += 1
 
print(f"Ola {nome}!")
print("FELIZ ANIVERSARIO!")
print(f"Voce tem {idade} anos de idade")