import pygame
from settings import *
from time import time
from objects.spaceship import Spaceship
import random

class Enemy(Spaceship):

    def __init__(self,
                 position: tuple, 
                 groups: list,
                 type: str,
                 missle_sprites: pygame.sprite.Group,
                 level) -> None:
        
        super().__init__(position, groups, missle_sprites, level)

        self.enemy_type = type
        enemy_info = enemy_data[self.enemy_type]

        self.height = enemy_info['height']
        self.width = enemy_info['width']

        self.life = enemy_info['life']

        self.shooting_limiter = enemy_info['shooting_limiter'] + random.uniform(-0.4, 0.4)
        self.missle_type = enemy_info['missle_type']
        self.missle_location = enemy_info['missle_location']

        image_path = enemy_info['image_path']
        tmp_image =  pygame.image.load(image_path)
        self.image = pygame.transform.scale(tmp_image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft = position)

        self.rect.center = position

        
        
        self.speed = enemy_info['speed']
        self.direction = pygame.Vector2()

        self.level = level
    

    def spawn(self) -> None:
        self.rect.center += pygame.math.Vector2(x = 0, y = 1)
        self.check_boundaries()
        self.position = self.rect.center

    def update(self, type = None) -> None:
        if type == "spawn":
            self.spawn()
        else:
            self.damage()
            self.shoot(self.missle_type)
            self.move()
            self.direction += pygame.math.Vector2(random.random()*2 - 1, 0)

    