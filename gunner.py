import pygame
from bullet import Bullet


class Gunner:
    GUNNER_SIZE = 50

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def redraw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.GUNNER_SIZE, self.GUNNER_SIZE))

    def move_right(self, delta):
        if self.x < 750:
            self.x = self.x + delta

    def move_left(self, delta):
        if self.x > 0:
            self.x = self.x - delta

    def fire(self):
        return Bullet(self.x + self.GUNNER_SIZE/2, self.y, 'red')
