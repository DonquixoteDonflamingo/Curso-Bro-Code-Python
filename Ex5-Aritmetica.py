# Calcular a Área de um circulo
import math as mt

raio = float(input("Coloque o raio de um circulo "))
area = mt.pi * pow(raio, 2)

print(f"A area do circulo e de: {round(area, 2)}")