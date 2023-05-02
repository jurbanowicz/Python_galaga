import pygame
from level import Level
from objects.missle import Missle
from objects.player import Player
from objects.enemy import Enemy

from random import randint

from settings import *

class Level_engine:
    def __init__(self) -> None:

        self.spaceship_sprites = pygame.sprite.Group()
        self.enemies_sprites = pygame.sprite.Group()
        self.missle_sprites = pygame.sprite.Group()
        self.booster_sprites = pygame.sprite.Group()

        self.gui = Level()

        self.player = None

        self.load_map()

        
    def load_map(self, preset = None):
        # preset could possibly be a file with information on how enemies should spawn in given level...
        self.player = Player((0, 0), [self.spaceship_sprites], self.missle_sprites, self.booster_sprites, self)
        self.gui.player = self.player
        self.spaceship_sprites.add(self.player)
        self.gui.visible_sprites.add(self.player)


    def generate_enemies(self, n: int):
        if (len(self.enemies_sprites) > 0):
            return
        for i in range(n):
            enemy = (Enemy((randint(30, WIDTH-30), 70), [self.enemies_sprites, self.spaceship_sprites], 'basic', self.missle_sprites, self))
            self.enemies_sprites.add(enemy)
            self.gui.visible_sprites.add(enemy)


    def missle_fired(self, missle: Missle):
        self.missle_sprites.add(missle)
        self.gui.visible_sprites.add(missle)

    def check_missle_collistion(self):
        for sprite in self.missle_sprites:
            if not sprite.exists:
                self.missle_sprites.remove(sprite)
                self.gui.visible_sprites.remove(sprite)
                del sprite
        for sprite in self.enemies_sprites:
            if not sprite.exists:
                self.enemies_sprites.remove(sprite)
                self.spaceship_sprites.remove(sprite)
                self.gui.visible_sprites.remove(sprite)
                del sprite
                self.player.score += 10

    def get_score(self):
        return self.player.score()

    def run(self):
        self.spaceship_sprites.update()
        self.missle_sprites.update()
        self.generate_enemies(3)
        self.check_missle_collistion()
        self.gui.update()

    

