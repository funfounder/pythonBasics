# def my_func():
#     try:
#         x = int(input('Insert positive real number: '))
#         y = int(input('Insert negative integer: '))
#         if x > 0 and y < 0:
#             return print(x ** y)
#         else:
#             return print('Your input is wrong!')
#     except ValueError:
#         return print('Your input is wrong!')
#
#
# my_func()


# устранил проблему с бесконечным циклом
# def my_func():
#     try:
#         x = int(input('Insert positive real number: '))
#         y = int(input('Insert negative integer: '))
#         if x > 0 and y < 0:
#             abs_y = abs(y)
#             i = 1
#             z = x * abs_y
#             while i < abs_y:
#                 z = z * abs_y
#                 i += 1
#             return print(1 / z)
#         else:
#             return print('Your input is wrong!')
#     except ValueError:
#         return print('Your input is wrong!')

#улучшил, подсмотрел реализацию через for in
def my_func():
    try:
        x = int(input('Insert positive real number: '))
        y = int(input('Insert negative integer: '))
        if x > 0 and y < 0:
            z = x * abs(y)
            for i in range(abs(y)-1):
                z *= x
            return print(1 / z)
        else:
            return print('Your input is wrong!')
    except ValueError:
        return print('Your input is wrong!')


my_func()