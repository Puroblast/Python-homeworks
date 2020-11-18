def my_func(x, y):
    print(x ** y)
    """Второй вариант решения"""
    z = x
    for i in range(-1, y, -1):
        z *= x
    print(1 / z)


while True:
    try:
        x = int(input("Введите целое положительное число: "))
        if x < 0:
            raise ValueError
        break
    except ValueError:
        print("Вводите ЦЕЛОЕ ПОЛОЖИТЕЛЬНОЕ число")

while True:
    try:
        y = int(input("Введите целое отрицательное число: "))
        if y >= 0:
            raise ValueError
        break
    except ValueError:
        print("Вводите ЦЕЛОЕ ОТРИЦАТЕЛЬНОЕ число")
my_func(x, y)
