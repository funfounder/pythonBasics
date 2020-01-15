user_number = int(input('Insert nubmer: '))
max_figure = 0
dozens = None
units = 0
if user_number == 0:
    max_figure = 'empty'
elif user_number < 10:
    max_figure = user_number
elif user_number == 10:
    max_figure = 1
elif user_number > 10:
    while dozens != 0:
        dozens = user_number // 10
        units = user_number % 10
        if units > max_figure:
            max_figure = units
        if dozens < 10 and dozens > max_figure:
            max_figure = dozens
        elif dozens < 10 and units > max_figure:
            max_figure = units
        elif dozens > 10:
            user_number = dozens
            dozens = user_number // 10
            units = user_number % 10
            if dozens < 10 and units > max_figure:
                max_figure = units
            elif dozens < 10 and dozens > max_figure:
                max_figure = dozens
            else:
                continue
        break
print(f'Max figure in your number is {max_figure}')
