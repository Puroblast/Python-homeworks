class MyError(Exception):
    pass


my_list = []
while True:
    x = input("Введите число,для выхода напишите stop: ")
    if x == 'stop':
        if my_list == []:
            print("Числа не были введены")
        else:
            print(my_list)
        break
    try:
        if x.isdigit() is True:
            my_list.append(int(x))
        else:
            try:
                my_list.append(float(x))
            except ValueError:
                raise MyError
    except MyError:
        print("Вводите числа")
