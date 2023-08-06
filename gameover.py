import pygame as pg


class GameOver:
    def __init__(self, screen, width):
        self.status = False
        self.screen = screen
        self.width = width
        self.font = pg.font.Font("freesansbold.ttf", 40)

    def show_game_over(self):
        text = self.font.render("Game Over!", True, "black", "red")
        text_rect = text.get_rect(center = (self.width/2, self.width / 2),)
        self.screen.blit(text, text_rect)

    def reset(self):
        self.status = False
