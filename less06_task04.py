class Auto:
    '''Car object'''

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'This is a new car: {self.name}, {self.color}, police car - {self.is_police}')

    def go(self):
        print(f'{self.name}: car run.')

    def stop(self):
        print(f'{self.name}: car stopped.')

    def turn(self, direction):
        print(f'{self.name}: car turned {"right" if direction == 0 else "left"}.')

    def show_speed(self):
        return f'{self.name}: car speed is {self.speed}'

class Town(Auto):
    '''City car'''
    def show_speed(self):
        return f'{self.name}: car speed is {self.speed}. Warning: speed exceed!' \
            if self.speed > 60 else f'{self.name}: car speed is {self.speed}'

class Work(Auto):
    '''Duty car'''
    def show_speed(self):
        return f'{self.name}: car speed is {self.speed}. Warning: speed exceed!' \
            if self.speed > 40 else f'{self.name}: car speed is {self.speed}'

class Race(Auto):
    '''Sport car'''

class Police(Auto):
    '''Police car'''
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = Police('"NYPD"', 'black', 100)
police_car.go()
print(police_car.show_speed())
police_car.turn(1)
police_car.stop()
print()

work_car = Work('"Ford"', 'green', 40)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()

print()
sport_car = Race('"Porsche"', 'red', 180)
sport_car.go()
sport_car.turn(0)
print(sport_car.show_speed())
sport_car.stop()
print()

town_car = Town('"Toyota"', 'white', 60)
town_car.go()
town_car.turn(1)
town_car.turn(0)
print(town_car.show_speed())
town_car.stop()

print(f'\nCar {town_car.name} (color {town_car.color})')
print(f'Car {police_car.name} (color {police_car.color})')