import pygame
from settings import *
from time import time
from objects.spaceship import Spaceship


class Player(Spaceship):

    def __init__(self, 
                 position: tuple, 
                 groups: list, 
                 missle_sprites: pygame.sprite.Group,
                 booster_sprites: pygame.sprite.Group ) -> None:
        
        super().__init__(position, groups, missle_sprites)
        
        self.width = 60
        self.height = 60
        tmp_image = pygame.image.load('main/python/resources/player1.png').convert_alpha()
        self.image = pygame.transform.scale(tmp_image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft = position)

        self.booster_sprites = booster_sprites


        self.life = 100
        self.speed = 8 # Modify the speed of the spaceship
        self.direction = pygame.math.Vector2()
        self.rect.center = WIDTH/2, HEIGHT - self.height

        self.shooting_limiter = 0.5 # time between shots

        self.score = 0
        
    def input(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.shoot()

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1

        else:
            self.direction.x = 0


    def update(self) -> None:
        self.input()
        self.damage()
        self.move()