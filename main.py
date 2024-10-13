import pygame
import time
from bullet import Bullet

pygame.init()

screen = pygame.display.set_mode((800, 600))
BG_color = (250, 250, 250)

clock = pygame.time.Clock()
x = 0
y= 550
running = True
bullets = []
while running:

    clock.tick(60)
    screen.fill(BG_color)

    for event in pygame.event.get():
        # handle quit
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Gunner LEFT and RIGHT movement
    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and x < 750:
        x += 5
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and x > 0:
        x -= 5

    # Fire code
    if keys[pygame.K_SPACE]:
        bullet = Bullet(x + 22, 550)
        bullets.append(bullet)

    # Draw the gunner
    pygame.draw.rect(screen, 'dark  green', (x, y, 50, 50))

    # Draw the bullets
    for b in bullets:
        if b.y <= 0:
            # destroy the bullet
            bullets.remove(b)
        else:
            pygame.draw.rect(screen, 'red', (b.x, b.y, 6, 10))
            b.y -= 5

    pygame.display.flip()
pygame.quit()
