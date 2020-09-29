import pygame
import resolution


class Message:
    def __init__(self):
        self.extra_large_font = pygame.font.Font('freesansbold.ttf', 50)
        self.large_font = pygame.font.Font('freesansbold.ttf', 32)
        self.small_font = pygame.font.Font('freesansbold.ttf', 24)
        self.show_message = "start"
        self.screen = resolution.screen
        self.background = pygame.image.load("images/message.png")

    def welcome_message(self):
        self.screen.blit(self.background, (25, 25))
        rules_one_text = self.small_font.render('Break all the blocks to get to next level', True, (255, 255, 255))
        rules_two_text = self.small_font.render('Yellow blocks can not be broken', True, (255, 255, 255))
        start_text = self.large_font.render('Press Space To Start', True, (255, 255, 255))
        self.screen.blit(rules_one_text, (180, 300))
        self.screen.blit(rules_two_text, (210, 350))
        self.screen.blit(start_text, (230, 400))
        start_key = pygame.key.get_pressed()
        if start_key[pygame.K_SPACE]:
            self.show_message = "play"

    def game_over_message(self, level, score):
        self.screen.blit(self.background, (25, 25))
        game_over_text = self.extra_large_font.render('Game Over', True, (255, 255, 255))
        level_score_text = self.large_font.render('You scored {} and got to level {} '.format(score, level), True,
                                                  (255, 255, 255))
        start_text = self.large_font.render('Press Space To Restart', True, (255, 255, 255))
        self.screen.blit(game_over_text, (260, 270))
        self.screen.blit(level_score_text, (160, 350))
        self.screen.blit(start_text, (220, 400))
        start_key = pygame.key.get_pressed()
        if start_key[pygame.K_SPACE]:
            self.show_message = "play"
