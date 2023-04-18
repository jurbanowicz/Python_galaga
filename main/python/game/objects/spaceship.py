import pygame
from settings import *
from time import time
from objects.entity import Entity

class Spaceship(Entity):

    def __init__(self,
                 position: tuple,
                 groups: list,
                 missle_sprites: pygame.sprite.Group ) -> None:
        
        super().__init__(position, groups)

        self.life = 50

        self.last_shot = time()
        self.shot_fired = False
        self.shooting_limiter = 1 # time between shots

        self.missle_sprites = missle_sprites

    

    def shoot(self) -> None:
        if time() - self.last_shot > self.shooting_limiter:
            self.last_shot = time()
            self.shot_fired = True
            print(f'SHOT FIRED: {self.shot_fired}')


    def damage(self) -> None:
        for sprite in self.missle_sprites:
            if sprite.rect.colliderect(self.rect):
                sprite.exists = False
                self.life -= sprite.damage
                if self.life <= 0:
                    self.exists = False


    
    
