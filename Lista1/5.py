number1 = int(input("Insira um número e descubra o maior ou menor: "))
number2 = int(input("Insira mais um número e descubra o maior ou menor: "))

if number1 > number2:
    print(f"O número {number1} é maior que o {number2}!")
elif number2 > number1:
    print(f'O número {number2} é maior que o {number1}!')
else:
    print("Os numeros são iguais!")
