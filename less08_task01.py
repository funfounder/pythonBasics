class Own_Error(Exception):
    def __init__(self, txt):
        self.txt = txt

class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def splt(cls, date_as_string):
        is_date = cls.is_date_valid(date_as_string)
        try:
            if is_date == False:
                raise Own_Error('Wrong date!')
        except Own_Error as err:
            print(err)
            return
        day, month, year = map(int, date_as_string.split('-'))
        date_return = cls(day, month, year)
        return date_return

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

date2 = Date.splt('11-10-2012')

try:
    print(date2.day, date2.month, date2.year)
except:
    print('Something is wrong')