import pygame
import sys
import random
from config import SCREEN_NAME, SCREEN_WIDTH, SCREEN_HEIGHT, ENEMY_SPEED, ENEMY_SPAWN_TIME, ENEMY_COUNT
from entities.player import Player
from entities.crosshair import Crosshair
from entities.mob import Mob
from systems.sign import sign

pygame.init()

font = pygame.font.SysFont(None, 24)  # None = default font, 24 = velikost
hp_font = pygame.font.SysFont(None, 12)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_NAME)
clock = pygame.time.Clock()

# Entity
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
mouse_x, mouse_y = pygame.mouse.get_pos()
cross = Crosshair(mouse_x, mouse_y)

mobs = []

# Timer MOB 1,5 s
SPAWN_MOB = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_MOB, ENEMY_SPAWN_TIME)

# Levý down - stav
lmb_down = False

# Stav - byly spawnuti
already_spawned = False
spawned_counter = 0


# Hlavní herní smyčka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == SPAWN_MOB:
            if spawned_counter == ENEMY_COUNT:
                already_spawned = True
            if not already_spawned:
                spawned_counter ++1
                edge = random.choice(["top", "bottom", "left", "right"])
                if edge == "top":
                    x, y = random.randint(32, SCREEN_WIDTH - 32), -32
                elif edge == "bottom":
                    x, y = random.randint(32, SCREEN_WIDTH - 32), SCREEN_HEIGHT
                elif edge == "left":
                    x, y = -32, random.randint(32, SCREEN_HEIGHT - 32)
                else:  # right
                    x, y = SCREEN_WIDTH, random.randint(32, SCREEN_HEIGHT - 32)
                mobs.append(Mob(x, y))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                lmb_down = True
                player.fire_at(event.pos)


            elif event.button == 3:
                print(f"Pravé kliknutí na pozici: {event.pos}")
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                lmb_down = False

    
    # Generování mobs
    keys = pygame.key.get_pressed()
    dx = (keys[pygame.K_d] or keys[pygame.K_RIGHT]) - (keys[pygame.K_a] or keys[pygame.K_LEFT])
    dy = (keys[pygame.K_s] or keys[pygame.K_DOWN]) - (keys[pygame.K_w] or keys[pygame.K_UP])
    player.move(dx, dy)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    cross.rect.x = mouse_x - cross.rect.width // 2  # Centrování crosshair na myš
    cross.rect.y = mouse_y - cross.rect.height // 2

    # Střelba s držením
    if lmb_down:
        player.fire_at((mouse_x, mouse_y))

    screen.fill((30, 30, 30))

    # Debug konzole
    fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, (200, 200, 200))
    mobs_text = font.render(f"Mobs: {len(mobs)}", True, (200, 200, 200))
    spawned_text = font.render(f"Spawned: {spawned_counter}", True, (200, 200, 200))

    screen.blit(fps_text, (10, 10))
    screen.blit(mobs_text, (10, 35))
    screen.blit(spawned_text, (10, 60))

    # Mobs pohyb (směr k hráči po ose x/y)
    for mob in mobs:
        dx_unit = sign(player.rect.centerx - mob.rect.centerx)
        dy_unit = sign(player.rect.centery - mob.rect.centery)
        mob.move(dx_unit * ENEMY_SPEED, dy_unit * ENEMY_SPEED)

    # Hit check
    for bullet in list(player.gun.bullets):
        for mob in list(mobs):
            if bullet.rect.colliderect(mob.rect):
                mob.get_hit(player.gun)
                try:
                    player.gun.bullets.remove(bullet)
                except ValueError:
                    pass
                if not mob.is_alive():
                    try:
                        mobs.remove(mob)
                    except ValueError:
                        pass
                break

    player.update(SCREEN_WIDTH, SCREEN_HEIGHT)
    player.draw(screen)
    cross.draw(screen)

    # Mobs vykresleni
    for mob in mobs:
        mob.draw(screen)
        # HP tag nad mobkou
        hp_tag = hp_font.render(f"HP: {mob.hp}", True, (220, 220, 220))
        screen.blit(hp_tag, (mob.rect.x, mob.rect.y - 10))



    pygame.display.flip()

    # FPS limit
    clock.tick(60)
