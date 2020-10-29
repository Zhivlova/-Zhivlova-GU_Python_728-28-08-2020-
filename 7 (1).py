class Matrix:
    def __init__(self, n_1, n_2, n_3):
        self.n_1 = n_1
        self.n_2 = n_2
        self.n_3 = n_3

    def __add__(self, other):
        return Matrix(self.n_1 + other.n_1, self.n_2 + other.n_2, self.n_3 + other.n_3)

    def __str__(self):
        return f'Матрица ({self.n_1}, {self.n_2}, {self.n_3})'

m1 = Matrix([1, 4, 5],
    [5, 8, 9],
    [6, 7, 11])

m2 = Matrix ([9, 4, 5],
    [5, 8, 9],
    [6, 7, 15])

    for x in range(m1[1]):
        for y in range(m2[0]):
            res[x+y] = m1[x,y] + m2[x,y]
print('\nResult :\n', res)