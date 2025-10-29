import pygame
from entities.gun import Gun

class Player:
    def __init__(self, x, y):
        self.speed = 2
        self.direction = "right"
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.gun = Gun(self)

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.gun.draw(screen)

    def update(self, screen_width, screen_height):
        self.gun.update(screen_width, screen_height)

    def fire_at(self, target_pos):
        self.gun.try_fire(target_pos)
    