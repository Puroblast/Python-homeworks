gain = int(input("Введите сумму вашей выручки: "))
costs = int(input("Введите сумму ваших издержек: "))
if gain > costs:
    income_per_person = int(input("Введите количество сотрудников в вашей фирме: ")) / (gain - costs)
    profit = (gain - costs) / gain
    print(
        f"Поздравляю, ваша фирма успешна!\nВаша рентабельность составляет: {profit}"
        f"\nПрибыль фирмы на одного сотрудника составляет: {income_per_person:.3f}"
    )
elif gain == costs:
    print("Ваша фирма работает в 0")
else:
    print("Ваша фирма приносит убытки")
