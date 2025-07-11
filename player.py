import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    shoot_rate_limit = 0

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, surface):
        pygame.draw.polygon(surface, (255,255,255), self.triangle(), 2)

    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time

    def update(self, delta_time):
        self.shoot_rate_limit -= delta_time
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-delta_time)
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        if keys[pygame.K_w]:
            self.move(delta_time)
        if keys[pygame.K_s]:
            self.move(-delta_time)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, delta_time):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta_time

    def shoot(self):
        if self.shoot_rate_limit > 0:
            return
        self.shoot_rate_limit = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1)
        shot.velocity = shot.velocity.rotate(self.rotation)
        shot.velocity *= PLAYER_SHOOT_SPEED