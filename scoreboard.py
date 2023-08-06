import pygame as pg


class Scoreboard:
    def __init__(self, screen, width):
        self.screen = screen
        self.width = width
        self.score = 0
        self.highscore = 0
        self.font = pg.font.Font("freesansbold.ttf", 32)

        # Colours for text
        self.white = (255, 255, 255)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)
        self.orange = (255, 165, 0)

    def draw_score(self):
        pg.draw.rect(
            self.screen,
            "orange",
            pg.Rect(
                0,
                self.width,
                self.width,
                200,
            ),
        )
        self.screen.blit(
            self.font.render("Score: " + str(self.score), True, "black", self.orange),
            pg.draw.rect(
                self.screen,
                "orange",
                pg.Rect(
                    self.width / 2 - 100,
                    self.width + 40,
                    0,
                    0,
                ),
            ),
        )
        self.screen.blit(
            self.font.render("High Score: " + str(self.highscore), True, "black", self.orange),
            pg.draw.rect(
                self.screen,
                "orange",
                pg.Rect(
                    self.width / 2 - 100,
                    self.width + 80,
                    0,
                    0,
                ),
            ),
        )
