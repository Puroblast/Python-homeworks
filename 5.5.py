with open("text_5.txt", "w", encoding="utf-8") as file:
    summ = 0
    numbers = input("Введите числа разделенные пробелом: ").split()
    file.writelines(" ".join(numbers))
    try:
        for i in range(len(numbers)):
            summ += int(numbers[i])
        print(f"Сумма введенных чисел равна: {summ}")
    except ValueError:
        print("Программа работает только с числами")
