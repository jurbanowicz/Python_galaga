import pygame
from settings import *
import settings
from time import time

class Player(pygame.sprite.Sprite):

    def __init__(self, position: tuple, 
                 groups: list, 
                 boundary_sprites: pygame.sprite.Group,
                 missle_sprites: pygame.sprite.Group ) -> None:
        
        super().__init__(groups)
        self.player_width = 60
        self.player_height = 60
        tmp_image = pygame.image.load('main/python/resources/player1.png').convert_alpha()
        self.image = pygame.transform.scale(tmp_image, (self.player_width, self.player_height))
        self.rect = self.image.get_rect(topleft = position)

        self.life = 100
        self.speed = 8 # Modify the speed of the spaceship
        self.rect.center = WIDTH/2, HEIGHT - 100

        self.last_shot = time()
        self.shooting_limiter = 1 # time between shots

        self.direction = pygame.math.Vector2()

        # self.boundary_sprites = boundary_sprites

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


    def move(self) -> None:
        self.rect.center += self.direction * self.speed
        self.check_boundaries()

    def shoot(self) -> None:
        if time() - self.last_shot > self.shooting_limiter:
            self.last_shot = time()

    def check_boundaries(self) -> None:

        # for sprite in self.boundary_sprites:
        #     if sprite.rect.colliderect(self.rect):
        #         if self.direction.x > 0:
        #             self.rect.right = sprite.rect.right
        #         if self.direction.x < 0:
        #             self.rect.left = sprite.rect.left

        if self.rect.center[0] - self.player_width/2 <= 0:
            self.rect.center = self.player_width/2, self.rect.center[1]
            self.direction.x = 0

        if self.rect.center[0] + self.player_width/2 >= WIDTH:
            self.rect.center = WIDTH - self.player_width/2, self.rect.center[1]
            self.direction.x = 0


    def update(self) -> None:
        self.input()
        self.move()
             