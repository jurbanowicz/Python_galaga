import pygame
from settings import *
from objects.entity import Entity

class Missle(Entity):

    def __init__(self, 
                 position: tuple, 
                 groups: list,
                 type: str,
                 y_direction: int) -> None:
        
        super().__init__(position, groups)
        self.missle_type = type
        missle_info = missle_data[self.missle_type]



        self.height = missle_info['height']
        self.width = missle_info['width']

        image_path = missle_info['image_path']
        self.image =  pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft = position)
        
        self.rect.center = position

        self.direction = pygame.Vector2(x = 0, y = y_direction) #y_direction = 1 lub -1
        self.speed = missle_info['speed']

        self.damage = missle_info['damage']

        # self.spaceship_sprites = spaceship_sprites



    def check_boundaries(self) -> None:
        if self.rect.center[1] <= 0 or self.rect.center[1] > HEIGHT:
            self.exists = False

    