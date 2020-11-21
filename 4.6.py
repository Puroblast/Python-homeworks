from itertools import count, cycle
my_list = []
while True:
    try:
        min_count = int(input("Введите начало отсчёта: "))
        break
    except ValueError:
        print("Введите число")
while True:
    try:
        max_count = int(input("Введите конец отсчёта: "))
        break
    except ValueError:
        print("Введите число")
try:
    for el in count(min_count):
        if el > max_count:
            raise ValueError
        else:
            my_list.append(el)
except ValueError:
    try:
        for el in cycle(my_list):
            if el >= max_count:
                print(el)
                raise ValueError
            else:
                print(el)
    except ValueError:
        print("Конец программы :)")
