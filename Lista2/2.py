qtd = 5
soma = 0

for i in range(qtd):
    elemento=int(input("Insira os elementos: \n"))
    soma = soma + elemento

media = soma/qtd
print(f"A média dos elementos é {round(media,2)}")