from objects.enemy import Enemy
from objects.missle import Missle
from settings import *
import generate
import pygame
from time import time
import random


class Boss(Enemy):
    def __init__(self,
                 position: tuple, 
                 groups: list,
                 type: str,
                 missle_sprites: pygame.sprite.Group,
                 level: object,
                 level_no: int,
                 y_direction = -1) -> None:
        
        super().__init__(position, groups, type, missle_sprites, level, y_direction)


        self.level_no = level_no
        self.last_helper_time = time()
        self.next_helper_time = generate.random_interval(24/(self.level_no+2))


    def generate_helper(self):
        if time()-self.last_helper_time >= self.next_helper_time:
            self.level.generate_boss_reinforcement((self.position[0] + (self.width/2)*random.randint(-1,1), self.position[1]))
            self.next_helper_time = generate.random_interval(96/(self.level_no+14))
            self.last_helper_time = time()

    def shoot(self, missle_type) -> None:
        if time() - self.last_shot > self.shooting_limiter:
            self.last_shot = time()

            missle = Missle((self.position[0] - 40, self.position[1] + self.missle_location), [], missle_type, -self.y_direction)
            self.level.missle_fired(missle)

            missle = Missle((self.position[0] + 40, self.position[1] + self.missle_location), [], missle_type, -self.y_direction)
            self.level.missle_fired(missle)

            return True
        return False
    
    def update(self, type = None) -> None:
        if type == "spawn":
            self.spawn()
        else:
            self.damage()
            self.shoot(self.missle_type)
            self.generate_helper()
            self.move()
            self.direction += pygame.math.Vector2(random.random()*2 - 1, 0)

