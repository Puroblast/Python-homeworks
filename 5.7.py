import json

with open("text_7.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    income_list = []
    summ = 0
    firm_dict = {}
    income_dict = {}
    for words in lines:
        word = words.split()
        income = int(word[2]) - int(word[3])
        if income > 0:
            firm_dict[word[0]] = income
            income_list.append(income)
        else:
            firm_dict[word[0]] = income
    for i in income_list:
        summ += int(i)
    income_dict["average profit"] = summ / len(income_list)
    final_list = [firm_dict, income_dict]
    print(final_list)
    with open("text_77.json", "w", encoding="utf-8") as json_file:
        json.dump(final_list, json_file, ensure_ascii=False)
