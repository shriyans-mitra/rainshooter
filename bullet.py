import pygame


class Bullet:
    BULLET_WIDTH = 6
    BULLET_HEIGHT = 10

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def redraw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.BULLET_WIDTH, self.BULLET_HEIGHT))
        self.y -= 5
