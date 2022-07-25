""" Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли
этот день выходным.
Пример: - 6 -> да - 7 -> да - 1 -> нет  """


def InputNumbers(inputText):
    flag = False
    while not flag:
        try:
            number = int(input(f"{inputText}"))
            flag = True
        except ValueError:
            print("Это не число!")
    return number


def checkNumber(num):
    if 6 <= num <= 7:
        print("Yes")
    elif 0 < num < 6:
        print("No")
    else:
        print("число вне пределов 7 дней")


num = InputNumbers("Введите число: ")
checkNumber(num)
