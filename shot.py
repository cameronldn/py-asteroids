import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color(255,255,255), (self.position.x, self.position.y), SHOT_RADIUS, 2)

    def update(self, delta_time):
        self.position += (self.velocity * delta_time)  
    