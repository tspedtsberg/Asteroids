# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from shot import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for update in updatable:
            update.update(dt)

        for obj in asteroids:
            if obj.collosion(player):
                print("Game over!")
                sys.exit()
        
            for shot in shots:
                if obj.collosion(shot):
                    shot.kill()
                    obj.split()

        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

