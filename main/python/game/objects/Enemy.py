import pygame
from settings import *

class Enemy(pygame.sprite.Sprite):

    def __init__(self, 
                 position: tuple, 
                 groups: list) -> None:
        
        super().__init__(groups)
        self.image =  pygame.image.load('main/python/resources/enemy1.png')
        self.rect = self.image.get_rect(topleft = position)
        
        self.speed = 0
        self.direction = pygame.Vector2(x = 0, y = 1)

    def move(self) -> None:
        self.rect.center += self.direction * self.speed