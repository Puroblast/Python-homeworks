result = int(input("Введите ваш результат пробежки: "))
end_result = int(input("Введите желаемый результат: "))
days = 1
print(f"{days}-й день = {result}")

while result < end_result:
    days += 1
    result = result + result * 0.1
    print(f"{days}-й день = {result:.2} км.")

print(f"Вам потребуется {days} дней чтобы достигнуть результата")
