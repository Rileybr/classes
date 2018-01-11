# ball By Brandon Riley
# 1/11/18
# creates the ball for the classic game of breakout
import pygame
import random


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, windowWidth, windowHeight):
        """
        creates a ball with given color, window width, and window height
        :param color: color of ball
        :param windowWidth: width of the window
        :param windowHeight: height of the window
        """
        # sets up ball
        self.RADIUS = 10
        self.image = pygame.Surface((self.RADIUS, self.RADIUS))
        self.rect = self.image.get_rect()
        # makes ball circle
        pygame.draw.circle(self.image, color, (self.rect.x + 5, self.rect.y + 5), int(self.RADIUS / 2))
        # sets speed of ball
        self.speedx = random.randint(2, 4)
        self.speedy = 5
        self.window_width = windowWidth
        self.window_height = windowHeight

    def move(self):
        """
        sets speed of ball and constrains it within the window
        :return:
        """
        # moves the ball
        self.rect.top += self.speedy
        self.rect.left += self.speedx
        # checks if ball hits walls of the window and switches direction of ball
        if self.rect[0] >= self.window_width - 10 or self.rect[0] <= 0:
            self.speedx = - self.speedx
            pygame.mixer.music.load("bell.wav")
            pygame.mixer.music.play()
        # checks if ball hits walls of the window and switches direction of ball
        if self.rect[1] <= 0:
            self.speedy = - self.speedy
            pygame.mixer.music.load("bell.wav")
            pygame.mixer.music.play()

    def collide_paddle(self, sprite_group):
        """
        checks if the ball collides with the paddle and changes the direction of the ball if it occurs
        :param sprite_group: the paddle
        :return:
        """
        if pygame.sprite.spritecollide(self, sprite_group, False):
            self.speedy = -self.speedy
            pygame.mixer.music.load("bell.wav")
            pygame.mixer.music.play()

    def collide_brick(self, sprite_group):
        """
        checks if the ball collides with a brick, changes the direction of the ball if it occurs and deletes the brick
        :param sprite_group: the brick group
        :return:
        """
        if pygame.sprite.spritecollide(self, sprite_group, True):
            self.speedy = -self.speedy
            pygame.mixer.music.load("bell.wav")
            pygame.mixer.music.play()

