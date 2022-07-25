'''Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Факториал
5! = 120
'''


def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def Factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


fac = InputNumbers("Введите число: ")
print(f"Факторил {fac}  = {Factorial(fac)}")
