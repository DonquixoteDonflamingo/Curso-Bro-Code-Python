# Quiz Game

questões = ("Quantos elementos tem na tabela periodica?: ",
            "Qual animal põe o maior ovo?: ",
            "Qual o gás mais abundante na atmosfera terrestre?: ",
            "Quantos ossos existem no corpo humano?: ",
            "Qual é o planeta mais quente do sistema solar?: ")

opções = (("A. 116", "B. 117", "C. 118", "D. 119"), 
          ("A. Baleia", "B. Crocodilo", "C. Elefante", "D. Avestruz"), 
          ("A. Nitrogenio", "B. Oxigenio", "C. Carbono", "D. Hidrogenio"), 
          ("A. 206", "B. 207", "C. 208", "D. 209"), 
          ("A. Mercurio", "B. Venus", "C. Terra", "D. Marte"))

respostas = ("C", "D", "A", "A", "B")
palpites = []

score = 0

questão_num = 0

for questão in questões:
    print("--------------------------------------------------")
    print(questão)
    for opção in opções[questão_num]:
        print(opção)
    
    palpite = input("Escolha entre (A, B, C, D): ").upper()
    palpites.append(palpite)
    if palpite == respostas[questão_num]:
        score += 1
        print("CORRETO!")
    else:
        print("INCORRETO!")
        print(f"{questões[questão_num]} é a resposta correta!")
    questão_num += 1

print("--------------------------------------------------")
print("                   RESULTADOS                     ")
print("--------------------------------------------------")

print("Respostas: ", end= '')
for resposta in respostas:
    print(resposta, end= ' ')
print()

print("Palpites: ", end= '')
for Palpite in palpites:
    print(Palpite, end= ' ')
print()

score = int(score / len(questões) * 100)
print(f"Seu score e de: {score}%")