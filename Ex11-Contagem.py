import time as tm

# Aqui nosso programa vai "dormir" por um tempinho
# Basicamente ele vai ficar sem fazer nada
# .sleep()
tempo = int(input("Digite o tempo em segundos para o cronômetro: "))

for i in range(tempo, 0, -1):
    segundos = i % 60
    minutos = int(i / 60) % 60
    horas =  int(i / 3600)
    print(f"{horas:02}:{minutos:02}:{segundos:02}")
    tm.sleep(1)

print("O TEMPO ACABOU!")