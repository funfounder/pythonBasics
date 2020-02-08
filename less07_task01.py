class Matrix:
    def __init__(self, args):
        self.args = args

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.args]))

    def __add__(self, other):
        result = []
        num = []
        try:
            for i in range(len(self.args)):
                for j in range(len(self.args[i])):
                    if len(self.args[i]) == len(other.args[i]):
                        num.append(self.args[i][j] + other.args[i][j])
                    else:
                        return "Matrix must be same size!"
                result.append(num)
                num = []
        except IndexError:
            print('Matrix must be same size!')
        return '\n'.join(map(str, result))

m_1 = Matrix([[1, 8], [3, 4], [5, 6]])
m_2 = Matrix([[7, 8], [9, 10], [7, 6]])

print(m_1 + m_2)