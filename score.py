import pygame
import resolution


class Score:
    def __init__(self):
        self.screen = resolution.screen

    def print_score(self, current_score, lives, level):
        font = pygame.font.Font('freesansbold.ttf', 32)
        score_text = font.render('Score: {0}'.format(current_score), True, (255, 255, 255))
        lives_text = font.render('Lives: {0}'.format(lives), True, (255, 255, 255))
        level_text = font.render('Level: {0}'.format(level), True, (255, 255, 255))
        self.screen.blit(score_text, (5, 5))
        self.screen.blit(lives_text, (350, 5))
        self.screen.blit(level_text, (650, 5))
