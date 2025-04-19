# indexing = Acessando elementos de uma sequência usando [] (indexing operator)
#            [começo : final : pulo]

cartao_numero = "1234-5678-9012-3456"

# print(cartao_numero[0 : 4])
# print(cartao_numero[5:9])
# print(cartao_numero[5:])
# se precisar do ultimo caractere o index e [-1]
# print(cartao_numero[-1])
# print(cartao_numero[::2])

# ultimos_num = cartao_numero[-4:]
# print(f"XXXX-XXXX-XXX-{ultimos_num}")
# com o index de [::-1] a string e revertida
cartao_numero = cartao_numero[::-1]

print(cartao_numero)