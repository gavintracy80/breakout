import pygame
import resolution


class Player:
    def __init__(self):
        self.player_img = pygame.image.load("images/paddle.png")
        self.rect = self.player_img.get_rect()
        self.rect.x = 335
        self.rect.y = 550
        self.screen = resolution.screen

    def draw_player(self):
        self.screen.blit(self.player_img, (self.rect.x, self.rect.y))

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x += -8

    def move_right(self):
        if self.rect.x < 670:
            self.rect.x += 8
