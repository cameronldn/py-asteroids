import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

updatables = pygame.sprite.Group()
drawables = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updatables, drawables)
Asteroid.containers = (asteroids, updatables, drawables)
Shot.containers = (shots, updatables, drawables)
AsteroidField.containers = (updatables)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    delta_time = 0
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

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
        for asteroid in asteroids:
            collision = asteroid.collision_check(player)
            if collision is True:
                print("Game Over Man!")
                quit()
            for shot in shots:
                collision = asteroid.collision_check(shot)
                if collision is True:
                    shot.kill()
                    asteroid.split()
        for drawable in drawables:
            drawable.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000


if __name__ == "__main__":
    main()