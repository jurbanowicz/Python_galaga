import pygame
from settings import *
from time import time
from objects.entity import Entity
from objects.missle import Missle
# from level_engine import Level_engine

import random

class Spaceship(Entity):

    def __init__(self,
                 position: tuple,
                 groups: list,
                 missle_sprites: pygame.sprite.Group,
                 level) -> None:
        
        super().__init__(position, groups)

        self.life = 50

        self.last_shot = time()
        self.shooting_limiter = 1 + random.uniform(-0.4, 0.4) # time between shots

        self.level = level
        self.position = position
        self.missle_sprites = missle_sprites

    

    def shoot(self, direction = 1) -> None:
        if time() - self.last_shot > self.shooting_limiter:
            self.last_shot = time()
            # self.shot_fired = True
            missle = Missle((self.position[0], self.position[1] + direction*50), [], 'basic', direction)
            self.level.missle_fired(missle)
            # print(f'SHOT FIRED: {self.shot_fired}')
            print(self.position)


    def damage(self) -> None:
        for sprite in self.missle_sprites:
            if sprite.rect.colliderect(self.rect):
                sprite.exists = False
                self.life -= sprite.damage
                if self.life <= 0:
                    self.exists = False


    
    
