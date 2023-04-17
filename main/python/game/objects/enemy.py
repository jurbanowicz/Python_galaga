import pygame
from settings import *
from time import time
from objects.spaceship import Spaceship

class Enemy(Spaceship):

    def __init__(self,
                 position: tuple, 
                 groups: list,
                 type: str,
                 missle_sprites: pygame.sprite.Group) -> None:
        
        super().__init__(position, groups, missle_sprites)

        self.enemy_type = type
        enemy_info = enemy_data[self.enemy_type]

        self.height = enemy_info['height']
        self.width = enemy_info['width']

        image_path = enemy_info['image_path']
        tmp_image =  pygame.image.load(image_path)
        self.image = pygame.transform.scale(tmp_image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft = position)

        self.rect.center = position
        
        self.speed = enemy_info['speed']
        self.direction = pygame.Vector2()

        self.shooting_limiter = 0.5 # time between shots

    def update(self) -> None:
        self.damage()
        self.move()