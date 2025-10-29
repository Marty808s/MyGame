import math
import pygame


class Bullet:
    def __init__(self, x, y, vx, vy, color=(255, 255, 255)):
        self.pos_x = float(x)
        self.pos_y = float(y)
        self.vel_x = float(vx)
        self.vel_y = float(vy)
        self.surface = pygame.Surface((4, 4))
        self.surface.fill(color)
        self.rect = self.surface.get_rect(center=(int(self.pos_x), int(self.pos_y)))

    def update(self):
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
        self.rect.centerx = int(self.pos_x)
        self.rect.centery = int(self.pos_y)

    def draw(self, screen):
        screen.blit(self.surface, self.rect)


class Gun:
    def __init__(self, owner):
        self.owner = owner
        self.name = "Zbraň"
        self.cooldown_ms = 200
        self.last_shot_time = 0
        self.bullet_speed = 9
        self.damage = 10
        self.bullets = []

    def _can_fire(self, now_ms):
        return now_ms - self.last_shot_time >= self.cooldown_ms

    def try_fire(self, target_pos):
        now = pygame.time.get_ticks()
        if not self._can_fire(now):
            return False

        ox, oy = self.owner.rect.centerx, self.owner.rect.centery
        tx, ty = target_pos
        dir_x = tx - ox
        dir_y = ty - oy
        length = math.hypot(dir_x, dir_y)
        if length == 0:
            return False

        unit_x = dir_x / length
        unit_y = dir_y / length
        vx = unit_x * self.bullet_speed
        vy = unit_y * self.bullet_speed

        spawn_x = ox + unit_x * 18
        spawn_y = oy + unit_y * 18

        bullet = Bullet(spawn_x, spawn_y, vx, vy)
        self.bullets.append(bullet)
        self.last_shot_time = now
        return True

    def update(self, screen_width, screen_height):
        alive = []
        for b in self.bullets:
            b.update()
            if -10 <= b.rect.centerx <= screen_width + 10 and -10 <= b.rect.centery <= screen_height + 10:
                alive.append(b)
        self.bullets = alive

    def draw(self, screen):
        for b in self.bullets:
            b.draw(screen)