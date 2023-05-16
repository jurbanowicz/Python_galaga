import pygame, sys
from time import time
from level import Level
from objects.missle import Missle
from objects.player import Player
from objects.enemy import Enemy
from objects.booster import Booster
from stats.stat_saver import save_game_result

from random import randint

from settings import *
import generate

class Level_engine:
    def __init__(self) -> None:

        self.clock = pygame.time.Clock()

        self.spaceship_sprites = pygame.sprite.Group()
        self.enemies_sprites = pygame.sprite.Group()
        self.missle_sprites = pygame.sprite.Group()
        self.booster_sprites = pygame.sprite.Group()


        self.gui = Level()

        self.player = None

        self.load_map()

        self.level_done = False
        self.level = 2

        self.stage_start_time = 0
        self.booster_interval = generate.random_interval(8)
        self.last_booster_time = 0

        
    def load_map(self, preset = None):
        # preset could possibly be a file with information on how enemies should spawn in given level...
        self.player = Player((0, 0), [self.spaceship_sprites], self.missle_sprites, self.booster_sprites, self)
        self.gui.player = self.player
        self.spaceship_sprites.add(self.player)
        self.gui.visible_sprites.add(self.player)


    def generate_enemies(self, n: int):
        if (len(self.enemies_sprites) > 0 or len(self.missle_sprites) > 0 or len(self.booster_sprites) > 0):
            return
        stage_data = generate.stage(self.level)
        for enemy_type, enemy_no in stage_data.items():
            for i in range(enemy_no):
                enemy = (Enemy((randint(30, WIDTH-30), -10 + randint(-5,5)), [self.enemies_sprites, self.spaceship_sprites], enemy_type, self.missle_sprites, self))
                self.enemies_sprites.add(enemy)
                self.gui.visible_sprites.add(enemy)
        self.stage_start_time = time()
        self.level += 1
        self.booster_interval = generate.random_interval(20/(len(self.enemies_sprites)+0.01))

    def generate_boosters(self):
        if time() - self.last_booster_time > self.booster_interval:
            booster_type = generate.booster_type()
            booster = Booster((randint(30, WIDTH-30), -10), [self.booster_sprites], booster_type)
            self.booster_sprites.add(booster)
            self.gui.visible_sprites.add(booster)
            
            
            self.last_booster_time = time()
            self.booster_interval = generate.random_interval(20/(len(self.enemies_sprites)+0.01))


    def missle_fired(self, missle: Missle):
        self.missle_sprites.add(missle)
        self.gui.visible_sprites.add(missle)

    def check_collistion(self):
        for sprite in self.missle_sprites:
            if not sprite.exists:
                self.missle_sprites.remove(sprite)
                self.gui.visible_sprites.remove(sprite)
                del sprite

        for sprite in self.booster_sprites:
            if not sprite.exists:
                self.booster_sprites.remove(sprite)
                self.gui.visible_sprites.remove(sprite)
                del sprite
        
        for sprite in self.enemies_sprites:
            if not sprite.exists:
                self.enemies_sprites.remove(sprite)
                self.spaceship_sprites.remove(sprite)
                self.gui.visible_sprites.remove(sprite)
                self.player.score += sprite.exp
                del sprite
                

    def load_stage(self):
        self.enemies_sprites.update("spawn")
        self.player.update("spawn")
        self.gui.update()
        


    def stage(self):
        self.spaceship_sprites.update()
        self.missle_sprites.update()
        self.generate_boosters()

        self.check_collistion()
        self.gui.update()

    def run(self):
        while self.player.exists: 
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.player.exists = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 

            self.generate_enemies(self.level)
            self.booster_sprites.update()
            if time() - self.stage_start_time <= 1.5: 
                self.load_stage()
            else:
                self.stage()

            # self.clock.tick(FPS)
            # pygame.display.update()

        save_game_result(self.player.score)

            


    

