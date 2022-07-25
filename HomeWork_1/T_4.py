'''Напишите программу, которая по заданному номеру четверти,
показывает диапазон возможных координат точек в этой четверти (x и y).'''


def Quarter(num):
    flag = False
    while not flag:
        try:
            number = int(input(num))
            flag = True
        except ValueError:
            print("Это не число")
    return number


def checkQuarter(num):
    if num == 1:
        print("X > 0, Y > 0")
    elif num == 2:
        print("X < 0, Y > 0")
    elif num == 3:
        print("X < 0, Y < 0")
    elif num == 4:
        print("X > 0, Y < 0")
    else:
        print("НЕТ такой четверти!!!")


numberQuarter = Quarter("Введите № четверти: ")
checkQuarter(numberQuarter)
