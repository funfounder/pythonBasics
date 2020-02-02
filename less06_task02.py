class Road:
    def __init__(self, _length, _width):
        result = int(_length) * int(_width) * 25 * 5
        print(f'You will need {float(result / 1000): .2f} t of asphalt for the road with length {_length} m and width {_width} m')

my_road = Road(1000, 50)
