import pygame
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    delta_time = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    gameRunning = True;

    while gameRunning:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(000)
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000


if __name__ == "__main__":
    main()