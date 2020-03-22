class MyDivisionZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


div = lambda x, y: x / y if y != 0 else MyDivisionZeroError('Ошибка дедения на 0!!')

print(div(1, 0))

print(div(4, 2))
