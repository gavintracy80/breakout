import pygame
import player
import resolution
import brick
import ball
import score
import message


pygame.init()
pygame.mixer.init()

level_sound = pygame.mixer.Sound("sounds/level.wav")

screen = resolution.screen
pygame.display.set_caption("BreakOut")
background = pygame.image.load("images/background.png")
player = player.Player()
score = score.Score()
ball = ball.Ball(25, 25)
message = message.Message()
new_bricks = brick.NewBrick()
new_bricks.new_bricks()

level = 1
end_level = 0
end_score = 0

bottom_row_a = 36
bottom_row_b = 45

running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if message.show_message == "start":
        message.welcome_message()

    if ball.lives == 0:
        message.show_message = "game over"
        end_level = level
        end_score = ball.score
        ball.lives = 5
        ball.score = 0
        level = 1
        new_bricks.bricks = []
        new_bricks.solid_bricks = []
        new_bricks.new_bricks()
    if message.show_message == "game over":
        message.game_over_message(end_level, end_score)

    elif message.show_message == "play":

        for i in range(len(new_bricks.bricks)):
            if new_bricks.bricks[i] != 0:
                new_bricks.bricks[i].draw_brick()
        if level > 1:
            for i in range(len(new_bricks.solid_bricks)):
                if new_bricks.solid_bricks[i] != 0:
                    new_bricks.solid_bricks[i].draw_brick()

        ball.draw_ball()

        ball.move()

        ball.collide(player.rect, new_bricks.bricks, new_bricks.solid_bricks)

        player.draw_player()

        score.print_score(ball.score, ball.lives, level)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.move_left()
        if keys[pygame.K_RIGHT]:
            player.move_right()

        clear = False
        for i in range(bottom_row_a, bottom_row_b):
            if bottom_row_a >= 0 and new_bricks.bricks[i] == 0:
                clear = True
            else:
                clear = False
                break

        if clear and bottom_row_a != 0:
            pygame.mixer.Sound.play(level_sound)
            bottom_row_a -= 9
            bottom_row_b -= 9
            for i in range(len(new_bricks.bricks)):
                if new_bricks.bricks[i] != 0:
                    new_bricks.bricks[i].rect.y += 40
        elif clear and bottom_row_a == 0:
            level += 1
            ball.speed += 1
            new_bricks.bricks = []
            new_bricks.solid_bricks = []
            new_bricks.new_bricks()
            new_bricks.new_solid_bricks(level - 1)
            bottom_row_a = 36
            bottom_row_b = 45

    pygame.display.update()
