grid = {'rate': 500, 'bonus': 20}

class Worker:
    def __init__(self, name, surname, position):
        self._income = grid
        emploee = {'name': name, 'surname': surname, "position": position, 'income': self._income}
        print(emploee)

class Position(Worker):
    def get_full_name(self):
        print(f'Full name is {Worker.name} {Worker.surname}')
    def get_full_salary(self):
        salary = int(Worker._income[1]) * (1 + (Worker._income[2] / 100))
        print(f'Full salary is {salary}')

my_worker = Position('Josh', 'Grade', 'Asphalter')
print(my_worker.get_full_salary())
print(my_worker.get_full_name())
