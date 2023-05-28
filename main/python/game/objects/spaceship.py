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
                 level,
                 y_direction = -1) -> None:
        
        super().__init__(position, groups)


        self.last_shot = time()

        self.level = level
        self.position = position
        self.missle_sprites = missle_sprites

        self.y_direction = y_direction

    
    def shoot(self, missle_type) -> None:
        if time() - self.last_shot > self.shooting_limiter:
            self.last_shot = time()
            missle = Missle((self.position[0], self.position[1] + self.missle_location), [], missle_type, -self.y_direction)
            self.level.missle_fired(missle)

            return True
        return False

    def damage(self) -> None:
        for sprite in self.missle_sprites:
            if sprite.rect.colliderect(self.rect) and self.y_direction == sprite.direction[1]:
                sprite.exists = False
                self.life -= sprite.damage
                if self.life <= 0:
                    self.exists = False


    
    
