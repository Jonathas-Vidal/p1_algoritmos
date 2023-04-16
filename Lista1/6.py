number1 = int(input("Insira um número e descubra o menor: "))
number2 = int(input("Insira mais um número e descubra o menor: "))
number3 = int(input("Insira mais um número e descubra o menor: "))

if number1 < number2 and number1 < number3:
    print(f"O número {number1} é o menor!")
elif number2 < number1 and number2 < number3:
    print(f'O número {number2} é o menor!')
elif number3 < number1 and number3 < number2:
    print(f'O número {number3} é o menor')
else:
    print("Você inseriu números iguais!")
