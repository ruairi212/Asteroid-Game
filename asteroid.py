import pygame
from circleshape import CircleShape

class Asteroid:
    def __init__(self, x, y, radius):
        super(CircleShape).__init__(x,y,radius)
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,2)
    def update(self,dt):
        self.move(velocity * dt)
    