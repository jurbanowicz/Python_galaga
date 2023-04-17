import pygame
from settings import *

class Booster(object):
    def __init__(self, 
                 position: tuple, 
                 groups: list) -> None:
        
        super().__init__(position, groups)
        self.image =  pygame.image.load('main/python/resources/booster1.png')
        self.rect = self.image.get_rect(topleft = position)

        self.speed = 0
        self.direction = pygame.Vector2(x = 0, y = 1)    
