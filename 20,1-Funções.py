def mostrar_fatura(username, valor, vencimento):
    print(f"Olá {username}")
    print(f"Sua fatura de valor R${valor:.2f} tem vencimento em {vencimento}")

mostrar_fatura("Gustavo", 450.4778714, "15/09/2027")