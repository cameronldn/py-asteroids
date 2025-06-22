import pygame
from constants import *
from player import Player

updatables = pygame.sprite.Group()
drawables = pygame.sprite.Group()
Player.containers = (updatables, drawables)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    delta_time = 0
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    gameRunning = True;

    while gameRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(000)
        updatables.update(delta_time)
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000


if __name__ == "__main__":
    main()