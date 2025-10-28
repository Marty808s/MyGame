import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.direction = "right"
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)