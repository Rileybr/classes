# paddle By Brandon Riley
# 1/11/18
# creates the paddle for the classic game of breakout
import pygame


class Paddle(pygame.sprite.Sprite):
    def __init__(self, color):
        """
        creates the paddle using the given color
        :param color: color of the paddle
        """
        # sets up paddle
        super().__init__()
        self.WIDTH = 60
        self.HEIGHT = 10
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, mouse_x):
        """
        moves the mouse rectangle to the mouse x position
        :param mouse_x: the position of the mouse in the x plane
        :return:
        """
        self.rect.x = mouse_x
