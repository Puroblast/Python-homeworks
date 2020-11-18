summ = 0


def my_sum():
    global summ
    for i in range(len(numbers)):
        if numbers[i] == "q":
            break
        summ += int(numbers[i])
    print(summ)


while True:
    numbers = input("Введите числа разделенные пробелом, стоп-слово 'q': ").split()
    try:
        my_sum()
    except ValueError:
        print("Вы ввели значение не по условию")
    if "q" in numbers:
        break
