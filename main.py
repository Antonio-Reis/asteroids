from constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
from logger import log_state
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from logger import log_event
import sys
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    
    #creating groups
    updatable = pygame.sprite.Group()
    drawable =  pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    #creating containers
    Player.containers = (updatable, drawable)
    Asteroid.containers =(asteroids,updatable,drawable)
    AsteroidField.containers =(updatable)
    Shot.containers = (shots,updatable, drawable)
    
    #Class objects
    player=Player(x,y)
    asteroidf = AsteroidField()
    
    
    # GAME LOOP
    while True:
        log_state()
        for event in pygame.event.get():
	        if event.type == pygame.QUIT:
                    return
        updatable.update(dt)
        
        #collision check
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event('player_hit')
                print('Game over!')
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event('asteroid_shot')
                    shot.kill()
                    asteroid.kill()
                        
        
        #start drawing
        screen.fill('black')
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        



if __name__ == "__main__":
    main()
