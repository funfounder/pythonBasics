#подсмотрел и добавил реализация ошибки некорректного месяца

user_month = int(input('Insert month count: '))
month_dict = {
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11],
    'winter': [12, 1, 2]
}

while user_month < 0 or user_month > 12:
    user_month = int(input('You have entered wrong month. Insert month count: '))

for key, value in month_dict.items():
    if value[0] == user_month:
        print(f'You have inserted {key}')
    elif value[1] == user_month:
        print(f'You have inserted {key}')
    elif value[2] == user_month:
        print(f'You have inserted {key}')


month_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn', 'autumn', 'autumn', 'winter']
print(f'The month refferes to {month_list[user_month-1]}')