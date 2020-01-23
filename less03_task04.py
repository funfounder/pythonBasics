def my_func():
    try:
        x = int(input('Insert positive real number: '))
        y = int(input('Insert negative integer: '))
        if x > 0 and y < 0:
            return print(x ** y)
        else:
            return print('Your input is wrong!')
    except ValueError:
        return print('Your input is wrong!')


my_func()

def my_func():
    try:
        x = int(input('Insert positive real number: '))
        y = int(input('Insert negative integer: '))
        if x > 0 and y < 0:
            abs_y = abs(y)
            i = 1
            z = x * abs_y
            while i != abs_y:
                z = z * abs_y
            z = 1 / z
            return print(z)
        else:
            return print('Your input is wrong!')
    except ValueError:
        return print('Your input is wrong!')


my_func()