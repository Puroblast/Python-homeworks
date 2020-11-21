i = 1


def fact(n):
    k = 1
    for el in range(1, n):
        k *= (el + 1)
        yield k


while True:
    try:
        g = fact(int(input("Введите число: ")))
        break
    except ValueError:
        print("Введите ЧИСЛО")

for _ in g:
    i += 1
    print(f"!{i}= {_}")
