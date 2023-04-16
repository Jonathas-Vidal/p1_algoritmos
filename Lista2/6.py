n = int(input("Insira um valor e veja seu fatorial: "))
fatorial: int = 1

for i in range(1, n+1):
    fatorial *= i

print(f"O fatorial de {n} é {fatorial}")
