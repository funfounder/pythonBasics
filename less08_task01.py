class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day} {self.month} {self.year}'

class Date_formating:

    @classmethod
    def splt(cls, date):
        date_list = date.split('-')
        day = int(date_list[0])
        month = int(date_list[1])
        year = int(date_list[2])
        return Date(day, month, year)

    @staticmethod
    def check(date: Date):
        return 0 < date.day <= 31 and 0 < date.month <= 12 and date.year > 0

date = Date_formating()
print(date.splt('12-04-1994'))
