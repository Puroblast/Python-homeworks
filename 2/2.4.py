words = input("Введите несколько слов через пробел: ").split()
for ind, word in enumerate(words, 1):
    print(f"{ind}" + "." + f"{word[0:9]}")
