# Return = Instrução usada para encerrar uma função
#          e enviar um resultado de volta ao chamador

def criar_nome(prim, ult):
    prim = prim.capitalize()
    ult = ult.capitalize()
    
    return prim + " "  + ult

nome_int = criar_nome("bob esponja", "calça quadrada")

print(nome_int)