import pygame
import sys
from config import SCREEN_NAME, SCREEN_WIDTH, SCREEN_HEIGHT
from entities.player import Player
from entities.crosshair import Crosshair

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_NAME)
clock = pygame.time.Clock()

# Entities
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
mouse_x, mouse_y = pygame.mouse.get_pos()
cross = Crosshair(mouse_x, mouse_y)

shots = []

# Hlavní herní smyčka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                print(f"Levné kliknutí na pozici: {event.pos}")

                shots.append({
                    'x': mouse_x - cross.shot_image.get_width() // 2,
                    'y': mouse_y - cross.shot_image.get_height() // 2,
                    'image': cross.shot_image
                })

            elif event.button == 3:
                print(f"Pravé kliknutí na pozici: {event.pos}")

    keys = pygame.key.get_pressed()
    dx = (keys[pygame.K_d] or keys[pygame.K_RIGHT]) - (keys[pygame.K_a] or keys[pygame.K_LEFT])
    dy = (keys[pygame.K_s] or keys[pygame.K_DOWN]) - (keys[pygame.K_w] or keys[pygame.K_UP])
    player.move(dx, dy)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    cross.rect.x = mouse_x - cross.rect.width // 2  # Centrování crosshair na myš
    cross.rect.y = mouse_y - cross.rect.height // 2

    screen.fill((30, 30, 30))
    player.draw(screen)
    cross.draw(screen)
    
    for shot in shots:
        screen.blit(shot['image'], (shot['x'], shot['y']))

    pygame.display.flip()

    # FPS limit
    clock.tick(60)
