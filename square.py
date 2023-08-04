import pygame as pg


class Square:
    def __init__(self, x, y, screen, square_size, spacing):
        self.screen = screen
        self.square_size = square_size
        self.spacing = spacing
        self.x = x
        self.y = y

        self.square = pg.draw.rect(
            screen,
            "green",
            pg.Rect(
                (square_size + spacing) * x  + self.spacing,
                (square_size + spacing) * y  + self.spacing,
                square_size,
                square_size,
            ),
        )

    def red(self):
        self.square = pg.draw.rect(
            self.screen,
            "red",
            pg.Rect(
                (self.square_size + self.spacing) * self.x + self.spacing,
                (self.square_size + self.spacing) * self.y + self.spacing,
                self.square_size,
                self.square_size,
            ),
        )

    def orange(self):
        self.square = pg.draw.rect(
            self.screen,
            "orange",
            pg.Rect(
                (self.square_size + self.spacing) * self.x + self.spacing,
                (self.square_size + self.spacing) * self.y + self.spacing,
                self.square_size,
                self.square_size,
            ),
        )
