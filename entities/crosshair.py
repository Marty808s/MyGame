import pygame

class Crosshair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.image = pygame.Surface((10, 10))
        self.image.fill((120, 120, 120))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Load shot image
        self.shot_image = pygame.image.load("assets/shot.png")

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

