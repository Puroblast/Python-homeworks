my_list = [7, 5, 3, 3, 2]
i = 0

while True:
    while True:  # точно не уверен будет ли этот цикл работать если его вынести за первый цикл, так как мы теряем
        # ошибку ValueError, поэтому решил сделать цикл в цикле, будет неплохо если вы на разборе этот момент уточните)
        try:
            new_el = int(input("Введите ваш рейтинг: "))
            break
        except ValueError:
            print("Вы ввели неверное значение, попробуйте ещё раз")
    if new_el > my_list[i]:
        my_list.insert(i, new_el)
        break
    elif new_el == my_list[i]:
        my_list.insert(i + my_list.count(my_list[i]), new_el)
        break
    else:
        i += 1

print(my_list)
