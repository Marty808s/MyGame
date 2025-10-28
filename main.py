import pygame
import sys
from config import SCREEN_NAME, SCREEN_WIDTH, SCREEN_HEIGHT
from entities.player import Player

pygame.init()

# Settings from config.py

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_NAME)

clock = pygame.time.Clock()

# Entities
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

# Hlavní herní smyčka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Vstup
    keys = pygame.key.get_pressed()
    dx = (keys[pygame.K_d] or keys[pygame.K_RIGHT]) - (keys[pygame.K_a] or keys[pygame.K_LEFT])
    dy = (keys[pygame.K_s] or keys[pygame.K_DOWN]) - (keys[pygame.K_w] or keys[pygame.K_UP])
    player.move(dx, dy)

    # Vybarvení pozadí (RGB)
    screen.fill((30, 30, 30))
    player.draw(screen)

    # Aktualizace obrazovky
    pygame.display.flip()

    # FPS limit
    clock.tick(60)
