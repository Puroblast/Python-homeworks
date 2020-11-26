import re

with open("text_6.txt", "r", encoding="utf-8") as file:
    lines = file.read().split("\n")
    numbers = []
    final_numbers = []
    for key in lines:
        value = re.findall("\d+", key)
        numbers.append(value)
    for number in numbers:
        summ = 0
        for i in number:
            summ += int(i)
        final_numbers.append(summ)
    hours = {}
    keys = []

    for ind in lines:
        word = ind[:ind.find(":") + 1]
        keys.append(word)
    for _ in range(len(final_numbers)):
        hours[keys[_]] = final_numbers[_]

    print(hours)
