from time import sleep

class TrafficLight:
    def __init__(self, __color):
        i = 0
        while i < 2:
            if __color == 'red':
                print('Now is red')
                sleep(7)
                print('Now is yellow')
                sleep(2)
                print('Now is green')
                sleep(7)
                print('Now is yellow')
                sleep(2)
                i += 1
            elif __color == 'yellow':
                print('Now is yellow')
                sleep(2)
                print('Now is green')
                sleep(7)
                print('Now is yellow')
                sleep(2)
                print('Now is red')
                sleep(7)
                i += 1
            else:
                print('Now is green')
                sleep(7)
                print('Now is yellow')
                sleep(2)
                print('Now is red')
                sleep(7)
                print('Now is yellow')
                sleep(2)
                i += 1

my_light = TrafficLight('green')