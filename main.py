import pygame
import sys
from config import SCREEN_NAME, SCREEN_WIDTH, SCREEN_HEIGHT

pygame.init()

# Settings from config.py

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_NAME)

clock = pygame.time.Clock()

# Hlavní herní smyčka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Vybarvení pozadí (RGB)
    screen.fill((30, 30, 30))

    # Aktualizace obrazovky
    pygame.display.flip()

    # FPS limit
    clock.tick(60)
