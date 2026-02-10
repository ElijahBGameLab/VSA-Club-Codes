# MADE COMPLETELY BY COPILOT

import pygame
import random
import numpy as np

pygame.init()

# Window setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Bouncing Goober")

clock = pygame.time.Clock()

# Goober properties
x, y = WIDTH // 2, HEIGHT // 2
radius = 25
dx, dy = 4, 3
color = (255, 100, 100)

# Generate a beep sound using numpy
pygame.mixer.init(frequency=44100, size=-16, channels=1)
duration = 0.1
freq = 600
sample_rate = 44100
t = np.linspace(0, duration, int(sample_rate * duration), False)
wave = (0.5 * np.sin(2 * np.pi * freq * t)).astype(np.float32)
beep = pygame.mixer.Sound(wave)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += dx
    y += dy

    bounced = False
    if x - radius <= 0 or x + radius >= WIDTH:
        dx = -dx
        bounced = True
    if y - radius <= 0 or y + radius >= HEIGHT:
        dy = -dy
        bounced = True

    if bounced:
        color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        beep.play()

    screen.fill((30, 30, 30))
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

