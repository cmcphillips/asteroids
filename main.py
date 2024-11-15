import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot

def main():
    print("Starting asteroids!")
    pygame.init()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        surface = pygame.display.get_surface()
        surface.fill(color = (0,0,0))
        
        for u in updatable:
            u.update(dt)

        for d in drawable:
            d.draw(surface)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print('Game over!')
                exit()

            for shot in shots:
                if asteroid.check_collision(shot):
                    shot.kill()
                    asteroid.split()
        # Update frame
        pygame.display.flip()
        dt = game_clock.tick(60)/1000

# main comment for testing

if __name__ == "__main__":
    main()