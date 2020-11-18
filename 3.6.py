def int_func():
    words = input("Введите слова из маленьких латинских букв").split()
    words_copy = []
    for i in range(len(words)):
        word_list = words[i].split()
        for ind in range(len(word_list)):
            k = " ".join(word_list[ind]).split()
            words_copy.append(words[i])
            for index in range(len(k)):
                if ord(k[index]) < 97 or ord(k[index]) > 122:
                    words_copy.remove(words[i])
                    break

    print(" ".join(words_copy).title())


int_func()
