# While Loop = Executa algum código ENQUANTO alguma condição permanecer verdadeira
# Lembre-se, tem que ter um meio de sair do loop

num = int(input("Coloque um número de 1 a 10: "))

while num < 1 or num > 10:
    print(f"{num} não é valido!")
    num = int(input("Coloque um número de 1 a 10: "))
print(f"Seu número é: {num}")