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

    def is_alive(self):
        return self.hp > 0
    
    def get_hit(self, gun):
        self.hp -= getattr(gun, "damage", 0)
        if self.hp <= 0:
            self.die()
        else:
            self.image.fill((100,100,100))
    
    def die(self):
        self.hp = 0
        # Visual feedback for death; actual removal is handled by game loop
        self.image.fill((50, 50, 50))

    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
    
    