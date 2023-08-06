from point import Point
from trail import Trail


class Snake:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.dir = "False"
        self.trail = Trail(
            [
                Point.rand_point(1, grid_size - 1 - 2),
            ]
        )

    def grow(self):
        x = self.trail[0].x
        y = self.trail[0].y
        self.trail._trail.insert(0, Point(x, y))

    def head(self):
        return self.trail[0]

    def move_up(self):
        if self.trail[0].y != 0:
            self.trail.shift_up()
            self.dir = "up"

    def move_down(self):
        if self.trail[0].y != self.grid_size - 1:
            self.trail.shift_down()
            self.dir = "down"

    def move_left(self):
        if self.trail[0].x != 0:
            self.trail.shift_left()
            self.dir = "left"

    def move_right(self):
        if self.trail[0].x != self.grid_size - 1:
            self.trail.shift_right()
            self.dir = "right"

    def reset(self):
        self.dir = "False"
        self.trail = Trail(
            [
                Point.rand_point(1, self.grid_size - 1 - 2),
            ]
        )
