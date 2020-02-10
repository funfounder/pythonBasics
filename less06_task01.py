from time import sleep

class TrafficLight:
    __color = 'Black'

    def running(self):
        while True:
                print('Now is red')
                sleep(7)
                print('Now is yellow')
                sleep(2)
                print('Now is green')
                sleep(7)
                print('Now is yellow')
                sleep(2)

my_light = TrafficLight()
my_light.running()


