number = int(input("Введите целое положительное число: "))
biggest_number = 0
while number >= 1:
    numbers = number % 10
    number = number // 10
    if numbers > biggest_number:
        biggest_number = numbers
print(f"Наибольшее число {biggest_number}")
