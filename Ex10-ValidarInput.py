# Exercício de validação de entrada do usuário
# 1. O nome de usuário não deve ter mais de 12 caracteres
# 2. O nome de usuário não deve conter espaços
# 3. O nome de usuário não deve conter dígitos

username = input("Coloque um noem de usuario: ")

if len(username) > 12:
    print("Seu nome de usuario não pode ter mais de 12 caracteres")
elif not username.find(" ") == -1:
    print("Seu nome de usuario não pode conter espaços em branco")
elif not username.isalpha():
    print("Seu nome de usuario não pode conter numeros")
else:
    print(f"Bem-Vindo {username}")