# Calcular a hipotenusa

import math as mt

a = float(input("Coloque o tamanho do lado A: "))
b = float(input("Coloque o tamanho do lado B: "))

c = mt.sqrt(pow(a, 2) + pow(b, 2))

print(f"O tamanho do lado C, ou hipotenusa e de: {round(c, 2)}")