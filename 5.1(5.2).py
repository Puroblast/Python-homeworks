with open("input.txt", "w", encoding="utf-8") as new_file:
    while True:
        new_str = input("Введите текст,для остановки нажмите 'Enter': ")
        if new_str == "":
            break
        new_file.writelines(f"{new_str}\n")
with open("input.txt", "r", encoding="utf-8") as new_file:
    lines = new_file.readlines()
    print(f"Количество строк в файле = {len(lines)}")
    for i in range(len(lines)):
        words = lines[i].split()
        print(f"Количество слов в строке {i + 1} = {len(words)}")
