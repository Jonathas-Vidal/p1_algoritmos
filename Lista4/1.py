x = 3
y = 4
z = 0.6

print(x + x * x ** (y * x) / z)

# Seguindo a ordem de precedência, será feita a operação entre parenteses (y * x), após isso a potenciação
# Em seguida a multiplicação, a divisão e por fim a soma.

print(((not(x + z < y)) or (x + x * z >= y )) and True)

# Devido ao operador 'or' que necessita de apenas um resultado ser True para que ele seja True, o operador not inverteu
# o resultado da expressão, que era false mas virou true.
# Sendo assim, true + true = true.