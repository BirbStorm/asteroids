# install pygame
import pygame
from player import Player
from constants import *



def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()