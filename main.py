import pygame
from constants import * 
from player import Player
from asteroid import Asteroid
def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(x= SCREEN_WIDTH/2,y= SCREEN_HEIGHT /2)
    clock = pygame.time.Clock()
    updatable.add(player,Asteroid)
    drawable.add(player,Asteroid)
    asteroids.add(Asteroid)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        for player in updatable:
            player.update(dt)
        screen.fill("black")
        for player in drawable():
            player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()