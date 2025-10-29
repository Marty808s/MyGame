import pygame

class Mob:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.hp = 100
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        print("Mobka: ", self.rect.x, self.rect.y)

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
    