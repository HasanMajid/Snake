import pygame as pg
from snake import Snake
from food import Food
from grid import Grid


class Game:
    def __init__(self):
        grid_size = 12
        grid_size += (
            2  # adding 2 for the outside boundaries, will not be visible on screen
        )
        square_size = 40
        spacing = 1

        # pygame setup
        pg.init()
        width = (square_size + spacing) * grid_size - square_size * 2 - spacing
        height = (square_size + spacing) * grid_size - square_size * 2 - spacing + 200
        pg.display.set_caption("Snake")
        screen = pg.display.set_mode((width, height))
        clock = pg.time.Clock()
        running = True

        scoreboard = Scoreboard(screen, width)
        snake = Snake(grid_size)
        food = Food(grid_size, snake.trail)

        start_ticks = pg.time.get_ticks()  # starter tick

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            keys = pg.key.get_pressed()
            if len(snake.trail) > 1:
                if keys[pg.K_w] and snake.trail[0].y - 1 != snake.trail[1].y:
                    snake.dir = "up"
                if keys[pg.K_s] and snake.trail[0].y + 1 != snake.trail[1].y:
                    snake.dir = "down"
                if keys[pg.K_a] and snake.trail[0].x - 1 != snake.trail[1].x:
                    snake.dir = "left"
                if keys[pg.K_d] and snake.trail[0].x + 1 != snake.trail[1].x:
                    snake.dir = "right"
            else:
                if keys[pg.K_w]:
                    snake.dir = "up"
                if keys[pg.K_s]:
                    snake.dir = "down"
                if keys[pg.K_a]:
                    snake.dir = "left"
                if keys[pg.K_d]:
                    snake.dir = "right"

            seconds = (
                pg.time.get_ticks() - start_ticks
            ) / 1000  # calculate how many seconds

            # Moving snake every 0.2 seconds
            if seconds >= 0.2:
                start_ticks = pg.time.get_ticks()  # starter tick
                if snake.dir == "up":
                    snake.move_up()
                elif snake.dir == "down":
                    snake.move_down()
                elif snake.dir == "left":
                    snake.move_left()
                elif snake.dir == "right":
                    snake.move_right()

            # Checking for collision
            if snake.trail[0].x == 0 or snake.trail[0].x == grid_size - 1:
                print("Game Over")
                running = False
            elif snake.trail[0].y == 0 or snake.trail[0].y == grid_size - 1:
                print("Game Over")
                running = False

            for i in range(2, len(snake.trail)):
                if snake.trail[0] == snake.trail[i]:
                    print("Game Over")
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("black")

            # Creating grid
            grid = Grid(screen, grid_size, square_size, spacing).grid

            # Displaying snake trail with red squares
            for point in snake.trail:
                grid[point.y][point.x].red()
            # Displaying food with orange square
            grid[food.y][food.x].orange()

            # Checking if snake ate the food (snake lands on orange square)
            if snake.trail[0] == food:
                snake.grow()
                food = Food(grid_size, snake.trail)

            # flip() the display to put your work on screen
            pg.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = clock.tick(60) / 1000

        pg.quit()
