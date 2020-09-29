import pygame
import resolution
import random


class Brick:
    def __init__(self, brick_x, brick_y, color):
        self.brick_img = pygame.image.load(color)
        self.brick_color = color
        self.rect = self.brick_img.get_rect()
        self.rect.x = brick_x
        self.rect.y = brick_y
        self.screen = resolution.screen

    def draw_brick(self):
        self.screen.blit(self.brick_img, (self.rect.x, self.rect.y))


class NewBrick:
    def __init__(self):
        self.bricks = []
        self.solid_bricks = []
        self.brick_colors = ["images/redbrick.png", "images/purplebrick.png", "images/bluebrick.png",
                             "images/orangebrick.png", "images/greenbrick.png", "images/yellowbrick.png"]

    def new_bricks(self):
        for y in range(1, 6):
            color = self.brick_colors[y - 1]
            for x in range(8, 713, 88):
                self.bricks.append(Brick(x, 40 * y, color))

    def new_solid_bricks(self, current_level):
        if current_level > 6:
            current_level = 6
        for y in range(6, 12, 2):
            random_bricks = random.sample(range(8, 713, 176), current_level)
            for x in range(8, 713, 88):
                for z in range(len(random_bricks)):
                    if random_bricks[z] == x:
                        self.solid_bricks.append(Brick(x, 40 * y, self.brick_colors[5]))
                    else:
                        self.solid_bricks.append(0)
