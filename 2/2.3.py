month = int(input("Введите месяц года: "))
season = ["Сейчас холодная зима, как отметили?", "Вы находитесь на пороге к Весне, но всё ещё Зима", "Весна наступила!",
          "Весна,скоро купаться!", "Весна,самое прекрасное время года", "Ура Лето пришло!", "Лето, отдыхаем!",
          "Последний месяц Лета, наслаждайтесь", "Осень", "Осень", "Осень,зима близко",
          "Зима, уже готовы отмечать новый год?"]
while True:
    try:
        print(season[month - 1])
        break
    except IndexError:
        month = int(input("Вы ввели невозможный месяц, попробуйте снова: "))
########################################################################################################################
month_dict = {
    1: "Сейчас холодная зима, как отметили?",
    2: "Вы находитесь на пороге к Весне, но всё ещё Зима",
    3: "Весна наступила!",
    4: "Весна,скоро купаться!",
    5: "Весна,самое прекрасное время года",
    6: "Ура Лето пришло!",
    7: "Лето, отдыхаем!",
    8: "Последний месяц Лета, наслаждайтесь",
    9: "Осень",
    10: "Осень",
    11: "Осень,зима близко",
    12: "Зима, уже готовы отмечать новый год?"
}
while True:
    try:
        print(month_dict[month])
        break
    except KeyError:
        month = int(input("Вы ввели невозможный месяц, попробуйте снова: "))
