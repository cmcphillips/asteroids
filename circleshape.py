import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self, other_circle):
        distance_between_circles = pygame.math.Vector2.distance_to(self.position, other_circle.position)
        radius_sum = self.radius + other_circle.radius
        if radius_sum > distance_between_circles:
            return True
        else:
            return False