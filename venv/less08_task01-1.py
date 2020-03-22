class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Всё в порядке'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('24 - 02 - 2020')
print(today)
print(Data.valid(11, 13, 2022))
print(today.valid(26, 10, 2020))
print(Data.extract('11 - 11 - 2011'))
print(today.extract('24 - 02 - 2020'))
print(Data.valid(24, 11, 2020))


#  ------------------------------------------- вариант решения ---------------------------------------------------------

class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def change_type(cls, data):
        return f'День {int(data[0]):02d}, Месяц {int(data[1]):02d}, Год {int(data[2])}'

    @staticmethod
    def validation(data):
        if not int(data[0]) in range(1, 32) or not int(data[1]) in range(1, 13) or int(data[2]) > 2020:
            return 'Введена некоррекная дата!'

    def data_func(self):
        result_1 = Data.change_type(self.data.split('-'))
        result_2 = Data.validation(self.data.split('-'))
        return result_2 if result_2 else f'Переформатированная дата (тип int)\n{result_1}'


user_data = input('Введите дату (чч-мм-гг): ')
mc = Data(user_data)
print(mc.data_func())
user_data = input('Введите дату (чч-мм-гг): ')
mc_2 = Data(user_data)
print(mc_2.data_func())
print(mc.data_func())