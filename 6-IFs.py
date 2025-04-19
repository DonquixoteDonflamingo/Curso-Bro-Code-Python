# If = Execute algum código somente se alguma condição for Verdadeira
#      Caso contrário (else), faça outra coisa

idade = int(input("Coloque a sua idade: "))

if idade  >= 100:
    print("Ta veio pra porra ein")
elif idade < 0:
    print("Voce não nasceu ainda safado!")
elif idade >= 18:
    print("Voce pode beber agora")
else:
    print("Voce deve ter 18+ para beber")