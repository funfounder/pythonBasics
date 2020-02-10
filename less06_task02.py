class Road:
    def __init__(self, length, width):
            self._length = length
            self._width = width

    def get_result(self):
        result = int(self._length) * int(self._width) * 25 * 5
        print(f'You will need {float(result / 1000):.2f} t of asphalt for the road with length {self._length} m and width {self._width} m')

my_road = Road(1000, 50)
my_road.get_result()
