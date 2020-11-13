old_list = input("Введите список из нескольких элементов используя пробел: ").split()
for i in range(0, len(old_list), 2):
    if i >= len(old_list) - 1:
        None
    else:
        old_list[i], old_list[i + 1] = old_list[i + 1], old_list[i]

print(old_list)
