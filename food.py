from point import Point
from trail import Trail


class Food(Point):
    def __init__(self, grid_size, trail):
        self.grid_size = grid_size
        self.trail = trail
        point = Point.rand_point(1, grid_size - 3)
        while trail.has_point(point):
            point = Point.rand_point(1, grid_size - 3)
        super().__init__(point.x, point.y)
        print(point.x, point.y)

    def reset(self):
        self.__init__(self.grid_size, self.trail)
