# -*- coding: utf-8 -*-
"""
pow_vs_operator.py

Explicação detalhada das diferenças entre o operador ** e a função pow() em Python.
Todos os detalhes estão como comentários, seguidos de exemplos de uso.
"""

# 1. Sintaxe e precedência
# ** é um operador infix (parte da gramática da linguagem).  
# pow() é uma função built-in.  
# A precedência difere: o operador de negação (-) tem precedência menor que **, mas em pow() você passa o valor inteiro.
# Exemplo:
print("-3**2 =", -3**2)        # => -(3**2) = -9
print("pow(-3, 2) =", pow(-3, 2))  # => 9

# 2. Exponenciação modular (útil para grandes expoentes ou aplicações criptográficas)
# pow(base, expoente, módulo) calcula (base**expoente) % módulo de forma eficiente.
# Não há equivalente direto usando ** sem gerar um valor intermediário enorme.
# Exemplo:
print("2**10 % 1000 =", 2**10 % 1000)      # => 24 (faz 2**10 = 1024, depois módulo)
print("pow(2, 10, 1000) =", pow(2, 10, 1000))  # => 24 (calcula modularmente)

# 3. Tipos de retorno e restrições
# - Com dois argumentos, pow(x, y) == x**y:
#     * Ambos inteiros → resultado int (pode ser muito grande)
#     * Qualquer float → resultado float
# - Com três argumentos, todos devem ser int e o resultado também é int.
# Exemplos de tipos:
print("type(2 ** 3) =", type(2 ** 3))       # <class 'int'>
print("type(2.0 ** 3) =", type(2.0 ** 3))   # <class 'float'>
print("type(pow(2, 3)) =", type(pow(2, 3))) # <class 'int'>

# 4. Performance
# - ** é ligeiramente mais rápido para exponenciações simples, pois é um operador direto.
# - pow(base, exp, mod) é muito mais eficiente em tempo e memória para exponenciação modular.

# 5. Exemplos práticos consolidados
# Exponenciação simples
print("3 ** 4 =", 3 ** 4)      # => 81
print("pow(3, 4) =", pow(3, 4))  # => 81

# Precedência detalhada
print("-3**2 =", -3**2)        # => -9
print("pow(-3, 2) =", pow(-3, 2))  # => 9

# Modular (eficiência)
print("2**10 % 1000 =", 2**10 % 1000)    # => 24
print("pow(2, 10, 1000) =", pow(2, 10, 1000))  # => 24