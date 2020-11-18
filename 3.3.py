def max_sum(a, b, c):
    my_list = [a, b, c]
    my_list.sort(reverse=True)
    print("Сумма двух максимальных чисел будет равна: " + str(sum(my_list[:2])))


while True:
    try:
        max_sum(int(input("Введите первое число: ")), int(input("Введите второе число: ")),
                int(input("Введите третье число: ")))
        break
    except ValueError:
        print("Вводите числа")
