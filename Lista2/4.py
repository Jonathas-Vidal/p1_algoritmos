number = int(input('Digite um número inteiro e veja se ele é primo ou não: '))

if number > 1:
    for i in range(2, number):
        if(number % i) == 0:
            print(f'{number} não é primo.')
        else:
            print(f'{number} é primo')
