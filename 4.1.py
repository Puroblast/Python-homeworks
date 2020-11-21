from sys import argv

name, hours, wage, bonus = argv

print(f"Заработная плата сотрудника: {int(hours) * int(wage) + int(bonus)}")
