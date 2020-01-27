# def my_func(x, y, z):
#     try:
#         sorted_list = [x, y, z]
#         sorted_list = sorted(sorted_list)
#         return print(int(sorted_list[-1]) + int(sorted_list[-2]))
#     except ValueError:
#         return print('You have entered string')
#
#
# my_func(5, 2 , 1)

#записал себе для красоты
def my_func(x, y, z):
    return print(sum(sorted([x, y, z])[1:]))

my_func(5, 2 , 1)