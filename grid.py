from square import Square


class Grid:
    def __init__(self, screen, grid_size, square_size, spacing):
        self.grid = []
        self.grid_size = grid_size
        self.square_size = square_size
        self.spacing = spacing

        self.screen = screen
        x = 0
        y = 0
        row = []
        for rec in range(self.grid_size * self.grid_size):
            x += 1
            if rec % self.grid_size == 0:
                x = 0
                if rec != 0:
                    y += 1
                    self.grid.append(row)
                    row = []
            row.append(Square(x - 1 , y - 1, self.screen, self.square_size, self.spacing))
        self.grid.append(row)

