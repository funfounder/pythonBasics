class Matrix:
    def __init__(self, args):
        self.args = args

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.args]))

    def __add__(self, other):
        return Matrix([self.args[i][j] + other.args[i][j] for i in range(len(self.args))]
                      for j in range(len(self.args[0])))


a = [[5, 3, 1], [4, 4, 4], [6, 8, 2]]
b = [[7, 6, 4], [5, 4, 3], [1, 9, 7]]

m_1 = Matrix(a)
m_2 = Matrix(b)

print(m_1 + m_2)