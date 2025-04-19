# Format Specifiers = {:flags} formata um valor com base em quais
#                              sinalizadores são inseridos

# .(number)f = arredondar para esse número de casas decimais (ponto fixo)
# :(number) = alocar tantos espaços
# :03 = alocar e preencher com zeros essa quantidade de espaços
# :< = justificar à esquerda
# :> = justificar à direita
# :^ = alinha centralmente
# :+ = use um sinal de mais para indicar valor positivo
# := coloque o sinal na posição mais à esquerda
# : = insira um espaço antes de números positivos
# :, = separador de vírgula

preço1 = 30000.14159
preço2 = -9800007.65
preço3 = 100002.34

print(f"O preço um e R$ {preço1:+,.2f}")
print(f"O preço dois e R$ {preço2:+,.2f}")
print(f"O preço três e R$ {preço3:+,.2f}")