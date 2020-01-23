def my_func(x, y, z):
    try:
        sorted_list = [x, y, z]
        sorted_list = sorted(sorted_list)
        return print(int(sorted_list[-1]) + int(sorted_list[-2]))
    except ValueError:
        return print('You av entered not a number')


my_func(5, 2 , 1)
