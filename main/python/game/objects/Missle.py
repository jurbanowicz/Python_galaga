import pygame
from settings import *

class Missle(pygame.sprite.Sprite):

    def __init__(self, 
                 position: tuple, 
                 groups: list,
                 y_direction: int = -1) -> None:
        
        super().__init__(groups)
        self.height = 40
        self.width = 20
        self.image =  pygame.image.load('main/python/resources/missle_red.png')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft = position)
        self.rect.center = position

        self.direction = pygame.Vector2(x = 0, y = y_direction) #y_direction = 1 lub -1
        self.speed = 5


    def move(self) -> None:
        self.rect.center += self.direction * self.speed

    def update(self) -> None:
        self.move()

