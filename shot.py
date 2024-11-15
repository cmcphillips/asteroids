import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position[0], self.position[1]), self.radius, 2)

    def update(self, dt):
        self.position += dt * self.velocity