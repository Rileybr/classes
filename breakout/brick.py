# Brick By Brandon Riley
# 1/11/18
# creates the brick for the classic game of breakout
import pygame


class Brick(pygame.sprite.Sprite):
    def __init__(self, width, color):
        """
        creates brick with given color and width of the bricks
        :param width: width of a brick
        :param color: color of a brick
        """
        # sets up a brick
        super().__init__()
        self.BRICK_HEIGHT = 8
        self.image = pygame.Surface((width, self.BRICK_HEIGHT))
        self.image.fill(color)
        self.rect = self.image.get_rect()

