import pygame
import random
from bullet import Bullet
from gunner import Gunner
from bubble import Bubble, bubble_hit_ground

# ---------------------------------------------------
# This is the entry point to the program.
# The job of this code is to do the following:
# 1. Creating window
# 2. Processing Keyboard input
# 3. Controlling the overall game loop
# ---------------------------------------------------

colors = ['blue', 'magenta', 'black', 'red', 'pink', 'dark blue', 'green', 'dark green']


def generate_bubble():
    r = random.randint(1, 200 - difficulty)
    if r == 5:
        rand_r = random.randint(30, 50)
        rand_x = random.randint(rand_r, WINDOW_WIDTH - rand_r)
        rand_c = random.randint(0, len(colors) - 1)
        bubbles.append(Bubble(rand_x, rand_r, rand_r, colors[rand_c]))


def build_text(text, loc, color=(0, 0, 0), size=50):
    font = pygame.font.Font(None, size)
    text = font.render(text, True, color)
    text_rect = text.get_rect(center=loc)
    return text, text_rect


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BG_COLOR = (250, 250, 250)

pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

running = True
bullets = []
bubbles = []

# Set the game over
game_over = False

# Set the difficulty
difficulty = 0

# Create the gunner
gunner = Gunner(
    (WINDOW_WIDTH - Gunner.GUNNER_SIZE) / 2,
    WINDOW_HEIGHT - Gunner.GUNNER_SIZE,
    'dark green'
)

while running:
    clock.tick(60)
    screen.fill(BG_COLOR)

    # Generate random bubble
    generate_bubble()

    for event in pygame.event.get():
        # Handle quit
        if event.type == pygame.QUIT:
            running = False
        # Fire code
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullet = gunner.fire()
            bullets.append(bullet)

        # Restart game
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            difficulty = 0
            game_over = False

    keys = pygame.key.get_pressed()

    # Gunner's LEFT and RIGHT movement
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if gunner.x >= 750:
            gunner.x = 0
        else:
            gunner.move_right(5)
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if gunner.x <= 0:
            gunner.x = 750
        else:
            gunner.move_left(5)

    # Draw the gunner
    gunner.redraw(screen)

    for bloop in bubbles:
        if bloop.y + bloop.radius >= WINDOW_HEIGHT:
            bubbles.remove(bloop)
        else:
            if game_over:
                bubbles.remove(bloop)
            else:
                bloop.redraw(screen)

    # Draw the bullets
    for b in bullets:
        if b.y <= 0:
            # destroy the bullet
            bullets.remove(b)
        else:
            b.redraw(screen)

    for bubble in bubbles:
        if bubble_hit_ground(bubble.y, bubble.radius):
            gamover_text, gamover_rect = build_text("game over", (400, 300), 'red', 60)
            game_over = True
            for bu in bubbles:
                bubbles.remove(bu)
        for blt in bullets:
            if bubble.intersects(blt):
                bubble.radius = 3
                bullets.remove(blt)
                difficulty += 1


    if game_over:
        screen.blit(gamover_text, gamover_rect)

    pygame.display.flip()
pygame.quit()