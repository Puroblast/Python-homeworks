with open("text_3.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    income = 0
    for i in range(len(lines)):
        words = lines[i].split()
        if float(words[1]) < 20000:
            print(f"{words[0]} имеет оклад равный {words[1]}")
        income += float(words[1])
    print(f"Средний доход составляет {income / len(lines)}")
