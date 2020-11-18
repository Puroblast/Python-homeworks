def divination(a, b):
    try:
        print(round(a / b, 4))
    except ZeroDivisionError:
        print("На ноль делить нельзя.")


while True:
    try:
        divination(int(input("Введите первое число: ")), int(input("Введите второе число: ")))
        break
    except ValueError:
        print("Вы должны ввести число")
