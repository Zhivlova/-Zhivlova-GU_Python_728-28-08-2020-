class Road:

    def __init__(self, _road_length, _road_width):
        self._road_length = int(20)
        self._road_width = int(5000)
        self.weight1 = int(25)
        self.thickness = int(5)

    def weight(self):
        weight = self._road_length * self._road_width * self.weight1 * self.thickness / 1000

road1 = Road(5000, 20)
print(road1.weight())