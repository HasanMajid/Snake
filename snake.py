from point import Point
from trail import Trail


class Snake:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.length = 1
        self.dir = "False"
        self.trail = Trail(
            [
                Point.rand_point(1, grid_size - 1 - 2),
            ]
        )

    def grow(self):
        self.length += 1

    def head(self):
        return self.trail[0]

    def move_up(self):
        if self.trail[0].y != 0:
            self.trail.shift_up(self.length)
            self.dir = "up"

    def move_down(self):
        if self.trail[0].y != self.grid_size - 1:
            self.trail.shift_down(self.length)
            self.dir = "down"

    def move_left(self):
        if self.trail[0].x != 0:
            self.trail.shift_left(self.length)
            self.dir = "left"

    def move_right(self):
        if self.trail[0].x != self.grid_size - 1:
            self.trail.shift_right(self.length)
            self.dir = "right"

    def reset(self):
        self.dir = "False"
        self.length = 1
        self.trail = Trail(
            [
                Point.rand_point(1, self.grid_size - 1 - 2),
            ]
        )
