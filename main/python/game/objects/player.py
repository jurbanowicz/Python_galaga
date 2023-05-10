import pygame
from settings import *
from time import time
from objects.spaceship import Spaceship
# from level_engine import Level_engine

class Player(Spaceship):

    def __init__(self, 
                position: tuple, 
                groups: list, 
                missle_sprites: pygame.sprite.Group,
                booster_sprites: pygame.sprite.Group,
                level) -> None:
        
        super().__init__(position, groups, missle_sprites, level)
        
        self.width = 75
        self.height = 75
        tmp_image = pygame.image.load('main/python/resources/player2.png').convert_alpha()
        self.image = pygame.transform.scale(tmp_image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft = position)

        self.level = level

        self.booster_sprites = booster_sprites

        self.life = 100
        self.speed = 8 # Modify the speed of the spaceship
        self.direction = pygame.math.Vector2()
        self.rect.center = WIDTH/2, HEIGHT - self.height

        self.shooting_limiter = 0.2 # time between shots

        self.position = self.rect.center

        self.score = 0

        self.missles = {"bomb" : 10}
        
    def input(self, type = None) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and type != "spawn":
            self.shoot(missle_type = "basic", direction = -1)
        
        if keys[pygame.K_q] and type != "spawn":
            if self.missles["bomb"] > 0:
                if self.shoot(missle_type = "bomb", direction = -1):
                    self.missles["bomb"] -= 1

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1

        else:
            self.direction.x = 0

    def update(self, type = None) -> None:
        self.input(type)
        self.damage()
        self.move()
