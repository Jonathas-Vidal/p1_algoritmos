num = int(input('Insira um elemento da sequência de Fibonacci: '))
anterior = 1
proximo = 1
temp = 0
for i in range(num):
    print(anterior)
    temp = anterior
    anterior = proximo
    proximo = anterior + temp
