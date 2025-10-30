import pygame
from config import ENEMY_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT
from systems.sign import sign

def player_movement(player, keys):
    dx = (keys[pygame.K_d] or keys[pygame.K_RIGHT]) - (keys[pygame.K_a] or keys[pygame.K_LEFT])
    dy = (keys[pygame.K_s] or keys[pygame.K_DOWN]) - (keys[pygame.K_w] or keys[pygame.K_UP])
    player.move(dx, dy)

def mob_movement(mob, player):
    dx_unit = sign(player.rect.centerx - mob.rect.centerx)
    dy_unit = sign(player.rect.centery - mob.rect.centery)
    mob.move(dx_unit * ENEMY_SPEED, dy_unit * ENEMY_SPEED)