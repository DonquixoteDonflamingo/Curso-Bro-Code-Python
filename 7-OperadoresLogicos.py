# Operadores Lógicos = Avalia múltiplas condições (or, and, not)
#                 or = Pelo menos uma condição deve ser Verdadeira
#                and = Ambas as condições devem ser Verdadeiras
#                not = Inverte a condição (nem Falso, nem Verdadeiro)

temo = 25
chovendo = False

if temo > 35 or temo < 0 or chovendo:
    print("O evento esta cancelado")
else:
    print("O evento esta de pe!")