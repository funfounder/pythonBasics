a = [[5, 3, 1], [4, 4, 4], [6, 8, 2]]
b = [[7, 6, 4], [5, 4, 3], [1, 9, 7]]

class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        c = []
        for i in range(len(self.lists)):
            c.append([])
            for j in range(len(self.lists[0])):
                c[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, c))

m_1 = Matrix(a)
m_2 = Matrix(b)
print(m_1 + m_2)