import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position[0], self.position[1]), self.radius, 2)

    def update(self, dt):
        #direction = pygame.Vector2(0,1).rotate(dt)
        self.position += dt * self.velocity
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vector1 = self.velocity.rotate(random_angle)
            vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
            asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
            
            asteroid1.velocity = vector1 * 1.2
            asteroid2.velocity = vector2 * 1.2
            

# shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
