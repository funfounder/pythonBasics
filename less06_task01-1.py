# import time
# import itertools
#
# class TrafficLight:
#     __color = [['red',[7, 31]], ['yellow', [2, 33]], ['green',[4, 32]], ['yellow', [2, 33]]]
#
#     def running(self):
#         for el in itertools.cycle(self.__color):
#             print(f"\r\033[{el[1][1]}m\033[1m{el[0]}\033[0m", end="")
#             time.sleep(el[1][0])
#
# light = TrafficLight()
# light.running()
#
#
# -------------

# from time import sleep
# from itertools import cycle
# import datetime
#
#
# class TrafficLight:
#     def __init__(self, go, wait, stop):
#         self.__color = [go, wait, stop]
#
#     def running(self):
#         t = str(datetime.datetime.time(datetime.datetime.now()))
#         correct_order = ['red', 'yellow', 'green']
#         new_list = [i for i in self.__color if i == correct_order[self.__color.index(i)]]
#         if len(new_list) < 3:
#             print('Wrong order')
#         else:
#             self.__color.append('yellow')
#             for i in cycle(self.__color):
#                 if i == 'yellow':
#                     print(f'\033[33m{i}')
#                     sleep(2)
#                 elif i == 'red':
#                     print(f'\033[31m{i}')
#                     sleep(7)
#                 else:
#                     print(f'\033[32m{i}')
#                     sleep(7)
#                 if 0 <= int(t[:2]) <= 5:
#                     break
#
#
# a = TrafficLight('red', 'yellow', 'green')
# a.running()

#--------------------

# from time import sleep
#
#
# class TrafficLight:
#     __color = 0
#
#     def running(self):
#         # [красный, жёлтый, зелёный]
#         lights = [
#             {
#                 'name': 'красный',
#                 'color': '\x1b[41m',
#                 'delay': 7
#             },
#             {
#                 'name': 'жёлтый',
#                 'color': '\x1b[43m',
#                 'delay': 2
#             },
#             {
#                 'name': 'зелёный',
#                 'color': '\x1b[42m',
#                 'delay': 5
#             }
#         ]
#
#         print('\nИмитация работы светофора:\n')
#
#         while True:
#             # формируем строку вывода (светофор)
#             s = ''
#             for i in range(3):
#                 if i == self.__color:
#                     s += f'({lights[self.__color]["color"]}   \x1b[0m)'
#                 else:
#                     s += '(   )'
#
#             print(f'\r{s}', end='')
#             # устанавливаем задержку
#             sleep(lights[self.__color]["delay"])
#             # меняем цвет
#             self.__color = (self.__color + 1) % 3
#
#
# lights = TrafficLight()
# lights.running()