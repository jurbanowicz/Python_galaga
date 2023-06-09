import pygame
from settings import *
from time import time
from objects.spaceship import Spaceship
from objects.enemy import Enemy
# from level_engine import Level_engine

class Player(Spaceship):

    def __init__(self, 
                position: tuple, 
                groups: list, 
                missle_sprites: pygame.sprite.Group,
                booster_sprites: pygame.sprite.Group,
                level) -> None:
        
        super().__init__(position, groups, missle_sprites, level)
        
        player_info = player_data['basic']

        self.width = player_info['width']
        self.height = player_info['height']

        tmp_image = pygame.image.load(player_info['image_path']).convert_alpha()
        self.image = pygame.transform.scale(tmp_image, (self.width, self.height))
        self.rect = self.image.get_rect(topleft = position)

        self.level = level

        self.booster_sprites = booster_sprites

        self.life = player_info['life']
        self.speed = player_info['speed'] # Modify the speed of the spaceship
        self.direction = pygame.math.Vector2()
        self.y_direction = 1
        self.rect.center = WIDTH/2, HEIGHT - self.height

        self.shooting_limiter = player_info['shooting_limiter'] # time between shots
        self.missle_location = player_info['missle_location']

        self.position = self.rect.center

        self.score = 0

        self.missles = {"bomb" : 10}
        
    def input(self, type = None) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and type != "spawn":
            self.shoot(missle_type = "basic")
        
        if keys[pygame.K_q] and type != "spawn":
            if self.missles["bomb"] > 0:
                if self.shoot(missle_type = "bomb"):
                    self.missles["bomb"] -= 1

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1

        else:
            self.direction.x = 0

    def upgrade(self):
        for sprite in self.booster_sprites:
            if sprite.rect.colliderect(self.rect):
                sprite.exists = False
                self.powerup(sprite.booster_type)

    def powerup(self, type: str)-> None:
        match type:
            case 'health':
                self.life += 3

            case 'bomb':
                self.missles['bomb'] += 1

            case 'reinforcement':
                self.level.generate_player_reinforcement(self.score)

            case 'xp':
                self.score += 20
                




    def update(self, type = None) -> None:
        self.input(type)
        self.damage()
        self.upgrade()
        self.move()
