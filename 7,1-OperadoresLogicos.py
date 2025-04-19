# Operadores Lógicos = Avalia múltiplas condições (or, and, not)
#                 or = Pelo menos uma condição deve ser Verdadeira
#                and = Ambas as condições devem ser Verdadeiras
#                not = Inverte a condição (nem Falso, nem Verdadeiro)

temp = 30
ensolarado = True

if temp >= 28 and ensolarado:
    print("Esta quente lá fora!")
    print("Tambem esta ensolarado!")
elif temp <= 0 and ensolarado:
    print("Esta frio la fora!")
    print("Tambem esta ensolarado!")
elif 28 > temp > 0 and ensolarado:
    print("Esta quentinho lá fora!")
    print("Tambem esta ensolarado!")
elif temp >= 28 and not ensolarado:
    print("Esta quente lá fora!")
    print("Esta nublado!")
elif temp <= 0 and not ensolarado:
    print("Esta frio la fora!")
    print("Esta nublado!")
elif 28 > temp > 0 and not ensolarado:
    print("Esta quentinho lá fora!")
    print("Esta nublado!")