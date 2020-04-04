def my_func(x, y):
    try:
        div_n = (int(x) / int(y))
        return print(div_n)
    except ValueError:
        return print('You have entered string!')
    except ZeroDivisionError:
        return print('Dividing on zero is not allowed!')

my_func(input('Insert first number - ' ), input('Insert second number - '))