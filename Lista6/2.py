salarioInicial = float(input("Digite seu primeiro salário: "))
anos = int(input("Digite seus anos de trabalho: "))
porcentagem = 0.015
for i in range(anos):
    print(f'{salarioInicial + (salarioInicial * porcentagem)}')
    porcentagem *= 2
