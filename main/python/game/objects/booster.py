import pygame
from objects.entity import Entity
from settings import *

class Booster(Entity):
    def __init__(self, 
                 position: tuple, 
                 groups: list,
                 type: str) -> None:
        
        super().__init__(position, groups)

        self.booster_type = type
        booster_info = booster_data[self.booster_type]

        self.height = booster_info['height']
        self.width = booster_info['width']


        tmp_image =  pygame.image.load(booster_info['image_path'])
        self.image = pygame.transform.scale(tmp_image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft = position)

        self.rect = self.image.get_rect(topleft = position)

        self.speed = booster_info['speed']
        self.direction = pygame.Vector2(x = 0, y = 1)    


    def check_boundaries(self) -> None:
        if self.rect.center[1] > HEIGHT:
            self.exists = False