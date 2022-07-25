""" Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.  """


def inputNumbers(x):
    xyz = ["X", "Y", "Z"]  # Это список
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))  # метод a.(обращение к списку (он пока что пустой)
        # далее идет сам метод append(что значит добавить) добавляющий
        # новые элементы в список)
    return a


def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")
