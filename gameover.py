import pygame as pg


class GameOver:
    def __init__(self, screen, width):
        self.status = False
        self.screen = screen
        self.width = width
        self.font = pg.font.Font("freesansbold.ttf", 32)

    def show_game_over(self):
        self.screen.blit(
            self.font.render("Game Over", True, "black", "red"),
            pg.draw.rect(
                self.screen,
                "orange",
                pg.Rect(
                    self.width / 2,
                    self.width / 2,
                    0,
                    0,
                ),
            ),
        )
    
    def reset(self):
        self.status = False
