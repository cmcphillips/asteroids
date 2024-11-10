import pygame
from constants import *

def main():
    print("Starting asteroids!")
    pygame.init()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        surface = pygame.display.get_surface()
        surface.fill(color = (0,0,0))
        pygame.display.flip()

# main comment for testing

if __name__ == "__main__":
    main()