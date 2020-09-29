import pygame
import resolution

pygame.mixer.init()


class Ball:
    def __init__(self, ball_x, ball_y):
        self.ball_img = pygame.image.load("images/ball.png")
        self.rect = self.ball_img.get_rect()
        self.paddle_hit_sound = pygame.mixer.Sound("sounds/paddle_hit.wav")
        self.brick_hit_sound = pygame.mixer.Sound("sounds/brick_hit.wav")
        self.out_sound = pygame.mixer.Sound("sounds/out.wav")
        self.rect.x = ball_x
        self.rect.y = ball_y
        self.direction_x = 1
        self.direction_y = 1
        self.speed = 4
        self.score = 0
        self.lives = 5
        self.collision_number = 0
        self.screen = resolution.screen

    def draw_ball(self):
        self.screen.blit(self.ball_img, (self.rect.x, self.rect.y))

    def move(self):
        self.rect.x += self.speed * self.direction_x
        self.rect.y += self.speed * self.direction_y
        if self.rect.y < 1:
            self.rect.y = 1
            self.direction_y *= -1
        elif self.rect.y > 580:
            pygame.mixer.Sound.play(self.out_sound)
            self.lives -= 1
            self.rect.x = 25
            self.rect.y = 25
            self.collision_number = 0
        elif self.rect.x > 768:
            self.rect.x = 768
            self.direction_x *= -1
        elif self.rect.x < 1:
            self.rect.x = 1
            self.direction_x *= -1

    def collide(self, player_rect, bricks, solid_bricks):
        if self.rect.colliderect(player_rect):
            if player_rect.top <= self.rect.bottom <= player_rect.bottom - (24 - self.speed):
                pygame.mixer.Sound.play(self.paddle_hit_sound)
                self.direction_y *= -1
                self.collision_number += 1
        for i in range(len(bricks)):
            if bricks[i] != 0 and self.rect.colliderect(bricks[i].rect) and self.collision_number > 0:
                pygame.mixer.Sound.play(self.brick_hit_sound)
                if bricks[i].rect.top <= self.rect.bottom <= bricks[i].rect.bottom - (33 - self.speed) or \
                        bricks[i].rect.bottom >= self.rect.top >= bricks[i].rect.top + (33 - self.speed):
                    self.direction_y *= -1
                    bricks[i] = 0
                    self.score += 1
                else:
                    self.direction_x *= -1
                    bricks[i] = 0
                    self.score += 1
        for i in range(len(solid_bricks)):
            if solid_bricks[i] != 0 and self.rect.colliderect(solid_bricks[i].rect) and self.collision_number > 0:
                pygame.mixer.Sound.play(self.brick_hit_sound)
                if solid_bricks[i].rect.top <= self.rect.bottom <= solid_bricks[i].rect.bottom - (33 - self.speed) or \
                        solid_bricks[i].rect.bottom >= self.rect.top >= solid_bricks[i].rect.top + (33 - self.speed):
                    self.direction_y *= -1
                else:
                    self.direction_x *= -1
