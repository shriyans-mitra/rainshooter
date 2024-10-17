import pygame.draw


def bubble_hit_ground(bubble_y, bubble_radius):
    if (bubble_y + bubble_radius) >= 600:
        return True
    else:
        return False


class Bubble:
    def __init__(self, x, y, radius, colour):
        self.x = x
        self.y = y
        self.colour = colour
        self.radius = radius

    def redraw(self, screen):
        self.y += 2
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)

    def intersects(self, bullet):
        if ((self.x - self.radius) < bullet.x < (self.x + self.radius)) and ((self.y - self.radius) < bullet.y < (self.y + self.radius)):
            return True
        else:
            return False

