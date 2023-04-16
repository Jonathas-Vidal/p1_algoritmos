num = int(input('Insira um número para ver sua tabuada até 20: '))
crescente = 0

for i in range(0, 21):
    print(f'{num}x{crescente} = {num * crescente}')
    crescente += 1
