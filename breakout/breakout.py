# Breakout By Brandon Riley
# 1/11/18
# Has player engage in the classic game of breakout
import pygame
import sys
import ball
import brick
import paddle
from pygame.locals import *


def main():

    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH = (APPLICATION_WIDTH - (BRICKS_PER_ROW - 1) * BRICK_SEP) / BRICKS_PER_ROW
    NUM_TURNS = 3
    pygame.init()
    main_surface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    pygame.display.set_caption("BREAKOUT")
    main_surface.fill((66, 75, 124))

    # Sets up the colors
    RED = (255, 144, 0)
    ORANGE = (255, 187, 40)
    YELLOW = (255, 197, 73)
    GREEN =(255, 218, 140)
    CYAN = (255, 229, 175)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    paddle_group = pygame.sprite.Group()
    brick_group = pygame.sprite.Group()
    my_brick = brick.Brick(BRICK_WIDTH, RED)
    win_num = 0
    lose_num = 0

    # Sets up bricks
    x_position = 0
    y_position = BRICK_Y_OFFSET
    color_of_brick = [RED, ORANGE, YELLOW, GREEN, CYAN]
    for g in range(5):
        for h in range(2):
            for z in range(BRICKS_PER_ROW):
                my_brick = brick.Brick(BRICK_WIDTH, color_of_brick[g])
                brick_group.add(my_brick)
                my_brick.rect.y = y_position
                my_brick.rect.x = x_position
                main_surface.blit(my_brick.image, my_brick.rect)
                x_position += BRICK_WIDTH + BRICK_SEP
            y_position += my_brick.BRICK_HEIGHT + BRICK_SEP
            x_position = 0

    # Sets up paddle
    my_paddle = paddle.Paddle(WHITE)
    my_paddle.rect.x = 170
    my_paddle.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    main_surface.blit(my_paddle.image, my_paddle.rect)
    paddle_group.add(my_paddle)

    # Sets up ball
    my_ball = ball.Ball(WHITE, APPLICATION_WIDTH, APPLICATION_HEIGHT)
    my_ball.rect.x = APPLICATION_WIDTH / 2 - 5
    my_ball.rect.y = APPLICATION_HEIGHT / 2 - 5

    main_surface.blit(my_ball.image, my_ball.rect)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                #  closes window when pressing the quit button
                pygame.quit()
                sys.exit()
        mouse_position = pygame.mouse.get_pos()
        main_surface.fill(BLACK)
        # creates bricks
        for x in brick_group:
            main_surface.blit(x.image, x.rect)
        # moves paddle based upon the given position of the mouse
        if 370 >= mouse_position[0] >= 30:
            my_paddle.move(mouse_position[0] - 30)

            main_surface.blit(my_paddle.image, my_paddle.rect)
        if mouse_position[0] > 370:

            main_surface.blit(my_paddle.image, (340, my_paddle.rect.y))
        if mouse_position[0] < 30:

            main_surface.blit(my_paddle.image, (0, my_paddle.rect.y))

        # moves ball and checks for collisions
        my_ball.move()

        my_ball.collide_paddle(paddle_group)
        my_ball.collide_brick(brick_group)

        # checks if ball hits bottom of screen
        if my_ball.rect.y >= APPLICATION_HEIGHT - 10:
            NUM_TURNS += -1
            my_ball.rect.x = APPLICATION_WIDTH/2
            my_ball.rect.y = APPLICATION_HEIGHT/2
            my_ball.speedx = -my_ball.speedx

        # sets up lives label in top left corner
        my_font = pygame.font.SysFont("helvetica", 25)
        lives_label = my_font.render("Lives:", 1, WHITE)
        main_surface.blit(lives_label, (10, 10))
        lives = my_font.render(str(NUM_TURNS), 1, WHITE)
        main_surface.blit(lives, (60, 10))

        # checks if you lose and prints game over screen
        if NUM_TURNS <= 0:
            pygame.draw.rect(main_surface, BLACK, (0, 0, APPLICATION_WIDTH, APPLICATION_HEIGHT))
            my_ball = ball.Ball(BLACK, APPLICATION_WIDTH, APPLICATION_HEIGHT)
            my_font = pygame.font.SysFont("helvetica", 75)
            game_over = my_font.render("GAME OVER", 1, WHITE)
            main_surface.blit(game_over, (35, ((APPLICATION_HEIGHT / 2) - 75)))
            lose_num += 1
            if lose_num == 1:
                pygame.mixer.music.load("you lose.mp3")
                pygame.mixer.music.play()

        # checks if you win and prints you win screen
        if len(brick_group) <= 0:
            pygame.draw.rect(main_surface, BLACK, (0, 0, APPLICATION_WIDTH, APPLICATION_HEIGHT))
            my_ball = ball.Ball(BLACK, APPLICATION_WIDTH, APPLICATION_HEIGHT)
            my_font = pygame.font.SysFont("helvetica", 75)
            you_win = my_font.render("YOU WIN", 1, WHITE)
            main_surface.blit(you_win, (80, ((APPLICATION_HEIGHT/2) - 75)))
            win_num += 1
            if win_num == 1:
                pygame.mixer.music.load("you win.wav")
                pygame.mixer.music.play()

        main_surface.blit(my_ball.image, my_ball.rect)
        pygame.display.update()

main()
