import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, position: tuple, 
                 groups: list, 
                 boundary_sprites: pygame.sprite.Group,
                 missle_sprites: pygame.sprite.Group ) -> None:
        
        super().__init__(groups)
        self.image = pygame.image.load('main/python/resources/player1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)

        self.life = 100
        self.speed = 8

        self.direction = pygame.math.Vector2()

        self.boundary_sprites = boundary_sprites

    def input(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1

        else:
            self.direction.x = 0


    def move(self) -> None:
        self.rect.center += self.direction * self.speed
        self.check_boundaries()

    def check_boundaries(self) -> None:

        for sprite in self.boundary_sprites:
            if sprite.rect.colliderect(self.rect):
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.right
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.left


    def update(self) -> None:
        self.input()
        self.move()
             