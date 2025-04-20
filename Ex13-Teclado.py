num_pad = ((1, 2, 3), 
           (4, 5, 6), 
           (7, 8, 9), 
         ("*", 0, "#")) # Isso e uma Tupla 2D

for linha in num_pad:
    for num in linha:
        print(num, end= ' ')
    print()