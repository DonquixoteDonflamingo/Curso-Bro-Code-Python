# Calculadora em Python

operador = input("Coloque um operador (+ - * /): ")
num1 = float(input("Coloque o primeiro numero: "))
num2 = float(input("Coloque o segundo numero: "))

if operador == '+' or '-' or '*' or '/':
    print("Este não é um operador valido!")
elif operador == '+':
    result = num1 + num2
    print(f"O resultado da soma e: {round(result, 2)}")
elif operador == '-':
    result = num1 - num2
    print(f"O resultado da subtracao e: {round(result, 2)}")
elif operador == '*':
    result = num1 * num2
    print(f"O resultado da multiplicacao e: {round(result, 2)}")
elif operador == '/':
    result = num1 / num2
    print(f"O resultado da divisao e: {round(result, 2)}")
else:
    print("Este não é um operador valido!")