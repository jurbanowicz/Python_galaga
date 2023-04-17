import pygame
from settings import *
from time import time



class Entity(pygame.sprite.Sprite):

    def __init__(self,
                 position: tuple,
                 groups: list) -> None:
        
        super().__init__(groups)

        self.width = 60
        self.height = 60

        tmp_image = pygame.image.load('main/python/resources/default.png').convert_alpha()
        self.image = pygame.transform.scale(tmp_image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft = position)

        self.speed = 5 # Modify the speed of the spaceship
        self.direction = pygame.Vector2()
        self.rect.center = WIDTH/2, HEIGHT

        self.exists = True

    def get_postition(self):
        return self.rect.center
    
    def move(self) -> None:
        self.rect.center += self.direction * self.speed
        self.check_boundaries()

    def check_boundaries(self) -> None:

        if self.rect.center[0] - self.width/2 <= 0:
            self.rect.center = self.width/2, self.rect.center[1]
            self.direction.x = 0

        if self.rect.center[0] + self.width/2 >= WIDTH:
            self.rect.center = WIDTH - self.width/2, self.rect.center[1]
            self.direction.x = 0



    def update(self) -> None:
        self.move()
