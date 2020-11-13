info = []
feature = {
    "Название": [],
    "Цена": [],
    "Количество": [],
    "Единица": []
}
i = 0
answer = None
while answer != "quit":
    answer = input("Доступные команды: 'add' , 'del' , 'quit' , 'view': ").lower()
    if answer == "add":
        while True:
            i += 1
            item = [input("Введите название товара,если хотите закончить напишите 'выйти': ").title()]
            if item == ['Выйти']:
                break
            feature["Название"] += item
            while True:
                try:
                    cost = [int(input("Введите цену товара: "))]
                    break
                except ValueError:
                    print("Вводите цифрами")
            feature["Цена"] += cost
            while True:
                try:
                    count = [int(input("Введите количество товара: "))]
                    break
                except ValueError:
                    print("Вводите цифрами")
            feature["Количество"] += count
            unit = [input("В чём измеряется количество товара?: ").lower()]
            feature["Единица"] += unit
            info.append((i, {"Название": item, "Цена": cost, "Количество": count, "Единица": unit}))
    elif answer == "view":
        for key in feature:
            print(f"{key}: {feature[key]}")
        for ind in range(len(info)):
            print(info[ind])
    elif answer == "quit":
        print("Хорошего дня!")
        break
    elif answer == "del":
        while True:
            try:
                del_item = input("Введите номер товара который вы хотите удалить, если хотите выйти напишите 'quit': ")
                if del_item == "quit":
                    break
                else:
                    info.pop(int(del_item) - 1)
                    for k in feature:
                        feature[k].pop(int(del_item) - 1)
                    break
            except (ValueError, IndexError):
                print("Вводите цифрами и уже добавленный в программу товар")
    else:
        print("Я пока не знаю такой команды, попробуйте снова")
