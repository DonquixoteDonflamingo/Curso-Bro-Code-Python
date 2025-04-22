# Jogo de advinhar números
import random as rm

baixo_num = 1
alto_num = 100
palpites = 0

resposta = rm.randint(baixo_num, alto_num)

rodando = True

print("Jogo de Advinhar numeros")
print(f"Selecione um número entre {baixo_num} e {alto_num} ")

while rodando:
    palpite = input("Coloque seu número: ")
    if palpite.isdigit():
        palpite = int(palpite)
        palpites += 1
        if palpite < baixo_num or palpite > alto_num:
            print(f"Esse número esta fora do alcance: {palpite}")
            print(f"Selecione um número entre {baixo_num} e {alto_num} ")
        elif palpite < resposta:
            print("Frio! Muito baixo! Tente novamente!")
        elif palpite > resposta:
            print("Frio! Muito alto! Tente novamente!")
        else:
            print(f"CORRETO! A RESPOSTA ERA {resposta}")
            print(f"Número de tentativas até chegar no número: {palpites}")
            rodando = False
    else:
        print("Palpite errado!")
        print(f"Selecione um número entre {baixo_num} e {alto_num} ")