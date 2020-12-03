class Matrix:
    def __init__(self, list_1):
        self.list_1 = list_1
        self.b = 0

    def __str__(self):
        return f'{"    ".join(map(str, [i for i in self.list_1]))}'

    def __add__(self, other):
        return [self.list_1[j] + other.list_1[j] for j in range(len(self.list_1))]


matrix = Matrix([1, 2, 3])
matrix_2 = Matrix([3, 4, 4])
print(matrix)
print(matrix_2)
try:
    print(matrix + matrix_2)
except IndexError:
    print("Разная размерность")
