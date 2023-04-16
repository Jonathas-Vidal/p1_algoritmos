elemento = int(input("Insira até qual número você deseja ver as potências de 2: "))
init = 0
for i in range(0, elemento+1):
    print(f'2 elevado a {init} = {2 ** init}')
    init += 1
