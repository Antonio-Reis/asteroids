from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x:float, y:float, radius:float) -> None:
        super().__init__(x,y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, 'white', self.position, self.radius,LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius<=ASTEROID_MIN_RADIUS:
            return
        log_event('asteroid_split')
        angle = random.uniform(20,50)
        first_ast_vect = self.velocity.rotate(angle)
        second_ast_vect = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        #instatiation new asteroids
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        #velocity update
        asteroid_1.velocity = first_ast_vect* 1.2
        asteroid_2.velocity = second_ast_vect * 1.2
        
        
